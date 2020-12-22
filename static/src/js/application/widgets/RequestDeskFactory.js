import React from 'react'

export class RequestDeskFactory {
    constructor(requestFactory) {
        this.requestFactory = (props) => requestFactory.makeRequest(props)

    }
    makeWidget(data, provider){
        let requests = this.makeRequests(data, provider)
        return new RequestDesk(requests, provider)
    }

    *makeRequests(data, provider){
        data = data || []
        for (let r of data){
            yield <this.requestFactory id={r.id} topic={r.topic} comment={r.comment} user={r.user} date={r.date} provider={provider}/>
        }
    }
}

class RequestDesk{
    constructor(requests, provider){
        this.requests = [...requests]
        this.provider = provider
    }

    generateHTML() {
        return (
            <div>
                <div id="card-container">
                    { this.requests }
                </div>
            </div>
        )
    }
}