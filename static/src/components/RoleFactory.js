export class RoleFactory {
    makeRole(role_id){
        return new Role(role_id)
    }
}

class Role{
    Roles = ["Администратор", "Заведующий"]
    TagNames = ["Администрирование", "Запросы"]
    constructor(role_id){
        this.role_name = this.Roles[role_id]
        this.tag = this.TagNames[role_id]
    }
}