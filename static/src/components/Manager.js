export class Manager{
    constructor(page, loginManager) {
        this.setPage(page || false)
        this.setLoginManager(loginManager || false)
    }

    updatePage(data){
        this.page.updateWidget(data)
        return this
    }

    setPage(page){
        if (page) {
            this.page = page || this.main_page
            this.page.setManager(this)
        }
        return this
    }

    setLoginManager(loginManager){
        if (loginManager) {
            this.loginManager = loginManager
            this.loginManager.setManager(this)
        }
        return this
    }

    start(){
        if (this.loginManager.checkAuthorize())
            this.updatePage(1)
        else
            this.loginManager.clearUser()
    }

    showAuth(authPage){
        this.main_page = this.page
        authPage.show()
    }
}
