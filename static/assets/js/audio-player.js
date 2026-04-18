(function() {
  'use strict';
  if (!window.speechSynthesis) return;

  var synth = window.speechSynthesis;
  var utterance = null;
  var playing = false;
  var paused = false;
  var speeds = [0.75, 1, 1.25, 1.5];
  var speedIdx = 1;

  function createPlayer() {
    var article = document.querySelector('.post-content');
    if (!article) return;

    var wrapper = document.createElement('div');
    wrapper.id = 'audio-player-wrap';
    wrapper.innerHTML =
      '<div class="audio-player-bar" id="audioPlayerBar">' +
        '<button class="audio-btn audio-listen-btn" id="audioListenBtn" title="Listen to article">' +
          '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>' +
          '<span>Listen</span>' +
        '</button>' +
        '<div class="audio-controls" id="audioControls" style="display:none">' +
          '<button class="audio-btn" id="audioPlayPause" title="Play/Pause">' +
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" id="audioPPIcon"><polygon points="5 3 19 12 5 21 5 3"/></svg>' +
          '</button>' +
          '<button class="audio-btn audio-speed-btn" id="audioSpeedBtn" title="Speed">1x</button>' +
          '<button class="audio-btn" id="audioStopBtn" title="Stop">' +
            '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/></svg>' +
          '</button>' +
          '<span class="audio-status" id="audioStatus">Playing...</span>' +
        '</div>' +
      '</div>';

    article.parentNode.insertBefore(wrapper, article.nextSibling);

    document.getElementById('audioListenBtn').addEventListener('click', startAudio);
    document.getElementById('audioPlayPause').addEventListener('click', togglePlayPause);
    document.getElementById('audioSpeedBtn').addEventListener('click', cycleSpeed);
    document.getElementById('audioStopBtn').addEventListener('click', stopAudio);

    utterance = new SpeechSynthesisUtterance();
    utterance.addEventListener('end', onEnd);
  }

  function startAudio() {
    var text = document.querySelector('.post-content').innerText.substring(0, 15000);
    utterance.text = text;
    utterance.rate = speeds[speedIdx];
    utterance.pitch = 1;
    synth.speak(utterance);
    playing = true;
    paused = false;
    document.getElementById('audioControls').style.display = 'flex';
    document.getElementById('audioStatus').textContent = 'Playing...';
  }

  function togglePlayPause() {
    if (paused) {
      synth.resume();
      paused = false;
      document.getElementById('audioStatus').textContent = 'Playing...';
    } else {
      synth.pause();
      paused = true;
      document.getElementById('audioStatus').textContent = 'Paused';
    }
  }

  function cycleSpeed() {
    speedIdx = (speedIdx + 1) % speeds.length;
    utterance.rate = speeds[speedIdx];
    document.getElementById('audioSpeedBtn').textContent = speeds[speedIdx] + 'x';
  }

  function stopAudio() {
    synth.cancel();
    playing = false;
    paused = false;
    document.getElementById('audioControls').style.display = 'none';
  }

  function onEnd() {
    playing = false;
    paused = false;
    document.getElementById('audioControls').style.display = 'none';
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createPlayer);
  } else {
    createPlayer();
  }
})();
