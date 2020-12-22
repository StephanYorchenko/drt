export class Api{
    constructor(cookie, request) {
        this.cookie = cookie
        this.request = request
    }
    createRequest () {
        return new XMLHttpRequest()
    }

    get(request) {
        let xmlHTTP = this.createRequest()
        xmlHTTP.open('GET', request, false)
        xmlHTTP.send()
        console.log(xmlHTTP)
        return (xmlHTTP.status === 200 ) ? JSON.parse(xmlHTTP.responseText) : false
    }

    post(addr, data) {
        console.log('post method')
        let xmlHTTP = this.createRequest()
        xmlHTTP.open('POST', addr, false)
        xmlHTTP.send(data)
        return (xmlHTTP.status === 200 ) ? JSON.parse(xmlHTTP.responseText) : false
    }

    put(addr, data) {
        console.log('put method')
        let xmlHTTP = this.createRequest()
        xmlHTTP.open('PUT', addr, false)
        xmlHTTP.send(data)
        return (xmlHTTP.status === 200 ) ? JSON.parse(xmlHTTP.responseText) : false
    }

    delete(addr, data){
        let xmlHTTP = this.createRequest()
        xmlHTTP.open('DELETE', addr, false)
        xmlHTTP.send(data)
        return (xmlHTTP.status === 200 ) ? JSON.parse(xmlHTTP.responseText) : false
    }

    getCookie(c_name) {
        return this.cookie.get(c_name)
    }

    clearCookies(){
        document.cookie.split(";").forEach((c) => {
          document.cookie = c
            .replace(/^ +/, "")
            .replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/");
        });
    }
}