
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
    const parentIdInput = document.querySelector('#parent_id');
    const replyingToLabel = document.querySelector('#replying-to');
    const replyUsernameSpan = document.querySelector('#reply-username');
    const cancelReplyBtn = document.querySelector('#cancel-reply');

    if (commentInput) {
        replyButtons.forEach(btn => {
            btn.addEventListener('click', function (e) {
                e.preventDefault();
                const username = this.getAttribute('data-username');
                const commentId = this.getAttribute('data-comment-id');

                // Set parent ID
                parentIdInput.value = commentId;

                // Show replying UI
                replyUsernameSpan.textContent = `@${username}`;
                replyingToLabel.classList.remove('d-none');

                // Focus input
                commentInput.focus();
                commentInput.placeholder = `Reply to @${username}...`;

                // Scroll smoothly to input
                commentInput.scrollIntoView({ behavior: 'smooth', block: 'center' });
            });
        });

        if (cancelReplyBtn) {
            cancelReplyBtn.addEventListener('click', function () {
                // Clear state
                parentIdInput.value = '';
                replyingToLabel.classList.add('d-none');
                commentInput.value = '';
                commentInput.placeholder = 'leave a note...';
            });
        }
    }

    // Toggle Replies Logic
    const toggleButtons = document.querySelectorAll('.toggle-replies-btn');
    toggleButtons.forEach(btn => {
        btn.addEventListener('click', function () {
            const targetId = this.getAttribute('data-bs-target');
            const targetElement = document.querySelector(targetId);

            if (targetElement.classList.contains('d-none')) {
                // Show
                targetElement.classList.remove('d-none');
                this.innerHTML = '&#x25B2; hide replies';
            } else {
                // Hide
                targetElement.classList.add('d-none');
                const count = this.getAttribute('data-count') || '';
                // We'll need to store count if we want to restore it perfectly or just generic
                // For simplicity, let's just restore original text logic or simpler
                // A smarter way is to grab the original text but let's stick to simple for now. 
                // Let's improve the button to store count.
                const countInitial = this.innerHTML.replace('▼ show ', '').replace(' replies', '').trim();
                // Actually easier: just toggle text
                if (this.innerHTML.includes('show')) {
                    // logic handled above
                } else {
                    // logic handled above
                }
            }
        });
    });

    // Better Toggle Logic
    document.body.addEventListener('click', function (e) {
        if (e.target.classList.contains('toggle-replies-btn')) {
            const btn = e.target;
            const targetId = btn.getAttribute('data-bs-target');
            const targetElement = document.querySelector(targetId);

            if (targetElement.classList.contains('d-none')) {
                targetElement.classList.remove('d-none');
                btn.innerHTML = btn.innerHTML.replace('▼', '▲').replace('show', 'hide');
            } else {
                targetElement.classList.add('d-none');
                btn.innerHTML = btn.innerHTML.replace('▲', '▼').replace('hide', 'show');
            }
        }
    });
});
