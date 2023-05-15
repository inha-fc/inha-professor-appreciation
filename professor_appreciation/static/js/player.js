var audio = document.getElementById('audio-player');
var progressBar = document.getElementById('audio-progress-bar');
var toggleButton = document.getElementById('toggle-button');

audio.addEventListener('timeupdate', function() {
    var currentTime = audio.currentTime;
    var duration = audio.duration;
    var progress = (currentTime / duration) * 100;
    progressBar.style.width = progress + '%';
});

toggleButton.addEventListener('click', function() {
    if (audio.paused) {
        audio.play();
        toggleButton.innerHTML = '<i class="fas fa-pause"></i>';
    }
});