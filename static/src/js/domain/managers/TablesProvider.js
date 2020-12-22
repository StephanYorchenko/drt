export class TablesProvider {
    constructor(api, loginManager) {
        this.api = api;
        this.loginManager = loginManager;
    }

    sendForm(data) {
        let form = new FormData()
        form.append('username', this.loginManager.getUserName())
        form.append('number', data.item)
        form.append('date', data.date)
        let response = this.api.post("/api/table_request", form)
        return response.result
    }
}