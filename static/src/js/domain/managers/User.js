export class UserFactory{
    roleFactory;
    constructor(roleFactory) {
        this.roleFactory = roleFactory
    }
    make(name, role_id){
        let role = this.roleFactory.makeRole(role_id)
        return (new User(name)).setRole(role)
    }
}

class User{
    constructor(name) {
        this.name = name
    }

    setRole(role){
        this.role = role
        return this
    }
}