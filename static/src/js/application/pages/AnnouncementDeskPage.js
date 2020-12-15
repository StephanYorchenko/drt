import React from "react";

export class AnnouncementDeskPage extends React.Component{
    constructor(props){
        super(props);
        this.announcementProvider = props.announcementProvider()
        this.state = {current : this.announcementProvider.setPage(this)}
    }

    render(){
        return (
            <div>
                {this.announcementProvider.loginManager.isAdmin() && this.adminForm()}
                <div className="Content" id="containerAnnouncements">
                    {this.state.current}
                </div>
            </div>
        )
    }

    adminForm(){
        return (
            <form className="anForm" name="newAnnouncement" onSubmit={this.sendAnnouncement}>
                <input className="form-control form-control-lg" type="text" id="title" placeholder="Ваш заголовок"/>
                <textarea className="form-control" id="text" rows="3"/>
                <br/>
                <div className="container-login100-form-btn">
                    <button type="submit" className="login100-form-btn">Разместить</button>
                </div>
            </form>
        )
    }

    contentUpdate(content){
        this.setState({current: content})
    }

    sendAnnouncement = (event) => {
        event.preventDefault();
        this.announcementProvider.sendNew(this.getFormData())
    }

    getFormData(){
        const data = {
            title: document.getElementById("title").value,
            text: document.getElementById("text").value
        }
        document.forms.newAnnouncement.reset()
        return data
    }
}