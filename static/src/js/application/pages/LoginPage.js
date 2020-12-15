import React from "react";

export class AuthorizeFormFactory{
    constructor(loginManager, redirectPage) {
        this.loginManager = loginManager
        this.redirect = redirectPage
    }
    makeWidget(){
        return new AuthorizeForm(this.loginManager, this.redirect)
    }
}

class AuthorizeForm{
    constructor(loginManager, redirect) {
        this.manager = loginManager
        this.redirect = redirect
    }

    tryAuthorize = (event) => {
        event.preventDefault();
        this.manager.tryAuthorize(this.getFormData())
        console.log(this.manager)
        if (this.manager.user != null){
            document.location.href = '/'
        }
    }

    generateHTML(){
        return (
            <div className="limiter">
                <div className="container-login100">
                    <div className="wrap-login100 p-l-85 p-r-85 p-t-55 p-b-55">
                        <form className="login100-form validate-form flex-sb flex-w" onSubmit={this.tryAuthorize} name="login">
                            <span className="login100-form-title p-b-32">Авторизация</span>
                            <span className="txt1 p-b-11">Имя пользователя</span>
                            <div className="wrap-input100 validate-input m-b-36\">
                                <input className="input100" type="text" id="username" />
                                <span className="focus-input100"/>
                            </div>
                            <span className="txt1 p-b-11">Пароль</span>
                            <div className="wrap-input100 validate-input m-b-12">
                                <input className="input100" type="password" id="password" />
                                <span className="focus-input100"/>
                            </div>
                            <div className="container-login100-form-btn">
                                <button type="submit" className="login100-form-btn">Войти</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        )
    }

    render(){
        return (this.manager.user != null) ? <this.redirect to='/' /> :  () => this.generateHTML()
    }

    getFormData() {
        const data = {
            name: document.getElementById("username").value,
            password: document.getElementById("password").value
        }
        document.forms.login.reset()
        return data
    }
}