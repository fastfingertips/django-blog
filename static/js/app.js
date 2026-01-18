
// Auto-dismiss alerts after 3 seconds
document.addEventListener("DOMContentLoaded", function () {
    // Alert Logic
    setTimeout(function () {
        let alerts = document.querySelectorAll(".alert");
        alerts.forEach(function (alert) {
            alert.style.transition = "opacity 0.5s ease";
            alert.style.opacity = "0";
            setTimeout(function () {
                alert.remove();
            }, 500);
        });
    }, 3000);

    // Reply Button Logic
    const replyButtons = document.querySelectorAll('.reply-btn');
    const commentInput = document.querySelector('textarea[name="comment_content"]');

    if (commentInput) {
        replyButtons.forEach(btn => {
            btn.addEventListener('click', function (e) {
                e.preventDefault();
                const username = this.getAttribute('data-username');

                // Focus input
                commentInput.focus();

                // Append @username to the current value
                const mention = `@${username} `;

                // If input is empty, just add mention
                if (commentInput.value.trim() === "") {
                    commentInput.value = mention;
                } else {
                    // If not empty, append with a newline or space
                    commentInput.value += `\n${mention}`;
                }

                // Scroll smoothly to input
                commentInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
            });
        });
    }
});
