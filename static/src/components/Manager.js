export class Manager{
    constructor(page) {
        this.page = page || false
        this.loginManager = false
    }

    updatePage(data){
        this.page.updateWidget(data)
        return this
    }

    setPage(page){
        this.page = page || this.main_page
        return this
    }

    setLoginManager(loginManager){
        this.loginManager = loginManager
        return this
    }

    start(){
        if (this.loginManager.checkAuthorize())
            this.updatePage(1)
        else
            this.showAuth(this.loginManager.loginPage)
    }

    showAuth(authPage){
        this.main_page = this.page
        authPage.show()
    }
}
