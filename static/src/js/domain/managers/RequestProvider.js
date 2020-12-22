export class RequestProvider {
    constructor(api, requestDeskFactory, loginManager) {
        this.requestFactory = requestDeskFactory
        this.api = api;
        this.loginManager = loginManager;
    }

    getRequests() {
        const data = this.api.get("/api/request") || []
        return data.requests
    }

    updateContent(flag) {
        if (flag === undefined)
            flag = true
        let data = this.getRequests()
        let content = this.requestFactory.makeWidget(data, this).generateHTML()
        console.log(content)
        if (flag)
            this.page.contentUpdate(this.requestFactory.makeWidget(data, this).generateHTML() )
        return content
    }

    setPage(page) {
        this.page = page
        return this.updateContent(false)
    }

    checkHostess(){
        console.log("------")
        let a = this.loginManager.isHostess()
        console.log(a)
        console.log("#########")
        return a !== false;
    }

    sendNew(data){
        let form = document.forms.newRequest
        let formData = new FormData()
        formData.append("topic", data.topic)
        formData.append("comment", data.comment)
        formData.append("username", this.loginManager.user.name)
        this.api.post('/api/request', formData)
        form.reset()
        this.updateContent(true)
    }

    Approve(request, event){
        event.preventDefault();
        let _id = event.target.firstChild.innerText
        let formData = new FormData()
        formData.append("id", _id)
        this.api.put('/api/request', formData)
        this.updateContent(true)
    }
}