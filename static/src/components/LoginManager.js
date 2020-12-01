export class LoginManager{
    userFactory;
    user;

    constructor(userFactory, md5, api, loginPage) {
        this.setPage(loginPage)
        this.md5 = md5
        this.api = api
        this.userFactory = userFactory;
        this.is_authorized = false
    }

    tryAuthorize(data){
        let xmlHttp = this.api.getXmlHttp();
        xmlHttp.open("POST", '/api/auth', false)
        let formData = new FormData()
        formData.append("name", data.name)
        formData.append("password", this.md5(data.password))
        xmlHttp.send(formData);
        const response = JSON.parse(xmlHttp.responseText);
        if (response.authorized){
            this.setUser(response.Name, response.Role)
            this.manager.updatePage(1)
        }
    }

    setUser(name, role){
        this.is_authorized = true
        this.user = this.userFactory.makeUser(name, role)
    }

    setManager(manager){
        this.manager = manager
        return this
    }

    checkAuthorize(){
        let name = this.api.getCookie("name")
        if (name == null)
            return false
        let xmlHttp = this.api.getXmlHttp();
        xmlHttp.open("POST", '/api/check', false)
        let formData = new FormData()
        formData.append("name", name)
        xmlHttp.send(formData)
        let answer = JSON.parse(xmlHttp.responseText).result
        console.log(answer)
        if (answer){
            this.setUser(name, +this.api.getCookie("role"))
        } else{
            this.clearUser()
        }
        return answer
    }

    setPage(loginPage){
        console.log('here', loginPage)
        this.loginPage = loginPage
        this.loginPage.setManager(this)
        console.log('here', loginPage)
        return this
    }

    clearUser() {
        this.user = undefined
        this.is_authorized = false
        let xmlHttp = this.api.getXmlHttp();
        xmlHttp.open("POST", '/api/logout', false)
        xmlHttp.send()
        console.log(this.loginPage)
        this.loginPage.updateWidget()
    }
}
