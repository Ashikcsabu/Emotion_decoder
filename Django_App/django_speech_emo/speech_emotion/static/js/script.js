document.addEventListener('DOMContentLoaded', function () {
    const video = document.getElementById('emo-video');
    const emotionAnimations = {
        'angry': document.getElementById('angry'),
        'disgust': document.getElementById('disgust'),
        'fear': document.getElementById('fear'),
        'happy': document.getElementById('happy'),
        'neutral': document.getElementById('neutral'),
        'sad': document.getElementById('sad'),
        'surprise': document.getElementById('surprise'),
    };

    // Update emotions every time the video time updates
    video.addEventListener('timeupdate', function () {
        const currentTime = video.currentTime;
        const currentKey = Object.keys(emotionData).find(key => {
            const [start, end] = key.split(':').map(Number);
            return currentTime >= start && currentTime < end;
        });
        if (currentKey) {
            const currentEmotion = emotionData[currentKey];
            updateEmotionAnimations(currentEmotion);
        }
    });

    // Function to update emotion animations
    function updateEmotionAnimations(emotion) {
        Object.keys(emotionAnimations).forEach(key => {
            const spans = emotionAnimations[key].querySelectorAll('span');
            spans.forEach(span => {
                if (key === emotion) {
                    // Clear the animation corresponding to the detected emotion
                    span.style.filter = 'none';
                } else {
                    // Blur all other animations
                    span.style.filter = 'blur(10px)';
                }
            });
        });
    }
});

    // Reference to the file input and label
    const fileInput = document.getElementById('file');
    const fileLabel = document.getElementById('fileLabel');
    const uploadForm = document.getElementById('uploadForm');
    const submitButton = uploadForm.querySelector('button[type="submit"]');

    // Change label text to "Done" when a file is selected
    fileInput.addEventListener('change', function () {
        if (fileInput.files.length > 0) {
            fileLabel.textContent = 'Ʉ₱ⱠØ₳ĐɆĐ';
        }
    });

    // Change the "Decode" button text to "Processing..." on form submission
    uploadForm.addEventListener('submit', function () {
        submitButton.textContent = '₱ⱤØ₵Ɇ₴₴ł₦₲...';
    });



