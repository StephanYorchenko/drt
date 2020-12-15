import React from "react";

export class TableFactory{
    constructor(api, md5, adminProvider){
        this.api = api
        this.md5 = md5
        this.adminProvider = adminProvider
    }

    makeTable(fields){
        return  <AdminTable fields={fields} adminProvider={() => this.adminProvider}/>
    }
}

class AdminTable extends React.Component{
    constructor(props){
        super(props)
        this.provider = props.adminProvider()
        this.provider.setPage(this)
        this.state = {
            users: this.provider.getUserList(),
            fields: props.fields
        }
    }

    update(users){
        this.setState({
            users: users,
            fields: this.state.fields
        })
    }

    generateRow(item){
        const deleteUser = () => this.provider.deleteUser(item[1])
        const config = (event) => this.provider.changePassword(event, item[1], event.target.value, item[2])
        const handleKeyDown = (event) => {
            if (event.key === 'Enter') {
                config(event)
            }
        }
        return (
            <tr>
                <td>{item[0]}</td>
                <td>{item[1]}</td>
                <td><input type="password" onKeyDown={handleKeyDown}/></td>
                <td>{item[2]}</td>
                <td><button onClick={deleteUser}>⮾</button></td>
            </tr>
        )
    }

    render(){
        const userCreate = (event) => this.provider.createUser(event)
        return (
            <div className="anForm">
                <table className="table">
                    <thead>
                        { this.state.fields.map((object) => <th scope="col">{object}</th>)}
                    </thead>
                    <tbody>
                        {this.state.users.map((item) => this.generateRow(item))}
                    </tbody>
                </table>
                <div className="card-footer">
                    <h5>Создание нового пользователя</h5>
                    <form className="form-row" name="new_user" onSubmit={userCreate}>
                        <input type="text" className="form-control-plaintext col" id="staticEmail2" name="_name" placeholder="Логин"/>
                        <input type="password" className="form-control col" id="inputPassword2" name="password" placeholder="Пароль"/>
                        <div className="form-group">
                            <select className="form-control" id="exampleFormControlSelect2" name="roles">
                                {this.provider.roleList.map((role) => <option>{role}</option>)}
                            </select>
                        </div>
                        <button type="submit" className="btn btn-primary col" name="submit">Создать</button>
                    </form>
                </div>
            </div>
        )
    }
}
