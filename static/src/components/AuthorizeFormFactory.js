export class AuthorizeFormFactory{
    makeWidget(manager){
        return new AuthorizeForm(manager)
    }
}

class AuthorizeForm{
    constructor(manager) {
        this.manager = manager
        console.log(this.manager)
        this.form = document.createElement("div")
    }

    tryAuthorize = () => {
        this.manager.tryAuthorize(this.getFormData())
    }

    generateHTML(){
        let limiter_div = document.createElement("div")
        limiter_div.className = "limiter"
        let container_login = document.createElement("div")
        container_login.className = "container-login100"
        let wrap_div = document.createElement("div")
        wrap_div.className = "wrap-login100 p-l-85 p-r-85 p-t-55 p-b-55"
        this.form.className = "login100-form validate-form flex-sb flex-w"
        this.form.innerHTML = "" +
            "<span class=\"login100-form-title p-b-32\">Авторизация</span>\n" +
            "<span class=\"txt1 p-b-11\">Имя пользователя</span>\n" +
            "<div class=\"wrap-input100 validate-input m-b-36\">\n" +
            "<input class=\"input100\" type=\"text\" id=\"username\" >\n" +
            "<span class=\"focus-input100\"></span>\n" +
            "</div>\n" +
            "<span class=\"txt1 p-b-11\">Пароль</span>\n" +
            "<div class=\"wrap-input100 validate-input m-b-12\">\n" +
            "<input class=\"input100\" type=\"password\" id=\"password\" >\n" +
            "<span class=\"focus-input100\"></span>\n" +
            "</div>"
        let btn_container = document.createElement("div")
        btn_container.className = "container-login100-form-btn"
        let btn = document.createElement("button")
        btn.className = "login100-form-btn"
        btn.addEventListener('click', this.tryAuthorize)
        btn.innerText = "Войти"

        limiter_div.append(container_login)
        container_login.append(wrap_div)
        wrap_div.append(this.form)
        this.form.append(btn_container)
        btn_container.append(btn)

        return limiter_div
    }

    getFormData(){
        return {
            name: document.getElementById("username").value,
            password: document.getElementById("password").value
        }
    }
}
