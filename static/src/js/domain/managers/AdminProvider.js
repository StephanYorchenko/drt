export class AdminProvider{
    page;

    constructor(api, md5, role, roleList) {
        this.api = api
        this.md5 = md5
        this.roleChecker = role
        this.roleList = roleList
    }

    deleteUser(username){
        let form = new FormData()
        form.append('username', username)
        this.api.delete('/api/user', form)
        if (this.page != null)
            this.page.update(this.getUserList())
    }

    setPage(page){
        this.page = page
    }

    getUserList(){
        let userList = this.api.get('/api/user/list');
        console.log(userList)
        if (userList !== false){
            let users = []
            for (let i = 0; i < userList.user_list.length; i++)
                users.push([i, userList.user_list[i].name,  userList.user_list[i].role])
            return users
        }
        return []
    }

    changePassword(event, name, password, role){
        let formData = new FormData()
        formData.append("name", name)
        formData.append("password", this.md5(password))
        formData.append("role", this.roleChecker(role))
        this.api.post('/api/user', formData)
        event.target.value = ""
    }

    createUser(event){
        event.preventDefault();
        let form = event.target
        let formData = new FormData()
        formData.append("name", form._name.value)
        formData.append("password", this.md5(form.password.value))
        formData.append("role", this.roleChecker(form.roles.value))
        this.api.post('/api/user', formData)
        this.page.update(this.getUserList())
        form.reset()
    }
}