const BODY_COLOR = '#f4f8fb';
const BODY = document.querySelector('body');
const trashIcon = document.querySelector('.trash-icon');

BODY.addEventListener('click', (e) => {
    if (e.target !== BODY) {
        return;
    }
    const messages = document.querySelectorAll('.message-container');

    for (const message of messages) {
        if (message.classList.contains('expanded-message-container')) {
            message.classList.remove('expanded-message-container');
            message.querySelector('p').classList.remove('expanded-message-text');
            message.querySelector('.expand-icon').classList.remove('expanded-expand-icon');
            message.querySelector('p').classList.add('message-text');
        }
    }
    BODY.style.backgroundColor = BODY_COLOR;
    trashIcon.style.display = "block";
});

function onExpandClick(e) {
    e.stopPropagation();

    const messageContainer = e.target.parentElement;
    const message = messageContainer.querySelector('p');
    const expandIcon = messageContainer.querySelector('.expand-icon')
    trashIcon.style.display = "none";

    if (messageContainer.classList.contains('expanded-message-container')) {
        messageContainer.classList.remove('expanded-message-container');
        message.classList.remove('expanded-message-text');
        expandIcon.classList.remove('expanded-expand-icon');
        
        message.classList.add('message-text');
        
        document.querySelector('body').style.backgroundColor = BODY_COLOR;
        trashIcon.style.display = "block";
        return;
    }

    // close other expanded messages
    const expandedMessages = document.querySelectorAll('.message-container');

    for (const message of expandedMessages) {
        message.classList.remove('expanded-message-container');
        message.querySelector('p').classList.remove('expanded-message-text');
        message.querySelector('.expand-icon').classList.remove('expanded-expand-icon');

        message.querySelector('p').classList.add('message-text');
    }


    messageContainer.classList.add('expanded-message-container');
    message.classList.add('expanded-message-text');
    message.classList.remove('message-text');
    expandIcon.classList.add('expanded-expand-icon');

    // make body bg color gray
    document.querySelector('body').style.backgroundColor = '#ccc';
}