export class AdminFactory{
    constructor(api, tableFactory) {
        this.tableFactory = tableFactory
        this.name = "Администрирование"
        this.api = api
    }
    makeWidget(manager){
        let users = this.getUserList()
        return new Admin(users, manager, this.api, this.tableFactory)
    }

    getUserList(){
        let xmlHttp = this.api.getXmlHttp();
        xmlHttp.open("GET", '/api/user/list', false);
        xmlHttp.send()
        let answer = JSON.parse(xmlHttp.responseText)
        return answer.user_list
    }
}

class Admin{
    constructor(users, manager, api, tableFactory) {
        this.tableFactory = tableFactory
        this.users = users
        this.manager = manager
        this.api = api
    }

    generateHTML(){
        let users = []
        for (let i = 0; i < this.users.length; i++){
            users.push([i, this.users[i].name,  this.users[i].role])
        }
        return this.tableFactory.makeTable(["#", "Логин", "Роль"], users)
    }
}