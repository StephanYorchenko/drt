import React from "react";

export class RequestPage extends React.Component{
    constructor(props){
        super(props);
        this.requestProvider = props.requestProvider()
        this.state = {current : this.requestProvider.setPage(this)}
    }

    render(){
        return (
            <div>
                {this.adminForm()}
                {this.requestProvider.checkHostess() && <div className="cont" id="containerR">{this.state.current}</div>}
            </div>
        )
    }

    adminForm(){
        return (
            <form className="anForm" name="newRequest" onSubmit={this.sendRequest}>
                <input className="form-control form-control-lg" type="text" id="topic" placeholder="Тема"/>
                <textarea className="form-control" id="comment" rows="3" placeholder="Комментарий"/>
                <br/>
                <div className="container-login100-form-btn">
                    <button type="submit" className="login100-form-btn">Отправить</button>
                </div>
            </form>
        )
    }

    contentUpdate(content){
        this.setState({current: content})
    }

    sendRequest = (event) => {
        event.preventDefault();
        this.requestProvider.sendNew(this.getFormData())
    }

    getFormData(){
        const data = {
            topic: document.getElementById("topic").value,
            comment: document.getElementById("comment").value
        }
        document.forms.newRequest.reset()
        return data
    }
}