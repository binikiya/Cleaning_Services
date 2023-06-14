const nameField = document.querySelector('#nameField');
const nickField = document.querySelector('#nickField');
const submitBtn = document.querySelector('.submit-btn');

nameField.addEventListener("keyup", (e) => {
    const nameVal = e.target.value;

    nameField.classList.remove('is-invalid');

    if (nameVal.length > 0) {
        fetch("/pricing/name-validation", {
            body: JSON.stringify({ name: nameVal}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            if (data.username_error) {
                nameField.classList.add('is-invalid');
                submitBtn.disabled = true;
            }
            else {
                submitBtn.removeAttribute("disabled");
            }
        });
    }
});

nickField.addEventListener("keyup", (e) => {
    const nickVal = e.target.value;

    nickField.classList.remove('is-invalid');

    if (nickVal.length > 0) {
        fetch("/pricing/nick-validation", {
            body: JSON.stringify({ nick: nickVal}),
            method: "POST",
        })
        .then((res) => res.json())
        .then((data) => {
            console.log('data', data);
            if (data.username_error) {
                nickField.classList.add('is-invalid');
                submitBtn.disabled = true;
            }
            else {
                submitBtn.removeAttribute("disabled");
            }
        });
    }
});