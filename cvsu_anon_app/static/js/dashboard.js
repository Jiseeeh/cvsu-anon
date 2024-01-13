const BODY_COLOR = '#f4f8fb';
const BODY = document.querySelector('body');


BODY.addEventListener('click', (e) => {
    if (e.target !== BODY) {
        return;
    }

    const trashIcon = document.querySelector('.trash-icon');
    const messages = document.querySelectorAll('.message-container');

    for (const message of messages) {
        if (message.classList.contains('expanded-message-container')) {
            const messageText = message.querySelector('textarea') ?? message.querySelector('p');
            const receiver = message.querySelector('.receiver');
            const saveIcon = message.querySelector('.save-icon');

            message.classList.remove('expanded-message-container');
            messageText.classList.remove('expanded-message-text');
            message.querySelector('.expand-icon').classList.remove('expanded-expand-icon');
            if (saveIcon) saveIcon.classList.remove('expanded-save-icon');
            if (receiver) receiver.classList.remove('expanded-receiver');
            messageText.classList.add('message-text');
        }
    }
    BODY.style.backgroundColor = BODY_COLOR;
    if (trashIcon) trashIcon.style.display = "block";
});

function onExpandClick(e,isOnTextArea=false) {
    e.stopPropagation();

    const tag = isOnTextArea ? 'textarea' : 'p';
    const messageContainer = e.target.parentElement;
    const trashIcon = messageContainer.querySelector('.trash-icon')
    const message = messageContainer.querySelector(tag);
    const expandIcon = messageContainer.querySelector('.expand-icon');
    const saveIcon = messageContainer.querySelector('.save-icon');
    const receiver = messageContainer.querySelector('.receiver');
    if (trashIcon) trashIcon.style.display = "none";

    if (messageContainer.classList.contains('expanded-message-container')) {
        messageContainer.classList.remove('expanded-message-container');
        message.classList.remove('expanded-message-text');
        expandIcon.classList.remove('expanded-expand-icon');
        if (saveIcon) saveIcon.classList.remove('expanded-save-icon');
        if (receiver) receiver.classList.remove('expanded-receiver');
        
        message.classList.add('message-text');
        
        document.querySelector('body').style.backgroundColor = BODY_COLOR;
        if (trashIcon) trashIcon.style.display = "block";
        return;
    }

    // close other expanded messages
    const expandedMessages = document.querySelectorAll('.message-container');

    for (const message of expandedMessages) {
        message.classList.remove('expanded-message-container');
        message.querySelector(tag).classList.remove('expanded-message-text');
        message.querySelector('.expand-icon').classList.remove('expanded-expand-icon');

        message.querySelector(tag).classList.add('message-text');
    }


    messageContainer.classList.add('expanded-message-container');
    message.classList.add('expanded-message-text');
    message.classList.remove('message-text');
    expandIcon.classList.add('expanded-expand-icon');
    if (saveIcon) saveIcon.classList.add('expanded-save-icon');
    if (receiver) receiver.classList.add('expanded-receiver');

    // make body bg color gray
    document.querySelector('body').style.backgroundColor = '#ccc';
}

function onSaveClick(e) {
    e.stopPropagation();

    const messageContainer = e.target.parentElement;
    const message = messageContainer.querySelector('textarea');
    
    fetch(`http://127.0.0.1:8000/patch_message/${e.target.dataset.id}/`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')  // Don't forget to include CSRF token
        },
        body: JSON.stringify({ message: message.value })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("Message updated successfully!");
        } else {
            alert("Something went wrong. Please try again later.");
        }
    })

}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if this cookie contains the name we are looking for
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}