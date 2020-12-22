import React from "react"

export class App{
    constructor(mainPageView, loginPage, adminPage, requestPage,
                router, adminRoute, privateRoute, loginRoute, navbar, loginManager,
                announcementProvider, requestProvider, tableRequestPage, tablesProvider){
        this.provider = announcementProvider
        this.reqProvider = requestProvider
        this.mainPage = (props) => new mainPageView(props)
        this.loginPage = loginPage
        this.adminPage = adminPage
        this.router = router
        this.privateRoute = privateRoute
        this.loginRoute = loginRoute
        this.requestPage = (props) => new requestPage(props)
        this.tableRequestPage = tableRequestPage
        this.tablesProvider = tablesProvider
        this.adminRoute = (props) => adminRoute(props)
        this.navBar =navbar
        this.loginManager = loginManager
    }

    Render = (props) => {
        return (
            <div className="App">
                <this.router>
                    {this.loginManager.checkAuthorize() && <this.navBar loginManager={() => this.loginManager} />}
                    <div>
                        <this.privateRoute path='/' exact={true}  component={(props) => <this.mainPage announcementProvider={() => this.provider}/>}/>
                        <this.privateRoute path='/request' exact={true} component={(props) => <this.requestPage requestProvider={() => this.reqProvider}/>}/>
                        <this.adminRoute path='/admin' exact={true} component={this.adminPage}/>
                        <this.loginRoute path="/login" exact={true} component={this.loginPage}/>
                        <this.privateRoute path="/request_table" exact={true} component={(props) => <this.tableRequestPage tablesProvider={() => this.tablesProvider}/>}/>
                    </div>
                </this.router>
            </div>
        )
    }
}