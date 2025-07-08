//websockets
document.addEventListener('DOMContentLoaded', () => {
    const socket = new WebSocket(`wss://${window.location.host}/ws/edit/${docId}/`);
    const page = document.querySelector('.page');

    let isUpdating = false;
    let isTyping = false;

    page.addEventListener('input', () => {
      isTyping = true;
      if (isUpdating) return;
      socket.send(JSON.stringify({ message: page.value }));

      clearTimeout(typingTimer);
      typingTimer = setTimeout(() => {
        isTyping = false;
    }, 500);
    });



    socket.onmessage = function (e) {
        if (isUpdating) return;

      const data = JSON.parse(e.data);
      if (data.message !== page.value) {
        isUpdating = true;
        page.value = data.message;
        isUpdating = false;
      }
    };

    // Save title via AJAX POST
    const titleInput = document.getElementById("doc-title");
    const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

    titleInput.addEventListener('blur', () => {
      const newTitle = titleInput.value;

      fetch(`/update-title/${docId}/`, {
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({ title: newTitle })
      }).then(response => {
        if (!response.ok) {
          alert("Failed to save title");
        }
      });
    });
    setInterval(() => {
  autosaveContent();
}, 5000);  // every 5 seconds saves actual content of the docs

    //autosave!
    function autosaveContent() {
  const content = document.querySelector('.page').value;
  const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

  fetch(`/update-content/${docId}/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken
    },
    body: JSON.stringify({ content })
  }).then(response => {
    if (!response.ok) {
      console.error("Autosave failed.");
    }
    if (response.ok) {
    document.getElementById("save-status").textContent = "✅ Saved";
  }
  });
}
    window.shareDoc = function() {
    const username = document.getElementById("share-username").value;

  fetch(`/share/${docId}/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken
    },
    body: JSON.stringify({ username: username })
  })
  .then(res => res.json())
  .then(data => {
    if (data.status === 'shared') {
      alert("✅ Document shared!");
    } else {
      alert("❌ " + data.message);
    }
  });
}
});