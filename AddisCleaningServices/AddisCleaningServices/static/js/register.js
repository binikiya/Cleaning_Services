const usernameField = document.querySelector('#nameField');
const addressField = document.querySelector('#addressField');
const emailField = document.querySelector('#emailField');
const phoneField = document.querySelector('#phoneField');

const phoneFeedbackArea = document.querySelector('.phoneFeedbackArea');
const emailFeedbackArea = document.querySelector('.emailFeedbackArea');
const addressFeedbackArea = document.querySelector('.addressFeedbackArea');
const feedBackField = document.querySelector('.invalid_feedback');

const submitBtn = document.querySelector('.submitBtn');

const nameField1 = document.querySelector('#nameField1');
const messageField1 = document.querySelector('#messageField');
const emailField1 = document.querySelector('#emailField1');
const phoneField1 = document.querySelector('#phoneField1');

const submitbtn = document.querySelector('.submit-btn');

phoneField.addEventListener("keyup", (e) => {
    const phoneVal = e.target.value;

    phoneField.classList.remove('is-invalid');
    phoneFeedbackArea.style.display = "none";

    if (phoneVal.length > 0) {
        fetch("/validate-phone", {
            body: JSON.stringify({ phone: phoneVal }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            if (data.phone_error) {
                phoneField.classList.add('is-invalid');
                submitBtn.disabled = true;
            }
            else {
                submitBtn.removeAttribute("disabled");
            }
        });
    }
});

emailField.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;

    emailField.classList.remove('is-invalid');
    emailFeedbackArea.style.display = "none";

    if (emailVal.length > 0) {
        fetch("/validate-email", {
            body: JSON.stringify({ email: emailVal }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            if (data.email_error) {
                emailField.classList.add('is-invalid');
                submitBtn.disabled = true;
            }
            else {
                submitBtn.removeAttribute("disabled");
            }
        });
    }
});

addressField.addEventListener("keyup", (e) => {
    const addressVal = e.target.value;

    addressField.classList.remove('is-invalid');
    addressFeedbackArea.style.display = "none";

    if (addressVal.length > 0) {
        fetch("/validate-address", {
            body: JSON.stringify({ address: addressVal }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            if (data.address_error) {
                addressField.classList.add('is-invalid');
                submitBtn.disabled = true;
            }
            else {
                submitBtn.removeAttribute("disabled");
            }
        });
    }
});

usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;

    usernameField.classList.remove('is-invalid');
    feedBackField.style.display = "none";

    if (usernameVal.length > 0) {
        fetch("/validate-username", {
            body: JSON.stringify({ name: usernameVal}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            if (data.username_error) {
                usernameField.classList.add('is-invalid');
                /* feedbackField.style.display = "block";
                feedbackField.innerHTML = `<p>${data.username_error}`;*/
                submitBtn.disabled = true;
            }
            else {
                submitBtn.removeAttribute("disabled");
            }
        });
    }
});

/* comment section */
phoneField1.addEventListener("keyup", (e) => {
    const phoneVal = e.target.value;

    phoneField1.classList.remove('is-invalid');

    if (phoneVal.length > 0) {
        fetch("/validate-phone-one", {
            body: JSON.stringify({ phone1: phoneVal }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            if (data.phone_error) {
                phoneField1.classList.add('is-invalid');
                submitbtn.disabled = true;
            }
            else {
                submitbtn.removeAttribute("disabled");
            }
        });
    }
});

emailField1.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;

    emailField1.classList.remove('is-invalid');

    if (emailVal.length > 0) {
        fetch("/validate-email-one", {
            body: JSON.stringify({ email1: emailVal }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            if (data.email_error) {
                emailField1.classList.add('is-invalid');
                submitbtn.disabled = true;
            }
            else {
                submitbtn.removeAttribute("disabled");
            }
        });
    }
});

messageField1.addEventListener("keyup", (e) => {
    const addressVal = e.target.value;

    messageField1.classList.remove('is-invalid');

    if (addressVal.length > 0) {
        fetch("/validate-message-one", {
            body: JSON.stringify({ message: addressVal }),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            if (data.address_error) {
                messageField1.classList.add('is-invalid');
                submitbtn.disabled = true;
            }
            else {
                submitbtn.removeAttribute("disabled");
            }
        });
    }
});

nameField1.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;

    usernameField.classList.remove('is-invalid');

    if (usernameVal.length > 0) {
        fetch("/validate-name-one", {
            body: JSON.stringify({ name1: usernameVal}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            if (data.username_error) {
                nameField1.classList.add('is-invalid');
                submitbtn.disabled = true;
            }
            else {
                submitbtn.removeAttribute("disabled");
            }
        });
    }
});