const form = document.getElementById('chat-form');
const responseBox = document.getElementById('response-box');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = document.getElementById('message').value;
    const personality = document.getElementById('personality').value;

    const res = await fetch('/chat', {
        method: 'POST',
        body: new URLSearchParams({
            message: message,
            personality: personality
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    });
    const data = await res.json();
    responseBox.innerHTML = `<p><b>AI:</b> ${data.response}</p>`;
    form.reset();
});
