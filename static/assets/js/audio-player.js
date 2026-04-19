/* ================================================================
   Audio Player v4.1 — Professional TTS for Article Pages
   MenshlyGlobal Client-Side Logic

   Engine: Edge TTS Neural Voices (via /api/tts) with browser fallback
   Design: Pill-shaped player with animated wave bars + progress bar

   Key improvements over v3.0:
   - Edge TTS provides professional neural voices (no API key needed)
   - Cloud TTS eliminates Chrome 15-second cutoff entirely
   - Real progress bar showing playback position
   - HTML5 Audio API for reliable playback (no keepalive hacks)
   - Seamless fallback to browser TTS if cloud unavailable
   - Voice selection with multiple neural voice options
   ================================================================ */
(function() {
  'use strict';

  /* ---- State ---- */
  var engine = 'none'; // 'cloud' | 'browser' | 'none'
  var audioEl = null;  // HTML5 Audio element for cloud TTS
  var synth = window.speechSynthesis || null;
  var playing = false;
  var paused = false;
  var speeds = [0.75, 1, 1.25, 1.5, 2];
  var speedIdx = 1;
  var currentUtterance = null;
  var articleChunks = [];
  var chunkIndex = 0;
  var voicesLoaded = false;
  var cachedVoice = null;
  var cloudAudioCache = {};  // chunkIndex -> objectURL
  var isGenerating = false;
  var progressTimer = null;
  var selectedVoice = 'en-US-AriaNeural';  // Default neural voice
  var availableVoices = {};  // Populated from server
  var voiceMenuOpen = false;

  /* ---- SVG Icons (Feather-style) ---- */
  var ICONS = {
    headphones:
      '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' +
        '<path d="M3 18v-6a9 9 0 0 1 18 0v6"/>' +
        '<path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>' +
      '</svg>',
    play:
      '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none">' +
        '<polygon points="6 3 20 12 6 21 6 3"/>' +
      '</svg>',
    pause:
      '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none">' +
        '<rect x="5" y="3" width="4" height="18" rx="1"/>' +
        '<rect x="15" y="3" width="4" height="18" rx="1"/>' +
      '</svg>',
    skip:
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
        '<polygon points="5 4 15 12 5 20 5 4"/>' +
        '<line x1="19" y1="5" x2="19" y2="19"/>' +
      '</svg>',
    speed:
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
        '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>' +
      '</svg>',
    close:
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">' +
        '<line x1="18" y1="6" x2="6" y2="18"/>' +
        '<line x1="6" y1="6" x2="18" y2="18"/>' +
      '</svg>',
    voice:
      '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
        '<path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>' +
        '<path d="M19 10v2a7 7 0 0 1-14 0v-2"/>' +
        '<line x1="12" y1="19" x2="12" y2="23"/>' +
        '<line x1="8" y1="23" x2="16" y2="23"/>' +
      '</svg>',
    chevronDown:
      '<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">' +
        '<polyline points="6 9 12 15 18 9"/>' +
      '</svg>'
  };

  /* ================================================================
     CLOUD TTS — Calls /api/tts endpoint for professional AI voices
     ================================================================ */

  function detectCloudTTS() {
    /* Probe the /api/tts endpoint to see if it's available */
    return fetch('/api/tts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action: 'ping' })
    }).then(function(r) {
      if (r.ok) return r.json();
      throw new Error('not available');
    }).then(function(data) {
      if (data.available) {
        engine = 'cloud';
        if (data.defaultVoice) selectedVoice = data.defaultVoice;
        /* Fetch available voices */
        fetchVoices();
        return true;
      }
      throw new Error('not available');
    }).catch(function() {
      engine = synth ? 'browser' : 'none';
      return false;
    });
  }

  function fetchVoices() {
    fetch('/api/tts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ action: 'voices' })
    }).then(function(r) { return r.json(); }).then(function(data) {
      if (data.voices) availableVoices = data.voices;
    }).catch(function() {});
  }

  function requestCloudTTS(text, index) {
    return fetch('/api/tts', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        action: 'generate',
        text: text,
        voice: selectedVoice,
        speed: speeds[speedIdx]
      })
    }).then(function(r) {
      if (!r.ok) {
        /* If cloud TTS fails, throw to trigger fallback */
        return r.json().then(function(err) {
          throw new Error(err.error || 'TTS request failed: ' + r.status);
        }).catch(function(e) {
          if (e.message && e.message.indexOf('TTS request failed') === -1) throw e;
          throw new Error('TTS request failed: ' + r.status);
        });
      }
      return r.arrayBuffer();
    }).then(function(buffer) {
      var blob = new Blob([buffer], { type: 'audio/mpeg' });
      var url = URL.createObjectURL(blob);
      cloudAudioCache[index] = url;
      return url;
    });
  }

  function playCloudChunk() {
    if (!playing || chunkIndex >= articleChunks.length) {
      onEnd();
      return;
    }

    var text = articleChunks[chunkIndex];
    if (!text || text.trim().length === 0) {
      chunkIndex++;
      playCloudChunk();
      return;
    }

    updateStatus('Loading audio ' + (chunkIndex + 1) + '/' + articleChunks.length + '...');

    /* Check cache first */
    if (cloudAudioCache[chunkIndex]) {
      playCachedChunk(chunkIndex);
      return;
    }

    /* Generate and play */
    isGenerating = true;
    requestCloudTTS(text, chunkIndex).then(function(url) {
      isGenerating = false;
      if (playing && !paused) {
        playCachedChunk(chunkIndex);
      }
      /* Pre-fetch next chunk */
      prefetchNextChunk();
    }).catch(function(err) {
      isGenerating = false;
      console.warn('Cloud TTS failed, falling back to browser TTS:', err);
      engine = 'browser';
      /* Re-chunk for browser (smaller chunks) */
      var fullText = articleChunks.join(' ');
      articleChunks = chunkTextForBrowser(fullText);
      /* Start from approximate position */
      chunkIndex = 0;
      speakChunk();
    });
  }

  function playCachedChunk(index) {
    if (!audioEl) {
      audioEl = new Audio();
      audioEl.addEventListener('ended', onChunkEnded);
      audioEl.addEventListener('error', onChunkError);
      audioEl.addEventListener('timeupdate', updateProgress);
    }

    audioEl.src = cloudAudioCache[index];
    audioEl.playbackRate = 1;  /* Speed is handled server-side for cloud TTS */

    audioEl.play().then(function() {
      updateStatus('Playing ' + (chunkIndex + 1) + '/' + articleChunks.length);
      startProgressTimer();
    }).catch(function(err) {
      console.warn('Audio play failed:', err);
      updateStatus('Playback error');
    });
  }

  function onChunkEnded() {
    stopProgressTimer();
    chunkIndex++;
    if (chunkIndex >= articleChunks.length) {
      onEnd();
    } else if (playing && !paused) {
      /* Small pause between chunks for natural sound */
      setTimeout(function() {
        if (playing && !paused) playCloudChunk();
      }, 250);
    }
  }

  function onChunkError(e) {
    console.warn('Audio chunk error:', e);
    updateStatus('Audio error, retrying...');
    /* Retry once */
    setTimeout(function() {
      if (playing && !paused) playCloudChunk();
    }, 1000);
  }

  function prefetchNextChunk() {
    var nextIdx = chunkIndex + 1;
    if (nextIdx < articleChunks.length && !cloudAudioCache[nextIdx] && !isGenerating) {
      requestCloudTTS(articleChunks[nextIdx], nextIdx).catch(function() {});
    }
  }

  /* ---- Progress Bar ---- */
  function startProgressTimer() {
    stopProgressTimer();
    progressTimer = setInterval(updateProgress, 250);
  }

  function stopProgressTimer() {
    if (progressTimer) {
      clearInterval(progressTimer);
      progressTimer = null;
    }
  }

  function updateProgress() {
    var bar = document.getElementById('audioProgressBar');
    var timeEl = document.getElementById('audioTime');
    if (!bar) return;

    var pct = 0;
    var currentSec = 0;
    var totalSec = 0;

    if (engine === 'cloud' && audioEl && audioEl.duration && isFinite(audioEl.duration)) {
      pct = (audioEl.currentTime / audioEl.duration) * 100;
      currentSec = Math.floor(audioEl.currentTime);
      totalSec = Math.floor(audioEl.duration);
      /* Add progress from previous chunks */
      var chunkProgress = (chunkIndex / articleChunks.length) * 100;
      var chunkRange = (1 / articleChunks.length) * 100;
      pct = chunkProgress + (pct / 100) * chunkRange;
    } else if (engine === 'browser' && articleChunks.length > 0) {
      pct = ((chunkIndex + 0.5) / articleChunks.length) * 100;
    }

    bar.style.width = Math.min(pct, 100) + '%';
    if (timeEl && totalSec > 0) {
      timeEl.textContent = formatTime(currentSec) + ' / ' + formatTime(totalSec);
    }
  }

  function formatTime(sec) {
    var m = Math.floor(sec / 60);
    var s = sec % 60;
    return m + ':' + (s < 10 ? '0' : '') + s;
  }

  /* ================================================================
     BROWSER TTS FALLBACK — Fixed Chrome 15s cutoff
     Uses small chunks (max ~450 chars = ~10s) so Chrome never cuts off
     ================================================================ */

  function selectBestVoice() {
    if (!synth) return null;
    var voices = synth.getVoices();
    if (!voices.length) return null;

    /* Priority 1: Natural / Enhanced / Neural */
    var v1 = voices.find(function(v) {
      return v.lang.startsWith('en') && (
        v.name.toLowerCase().indexOf('natural') !== -1 ||
        v.name.toLowerCase().indexOf('enhanced') !== -1 ||
        v.name.toLowerCase().indexOf('neural') !== -1
      );
    });
    if (v1) return v1;

    /* Priority 2: Microsoft high-quality */
    var v2 = voices.find(function(v) {
      return v.lang.startsWith('en') && v.name.indexOf('Microsoft') !== -1 &&
        (v.name.indexOf('Zira') !== -1 || v.name.indexOf('David') !== -1 ||
         v.name.indexOf('Mark') !== -1 || v.name.indexOf('Jenny') !== -1 ||
         v.name.indexOf('Aria') !== -1 || v.name.indexOf('Guy') !== -1);
    });
    if (v2) return v2;

    /* Priority 3: Google */
    var v3 = voices.find(function(v) {
      return v.lang.startsWith('en') && v.name.indexOf('Google') !== -1;
    });
    if (v3) return v3;

    /* Priority 4: en-US */
    var v4 = voices.find(function(v) { return v.lang === 'en-US'; });
    if (v4) return v4;

    /* Priority 5: Any English */
    var v5 = voices.find(function(v) { return v.lang.startsWith('en'); });
    if (v5) return v5;

    return voices[0];
  }

  function getVoice() {
    if (!cachedVoice || !voicesLoaded) cachedVoice = selectBestVoice();
    return cachedVoice;
  }

  /* ---- Browser TTS chunking — small chunks to avoid Chrome cutoff ---- */
  function chunkTextForBrowser(text) {
    /* Max 450 chars per chunk = ~10 seconds of speech (safely under Chrome's 15s limit) */
    var maxChunk = 450;
    var chunks = [];
    var sentences = text.match(/[^.!?\n]+[.!?\n]+/g) || [text];
    var current = '';

    for (var i = 0; i < sentences.length; i++) {
      var s = sentences[i].trim();
      if (!s) continue;
      if (current.length + s.length + 1 <= maxChunk) {
        current += (current ? ' ' : '') + s;
      } else {
        if (current) chunks.push(current);
        if (s.length > maxChunk) {
          /* Split long sentence by commas or semicolons */
          var parts = s.match(/[^,;:]+[,;:]+/g) || [s];
          var sub = '';
          for (var j = 0; j < parts.length; j++) {
            if (sub.length + parts[j].length <= maxChunk) {
              sub += parts[j];
            } else {
              if (sub) chunks.push(sub);
              sub = parts[j];
            }
          }
          current = sub;
        } else {
          current = s;
        }
      }
    }
    if (current) chunks.push(current);
    return chunks;
  }

  /* Cloud TTS chunking — bigger chunks OK (no Chrome limit) */
  function chunkTextForCloud(text) {
    var maxChunk = 900; /* Stay under 1000 API limit with margin */
    var chunks = [];
    var paragraphs = text.split(/\n\s*\n/);
    var current = '';

    for (var i = 0; i < paragraphs.length; i++) {
      var para = paragraphs[i].trim();
      if (!para) continue;
      if (current.length + para.length + 2 <= maxChunk) {
        current += (current ? ' ' : '') + para;
      } else {
        if (current) chunks.push(current);
        /* Split paragraph by sentences */
        var sentences = para.match(/[^.!?]+[.!?]+[\s]*/g) || [para];
        var sub = '';
        for (var j = 0; j < sentences.length; j++) {
          if (sub.length + sentences[j].length <= maxChunk) {
            sub += sentences[j];
          } else {
            if (sub) chunks.push(sub.trim());
            sub = sentences[j];
          }
        }
        current = sub;
      }
    }
    if (current) chunks.push(current);
    return chunks;
  }

  /* ---- Browser TTS speak (no keepalive needed — chunks too short) ---- */
  function speakChunk() {
    if (!playing || chunkIndex >= articleChunks.length) {
      onEnd();
      return;
    }

    var text = articleChunks[chunkIndex];
    if (!text || text.trim().length === 0) {
      chunkIndex++;
      speakChunk();
      return;
    }

    synth.cancel(); /* Clear any stuck utterances */

    currentUtterance = new SpeechSynthesisUtterance(text);
    currentUtterance.rate = speeds[speedIdx];
    currentUtterance.pitch = 1.05; /* Slightly higher pitch for clarity */

    var voice = getVoice();
    if (voice) currentUtterance.voice = voice;

    currentUtterance.onstart = function() {
      updateStatus('Playing ' + (chunkIndex + 1) + '/' + articleChunks.length);
      startProgressTimer();
    };

    currentUtterance.onend = function() {
      stopProgressTimer();
      chunkIndex++;
      updateProgress();
      if (playing && !paused) {
        /* Small gap between chunks for natural pacing */
        speakChunk();
      }
    };

    currentUtterance.onerror = function(e) {
      if (e.error !== 'canceled' && e.error !== 'interrupted') {
        console.warn('Speech error:', e.error);
        /* Skip to next chunk on error */
        chunkIndex++;
        if (playing && !paused) {
          setTimeout(speakChunk, 100);
        }
      }
    };

    synth.speak(currentUtterance);
    /* NO keepalive needed — each chunk is under 10 seconds */
  }

  /* ================================================================
     VOICE SELECTION DROPDOWN
     ================================================================ */

  function toggleVoiceMenu() {
    var dropdown = document.getElementById('audioVoiceDropdown');
    if (!dropdown) return;

    voiceMenuOpen = !voiceMenuOpen;
    dropdown.style.display = voiceMenuOpen ? 'block' : 'none';

    if (voiceMenuOpen && Object.keys(availableVoices).length === 0) {
      /* Voices not loaded yet, use defaults */
      availableVoices = {
        'en-US-AriaNeural': 'Aria (Female, US)',
        'en-US-JennyNeural': 'Jenny (Female, US)',
        'en-US-GuyNeural': 'Guy (Male, US)',
        'en-US-DavisNeural': 'Davis (Male, US)',
        'en-GB-SoniaNeural': 'Sonia (Female, UK)',
        'en-GB-RyanNeural': 'Ryan (Male, UK)'
      };
    }

    /* Populate dropdown */
    if (voiceMenuOpen && dropdown.children.length === 0) {
      var voiceKeys = Object.keys(availableVoices);
      for (var i = 0; i < voiceKeys.length; i++) {
        var key = voiceKeys[i];
        var item = document.createElement('div');
        item.className = 'audio-voice-item' + (key === selectedVoice ? ' active' : '');
        item.textContent = availableVoices[key];
        item.setAttribute('data-voice', key);
        item.addEventListener('click', function(e) {
          selectedVoice = this.getAttribute('data-voice');
          voiceMenuOpen = false;
          dropdown.style.display = 'none';
          /* Update voice button label */
          var voiceBtn = document.getElementById('audioVoiceBtn');
          if (voiceBtn) {
            voiceBtn.title = 'Voice: ' + availableVoices[selectedVoice];
          }
          /* Clear cache if we're switching voices mid-play */
          if (playing) {
            clearCloudCache();
          }
        });
        dropdown.appendChild(item);
      }
    }
  }

  /* Close voice menu when clicking outside */
  document.addEventListener('click', function(e) {
    if (voiceMenuOpen) {
      var voiceBtn = document.getElementById('audioVoiceBtn');
      var dropdown = document.getElementById('audioVoiceDropdown');
      if (voiceBtn && dropdown && !voiceBtn.contains(e.target) && !dropdown.contains(e.target)) {
        voiceMenuOpen = false;
        dropdown.style.display = 'none';
      }
    }
  });

  /* ================================================================
     PLAYER UI
     ================================================================ */

  function createPlayer() {
    var article = document.querySelector('.post-content');
    if (!article) return;

    var wrapper = document.createElement('div');
    wrapper.id = 'audio-player-wrap';
    wrapper.innerHTML =
      '<div class="audio-player" id="audioListenBtn">' +
        '<button class="audio-play-btn" aria-label="Listen to article">' +
          '<span class="audio-play-icon">' + ICONS.headphones + '</span>' +
        '</button>' +
        '<div class="audio-info">' +
          '<span class="audio-label">Listen</span>' +
          '<span class="audio-sublabel">Audio Article</span>' +
        '</div>' +
        '<div class="audio-wave">' +
          '<span></span><span></span><span></span><span></span>' +
        '</div>' +
      '</div>' +
      '<div class="audio-controls-bar" id="audioControls" style="display:none">' +
        '<button class="audio-ctrl-btn" id="audioPlayPause" title="Pause" aria-label="Pause">' +
          ICONS.pause +
        '</button>' +
        '<button class="audio-ctrl-btn" id="audioSkipBtn" title="Skip to next section" aria-label="Skip">' +
          ICONS.skip +
        '</button>' +
        '<button class="audio-ctrl-btn audio-speed-btn" id="audioSpeedBtn" title="Speed" aria-label="Speed">' +
          '<span class="speed-label">1x</span>' +
        '</button>' +
        (engine === 'cloud' ?
          '<button class="audio-ctrl-btn audio-voice-btn" id="audioVoiceBtn" title="Voice: Aria (Female, US)" aria-label="Select voice">' +
            ICONS.voice +
          '</button>' : '') +
        '<div class="audio-progress-wrap">' +
          '<div class="audio-progress-bar" id="audioProgressBar"></div>' +
        '</div>' +
        '<span class="audio-status" id="audioStatus">Preparing...</span>' +
        '<span class="audio-time" id="audioTime"></span>' +
        '<span class="audio-engine-badge" id="audioEngineBadge"></span>' +
        '<button class="audio-ctrl-btn audio-close-btn" id="audioCloseBtn" title="Close" aria-label="Close">' +
          ICONS.close +
        '</button>' +
      '</div>' +
      '<div class="audio-voice-dropdown" id="audioVoiceDropdown" style="display:none"></div>';

    article.parentNode.insertBefore(wrapper, article);

    document.getElementById('audioListenBtn').addEventListener('click', startAudio);
    document.getElementById('audioPlayPause').addEventListener('click', togglePlayPause);
    document.getElementById('audioSkipBtn').addEventListener('click', skipNextChunk);
    document.getElementById('audioSpeedBtn').addEventListener('click', cycleSpeed);
    document.getElementById('audioCloseBtn').addEventListener('click', stopAudio);

    var voiceBtn = document.getElementById('audioVoiceBtn');
    if (voiceBtn) voiceBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      toggleVoiceMenu();
    });

    document.addEventListener('keydown', function(e) {
      if (!playing) return;
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.code === 'Space') { e.preventDefault(); togglePlayPause(); }
      else if (e.code === 'Escape') { e.preventDefault(); stopAudio(); }
    });
  }

  /* ---- Extract clean article text ---- */
  function getArticleText() {
    var article = document.querySelector('.post-content');
    if (!article) return '';
    var clone = article.cloneNode(true);
    var remove = clone.querySelectorAll('script, style, iframe, noscript, #audio-player-wrap');
    remove.forEach(function(el) { el.remove(); });
    var text = clone.innerText || clone.textContent || '';
    /* Clean up: remove extra whitespace, special chars */
    text = text.replace(/\s+/g, ' ').trim();
    /* Remove common noise */
    text = text.replace(/\[.*?\]/g, ''); /* Remove [brackets] */
    text = text.replace(/READ MORE.*?(?=\.|$)/gi, '');
    return text;
  }

  /* ================================================================
     PLAYBACK CONTROLS
     ================================================================ */

  function startAudio() {
    /* Reset state */
    clearCloudCache();
    chunkIndex = 0;
    playing = true;
    paused = false;

    var text = getArticleText();
    if (!text || text.length < 10) {
      updateStatus('No article text found.');
      playing = false;
      return;
    }

    document.getElementById('audioControls').style.display = 'flex';
    document.getElementById('audioListenBtn').style.display = 'none';
    updatePlayPauseIcon();

    if (engine === 'cloud') {
      articleChunks = chunkTextForCloud(text);
      playCloudChunk();
    } else if (engine === 'browser') {
      articleChunks = chunkTextForBrowser(text);
      speakChunk();
    } else {
      updateStatus('Audio not available');
      playing = false;
    }

    /* Show engine badge */
    var badge = document.getElementById('audioEngineBadge');
    if (badge) {
      badge.textContent = engine === 'cloud' ? 'AI' : 'TTS';
      badge.title = engine === 'cloud' ? 'Professional AI Voice' : 'Browser Text-to-Speech';
    }
  }

  function togglePlayPause() {
    if (!playing) { startAudio(); return; }

    if (paused) {
      paused = false;
      if (engine === 'cloud' && audioEl) {
        audioEl.play();
      } else if (engine === 'browser' && synth) {
        synth.resume();
      }
      updateStatus('Playing ' + (chunkIndex + 1) + '/' + articleChunks.length);
      startProgressTimer();
    } else {
      paused = true;
      if (engine === 'cloud' && audioEl) {
        audioEl.pause();
      } else if (engine === 'browser' && synth) {
        synth.pause();
      }
      updateStatus('Paused');
      stopProgressTimer();
    }
    updatePlayPauseIcon();
  }

  function skipNextChunk() {
    if (!playing) return;

    if (engine === 'cloud') {
      if (audioEl) audioEl.pause();
      stopProgressTimer();
      chunkIndex++;
      if (chunkIndex >= articleChunks.length) {
        onEnd();
      } else {
        playCloudChunk();
      }
    } else {
      synth.cancel();
      stopProgressTimer();
      chunkIndex++;
      if (chunkIndex >= articleChunks.length) {
        onEnd();
      } else {
        speakChunk();
      }
    }
  }

  function cycleSpeed() {
    speedIdx = (speedIdx + 1) % speeds.length;
    var speed = speeds[speedIdx];
    var label = document.querySelector('.speed-label');
    if (label) label.textContent = speed + 'x';

    if (engine === 'cloud' && audioEl) {
      /* For cloud TTS, we need to regenerate audio at new speed.
         Changing playbackRate works but distorts quality.
         Best approach: re-generate current chunk at new speed. */
      clearCloudCache();
      if (playing && !paused) {
        playCloudChunk();
      }
    } else if (engine === 'browser' && playing && !paused && synth.speaking) {
      synth.cancel();
      stopProgressTimer();
      speakChunk(); /* Will use new speedIdx */
    }
  }

  function stopAudio() {
    if (engine === 'cloud' && audioEl) {
      audioEl.pause();
      audioEl.src = '';
    } else if (synth) {
      synth.cancel();
    }
    stopProgressTimer();
    playing = false;
    paused = false;
    currentUtterance = null;
    articleChunks = [];
    chunkIndex = 0;
    clearCloudCache();
    document.getElementById('audioControls').style.display = 'none';
    document.getElementById('audioListenBtn').style.display = 'inline-flex';
    var bar = document.getElementById('audioProgressBar');
    if (bar) bar.style.width = '0%';
  }

  function onEnd() {
    stopProgressTimer();
    playing = false;
    paused = false;
    updateStatus('Finished');
    updatePlayPauseIcon();
    var bar = document.getElementById('audioProgressBar');
    if (bar) bar.style.width = '100%';
    setTimeout(function() {
      document.getElementById('audioControls').style.display = 'none';
      document.getElementById('audioListenBtn').style.display = 'inline-flex';
      if (bar) bar.style.width = '0%';
    }, 2500);
  }

  /* ---- Helpers ---- */
  function updateStatus(text) {
    var el = document.getElementById('audioStatus');
    if (el) el.textContent = text;
  }

  function updatePlayPauseIcon() {
    var btn = document.getElementById('audioPlayPause');
    if (btn) {
      btn.innerHTML = paused ? ICONS.play : ICONS.pause;
      btn.title = paused ? 'Resume' : 'Pause';
      btn.setAttribute('aria-label', paused ? 'Resume' : 'Pause');
    }
  }

  function clearCloudCache() {
    Object.keys(cloudAudioCache).forEach(function(k) {
      URL.revokeObjectURL(cloudAudioCache[k]);
    });
    cloudAudioCache = {};
  }

  /* ---- Initialize ---- */
  function init() {
    /* First try cloud TTS, fall back to browser */
    detectCloudTTS().then(function() {
      console.log('[AudioPlayer] Engine:', engine, '| Voice:', selectedVoice);
      createPlayer();
    });
  }

  /* Load voices for browser fallback */
  if (synth) {
    var voices = synth.getVoices();
    if (voices.length) {
      voicesLoaded = true;
      cachedVoice = selectBestVoice();
    }
    if (synth.onvoiceschanged !== undefined) {
      synth.onvoiceschanged = function() {
        voicesLoaded = true;
        cachedVoice = selectBestVoice();
      };
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
