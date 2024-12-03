document.addEventListener("DOMContentLoaded", function() {
    // Get the messages from the data attribute in the HTML
    const messagesElement = document.getElementById('django-messages');
    const messages = messagesElement ? messagesElement.getAttribute('data-messages').split(' | ') : [];

    // Check if there are any error messages
    if (messages.length > 0 && messages[0]) {
        messages.forEach(function(message) {
            showErrorModal(message);
        });
    }

    // Function to show error modal with a specific message
    function showErrorModal(message) {
        const errorModal = document.getElementById('errorModal');
        const errorMessage = document.getElementById('errorMessage');
        errorMessage.innerText = message;
        errorModal.style.display = 'block';
    }

    // Close modal when clicking the close button
    document.querySelector('.close-btn').onclick = function() {
        document.getElementById('errorModal').style.display = 'none';
    };

    // Close modal if clicking outside of it
    window.onclick = function(event) {
        if (event.target == document.getElementById('errorModal')) {
            document.getElementById('errorModal').style.display = 'none';
        }
    };
});