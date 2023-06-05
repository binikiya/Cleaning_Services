/* style switcher */
const styleSwitcherToggle = () => {
    const styleSwitcheer = document.querySelector(".js-style-switcher");
    const styleSwitcheerToggler = document.querySelector(".js-style-switch-toggler");

    styleSwitcheerToggler.addEventListener("click", function() {
        styleSwitcheer.classList.toggle("open");
        this.querySelector("i").classList.toggle("fa-times");
        this.querySelector("i").classList.toggle("fa-cog");
    });
}
styleSwitcherToggle();

/* theme color */
const themeColor = () => {
    const hueSlinder = document.querySelector(".js-hue-slinder");
    const html = document.querySelector("html");

    const setHue = (value) => {
        html.style.setProperty("--hue", value);
        document.querySelector(".js-hue").innerHTML = value;
    }

    hueSlinder.addEventListener("input", function() {
        setHue(this.value);
        localStorage.setItem("--hue", this.value);
    });

    const slider = (value) => {
        hueSlinder.value = value;
    }

    /* check for user saved preference */
    if (localStorage.getItem("--hue") != null) {
        setHue(localStorage.getItem("--hue"));
        slider(localStorage.getItem("--hue"));
    }
    /* defaul color */
    else {
        const hue = getComputedStyle(html).getPropertyValue("--hue");
        setHue(hue);
        slider(hue.split(" ").join(""));
    }
}
themeColor();

/* theme light and dark mode */
const themeLightDark = () => {
    const darkModeCheckbox = document.querySelector(".js-dark-mode");

    const themeMode = () => {
        if (localStorage.getItem("theme-dark") === "false") {
            document.body.classList.remove("t-dark");
        }
        else {
            document.body.classList.add("t-dark");
        }
    }

    darkModeCheckbox.addEventListener("click", function(){
        localStorage.setItem("theme-dark", this.checked);
        themeMode();
    });

    /* check for saved user preferences */
    if (localStorage.getItem("theme-dark") != null) {
        themeMode();
    }
    else {
        darkModeCheckbox.checked = true;
    }
}
themeLightDark();