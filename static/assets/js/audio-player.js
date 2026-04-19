/* ================================================================
   Audio Player — Text-to-Speech for Article Pages
   MenshlyGlobal Client-Side Logic v2.0
   - Modern headphone icon (Feather-based)
   - Smart voice selection (natural/enhanced voices preferred)
   - Intelligent text chunking (sentence-boundary aware)
   - Chrome keepalive workaround (pause/resume ping)
   - Pulse animation while speaking
   - Clean CSS class-based styling
   ================================================================ */
(function() {
  'use strict';
  if (!window.speechSynthesis) return;

  var synth = window.speechSynthesis;
  var playing = false;
  var paused = false;
  var speeds = [0.75, 1, 1.25, 1.5, 2];
  var speedIdx = 1;
  var currentUtterance = null;
  var articleChunks = [];
  var chunkIndex = 0;
  var keepaliveTimer = null;
  var voicesLoaded = false;
  var cachedVoice = null;

  /* ---- Modern SVG Icons (Feather-style, consistent stroke) ---- */
  var ICONS = {
    headphones:
      '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' +
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
    stop:
      '<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none">' +
        '<rect x="4" y="4" width="16" height="16" rx="2"/>' +
      '</svg>',
    skip:
      '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
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
      '</svg>'
  };

  /* ---- Smart Voice Selection ---- */
  function selectBestVoice() {
    var voices = synth.getVoices();
    if (!voices.length) return null;

    // Priority 1: Natural / Enhanced voices (Siri, Microsoft Natural, etc.)
    var naturalVoice = voices.find(function(v) {
      return v.lang.startsWith('en') && (
        v.name.toLowerCase().indexOf('natural') !== -1 ||
        v.name.toLowerCase().indexOf('enhanced') !== -1 ||
        v.name.toLowerCase().indexOf('neural') !== -1
      );
    });
    if (naturalVoice) return naturalVoice;

    // Priority 2: Microsoft Edge / Windows voices (generally high quality)
    var msVoice = voices.find(function(v) {
      return v.lang.startsWith('en') && (
        v.name.indexOf('Microsoft') !== -1 &&
        (v.name.indexOf('Zira') !== -1 || v.name.indexOf('David') !== -1 || v.name.indexOf('Mark') !== -1 || v.name.indexOf('Jenny') !== -1)
      );
    });
    if (msVoice) return msVoice;

    // Priority 3: Google voices (Chrome default but decent)
    var googleVoice = voices.find(function(v) {
      return v.lang.startsWith('en') && v.name.indexOf('Google') !== -1;
    });
    if (googleVoice) return googleVoice;

    // Priority 4: Any en-US voice
    var enUsVoice = voices.find(function(v) {
      return v.lang === 'en-US';
    });
    if (enUsVoice) return enUsVoice;

    // Priority 5: Any English voice
    var enVoice = voices.find(function(v) {
      return v.lang.startsWith('en');
    });
    if (enVoice) return enVoice;

    // Fallback: first available
    return voices[0];
  }

  function getVoice() {
    if (!cachedVoice || !voicesLoaded) {
      cachedVoice = selectBestVoice();
    }
    return cachedVoice;
  }

  /* ---- Intelligent Text Chunking ---- */
  function chunkText(text, maxChunkSize) {
    maxChunkSize = maxChunkSize || 2800;
    var chunks = [];

    // First split by paragraphs (double newlines)
    var paragraphs = text.split(/\n\s*\n/);
    var currentChunk = '';

    for (var i = 0; i < paragraphs.length; i++) {
      var para = paragraphs[i].trim();
      if (!para) continue;

      if (currentChunk.length + para.length + 2 <= maxChunkSize) {
        currentChunk += (currentChunk ? ' ' : '') + para;
      } else {
        if (currentChunk) chunks.push(currentChunk);

        // If single paragraph exceeds max, split by sentences
        if (para.length > maxChunkSize) {
          var sentenceChunks = splitBySentences(para, maxChunkSize);
          for (var j = 0; j < sentenceChunks.length; j++) {
            chunks.push(sentenceChunks[j]);
          }
          currentChunk = '';
        } else {
          currentChunk = para;
        }
      }
    }

    if (currentChunk) chunks.push(currentChunk);
    return chunks;
  }

  function splitBySentences(text, maxSize) {
    var chunks = [];
    var sentences = text.match(/[^.!?]+[.!?]+[\s]*/g) || [text];
    var current = '';

    for (var i = 0; i < sentences.length; i++) {
      var sentence = sentences[i];
      if (current.length + sentence.length <= maxSize) {
        current += sentence;
      } else {
        if (current) chunks.push(current.trim());
        // If single sentence is too long, hard-split
        if (sentence.length > maxSize) {
          var words = sentence.split(/\s+/);
          var wordChunk = '';
          for (var w = 0; w < words.length; w++) {
            if (wordChunk.length + words[w].length + 1 <= maxSize) {
              wordChunk += (wordChunk ? ' ' : '') + words[w];
            } else {
              if (wordChunk) chunks.push(wordChunk.trim());
              wordChunk = words[w];
            }
          }
          current = wordChunk;
        } else {
          current = sentence;
        }
      }
    }

    if (current) chunks.push(current.trim());
    return chunks;
  }

  /* ---- Create Player UI ---- */
  function createPlayer() {
    var article = document.querySelector('.post-content');
    if (!article) return;

    var wrapper = document.createElement('div');
    wrapper.id = 'audio-player-wrap';
    wrapper.innerHTML =
      '<button class="audio-listen-btn" id="audioListenBtn" title="Listen to this article">' +
        '<span class="audio-listen-icon">' + ICONS.headphones + '</span>' +
        '<span class="audio-listen-text">Listen to Article</span>' +
      '</button>' +
      '<div class="audio-controls" id="audioControls" style="display:none">' +
        '<button class="audio-ctrl-btn" id="audioPlayPause" title="Play/Pause">' +
          ICONS.pause +
        '</button>' +
        '<button class="audio-ctrl-btn" id="audioStopBtn" title="Stop">' +
          ICONS.stop +
        '</button>' +
        '<button class="audio-ctrl-btn audio-speed-btn" id="audioSpeedBtn" title="Playback speed">' +
          '<span class="speed-label">1x</span>' +
        '</button>' +
        '<span class="audio-status" id="audioStatus">Preparing...</span>' +
        '<button class="audio-ctrl-btn audio-close-btn" id="audioCloseBtn" title="Close player">' +
          ICONS.close +
        '</button>' +
      '</div>';

    article.parentNode.insertBefore(wrapper, article);

    document.getElementById('audioListenBtn').addEventListener('click', startAudio);
    document.getElementById('audioPlayPause').addEventListener('click', togglePlayPause);
    document.getElementById('audioSpeedBtn').addEventListener('click', cycleSpeed);
    document.getElementById('audioStopBtn').addEventListener('click', stopAudio);
    document.getElementById('audioCloseBtn').addEventListener('click', stopAudio);
  }

  /* ---- Extract clean article text ---- */
  function getArticleText() {
    var article = document.querySelector('.post-content');
    if (!article) return '';
    var clone = article.cloneNode(true);
    var remove = clone.querySelectorAll('script, style, .audio-player-bar, iframe, noscript, .audio-controls, #audio-player-wrap');
    remove.forEach(function(el) { el.remove(); });
    var text = clone.innerText || clone.textContent || '';
    text = text.replace(/\s+/g, ' ').trim();
    return text;
  }

  /* ---- Chrome Keepalive Workaround ---- */
  function startKeepalive() {
    stopKeepalive();
    // Chrome pauses speech synthesis after ~15 seconds of continuous speaking.
    // This workaround pauses and immediately resumes every 10 seconds to reset the timer.
    keepaliveTimer = setInterval(function() {
      if (synth.speaking && !synth.paused && playing && !paused) {
        synth.pause();
        setTimeout(function() {
          if (playing && !paused) {
            synth.resume();
          }
        }, 50);
      }
    }, 10000);
  }

  function stopKeepalive() {
    if (keepaliveTimer) {
      clearInterval(keepaliveTimer);
      keepaliveTimer = null;
    }
  }

  /* ---- Pulse Animation Control ---- */
  function setPlayingState(isSpeaking) {
    var listenBtn = document.getElementById('audioListenBtn');
    if (listenBtn) {
      if (isSpeaking) {
        listenBtn.classList.add('audio-speaking');
      } else {
        listenBtn.classList.remove('audio-speaking');
      }
    }
  }

  /* ---- Start Audio Playback ---- */
  function startAudio() {
    synth.cancel();

    var text = getArticleText();
    if (!text || text.length < 10) {
      updateStatus('No article text found.');
      return;
    }

    // Intelligent chunking
    articleChunks = chunkText(text, 2800);
    chunkIndex = 0;
    playing = true;
    paused = false;

    document.getElementById('audioControls').style.display = 'flex';
    document.getElementById('audioListenBtn').style.display = 'none';
    updatePlayPauseIcon();
    setPlayingState(true);
    speakChunk();
  }

  /* ---- Speak Current Chunk ---- */
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

    currentUtterance = new SpeechSynthesisUtterance(text);
    currentUtterance.rate = speeds[speedIdx];
    currentUtterance.pitch = 1;

    // Smart voice selection
    var voice = getVoice();
    if (voice) currentUtterance.voice = voice;

    currentUtterance.onend = function() {
      chunkIndex++;
      updateStatus('Playing (' + Math.min(chunkIndex, articleChunks.length) + '/' + articleChunks.length + ')');
      // Small delay before next chunk to prevent glitches
      setTimeout(function() {
        if (playing && !paused) speakChunk();
      }, 80);
    };

    currentUtterance.onerror = function(e) {
      if (e.error !== 'canceled' && e.error !== 'interrupted') {
        updateStatus('Error: ' + e.error);
      }
    };

    synth.speak(currentUtterance);
    updateStatus('Playing (' + (chunkIndex + 1) + '/' + articleChunks.length + ')');
    startKeepalive();
  }

  /* ---- Play / Pause Toggle ---- */
  function togglePlayPause() {
    if (!playing) {
      startAudio();
      return;
    }

    if (paused) {
      synth.resume();
      paused = false;
      updateStatus('Playing (' + (chunkIndex + 1) + '/' + articleChunks.length + ')');
      startKeepalive();
    } else {
      synth.pause();
      paused = true;
      updateStatus('Paused');
      stopKeepalive();
    }
    updatePlayPauseIcon();
  }

  /* ---- Cycle Playback Speed ---- */
  function cycleSpeed() {
    speedIdx = (speedIdx + 1) % speeds.length;
    var speed = speeds[speedIdx];
    var label = document.querySelector('.speed-label');
    if (label) label.textContent = speed + 'x';

    // If currently speaking, restart with new speed
    if (playing && !paused && synth.speaking) {
      synth.cancel();
      stopKeepalive();
      speakChunk();
    } else if (currentUtterance) {
      currentUtterance.rate = speed;
    }
  }

  /* ---- Stop Audio ---- */
  function stopAudio() {
    synth.cancel();
    playing = false;
    paused = false;
    stopKeepalive();
    document.getElementById('audioControls').style.display = 'none';
    document.getElementById('audioListenBtn').style.display = 'inline-flex';
    setPlayingState(false);
    currentUtterance = null;
    articleChunks = [];
    chunkIndex = 0;
  }

  /* ---- Playback Finished ---- */
  function onEnd() {
    playing = false;
    paused = false;
    stopKeepalive();
    setPlayingState(false);
    updateStatus('Finished');
    updatePlayPauseIcon();
    setTimeout(function() {
      document.getElementById('audioControls').style.display = 'none';
      document.getElementById('audioListenBtn').style.display = 'inline-flex';
    }, 2000);
  }

  /* ---- UI Helpers ---- */
  function updateStatus(text) {
    var el = document.getElementById('audioStatus');
    if (el) el.textContent = text;
  }

  function updatePlayPauseIcon() {
    var btn = document.getElementById('audioPlayPause');
    if (btn) {
      btn.innerHTML = paused ? ICONS.play : ICONS.pause;
      btn.title = paused ? 'Resume' : 'Pause';
    }
  }

  /* ---- Voices Loading (async on some browsers) ---- */
  function ensureVoices() {
    var voices = synth.getVoices();
    if (voices.length) {
      voicesLoaded = true;
      cachedVoice = selectBestVoice();
    }
  }

  if (synth.onvoiceschanged !== undefined) {
    synth.onvoiceschanged = function() {
      voicesLoaded = true;
      cachedVoice = selectBestVoice();
    };
  }
  // Try to load voices immediately (some browsers have them ready)
  ensureVoices();

  /* ---- Initialize ---- */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createPlayer);
  } else {
    createPlayer();
  }
})();
