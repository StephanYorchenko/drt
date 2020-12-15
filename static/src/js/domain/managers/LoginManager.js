export class LoginManager{
    user;

    constructor(md5, api, userFactory) {
        this.md5 = md5
        this.api = api
        this.userFactory = userFactory
        this.user = null
    }

    tryAuthorize(data){
        let formData = new FormData()
        formData.append("name", data.name)
        formData.append("password", this.md5(data.password))
        const result = this.api.post('/api/auth', formData)
        let user = result.authorized ? this.makeUser(result.Name, result.Role) : null
        if (result.authorized && this.nav != null){
            this.nav.setUser()
        }
        return user
    }

    setNav(nav){
        this.nav = nav
        return this
    }

    checkAuthorize() {
        let name = this.api.getCookie("name")
        if (name == null)
            return false
        let formData = new FormData()
        formData.append("name", name)
        let answer = this.api.post('/api/auth/check', formData)
        return answer.result ? this.makeUser() : this.clearUser()
    }

    isAdmin(){
        if (this.checkAuthorize()){
            if (+this.api.getCookie("role") === 1)
                return this.user
        }
        return false
    }

    isHostess(){
        if (this.checkAuthorize()){
            if (+this.api.getCookie("role") === 2)
                return this.user
        }
        return false
    }

    clearUser() {
        this.user = null
        console.log(document.cookie)
        this.api.clearCookies()
        console.log(document.cookie)
        this.api.post('/api/user/logout');
        return false
    }


    makeUser(Name, Role) {
        let name = Name || this.api.getCookie("name")
        let role = Role || this.api.getCookie("role")
        this.user = this.userFactory.make(name, role)
        return this.user
    }
}
