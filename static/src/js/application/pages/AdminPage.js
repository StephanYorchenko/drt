export class AdminFactory{
    constructor(api, adminTableFactory) {
        this.tableFactory = adminTableFactory
        this.api = api
    }
    makeWidget(manager){
        return new Admin(manager, this.api, this.tableFactory)
    }
}

class Admin{
    constructor(manager, api, tableFactory) {
        this.tableFactory = tableFactory
        this.manager = manager
        this.api = api
    }

    generateHTML(){
        return this.tableFactory.makeTable(["#", "Логин", "Пароль", "Роль"])
    }
}