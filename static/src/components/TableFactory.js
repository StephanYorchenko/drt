export class TableFactory{
    constructor(api, md5){
        this.api = api
        this.md5 = md5
    }
    makeTable(fields, items){
        let div = document.createElement("div")
        let table = document.createElement("table")
        table.className = "table"
        table.style.width = "70%"
        table.style.margin = "auto"
        table.append(this.generateHead(fields))
        for (let item of items){
            table.append(this.generateRow(item))
        }
        div.append(table)
        div.append(this.generateModalWindow())
        return div
    }

    generateHead(fields){
        let head = document.createElement("thead")
        let tr = document.createElement("tr")
        head.append(tr)
        for (let field of fields){
            let new_field = document.createElement("th")
            new_field.setAttribute("scope", "col")
            new_field.innerText = field
            tr.append(new_field)
        }
        return head
    }

    generateRow(item){
        let row = document.createElement("tr")

        for (let i = 0; i < item.length; i++){
            let cell = document.createElement("td")
            if (i === 1){
                cell.innerHTML = "<a href=\"#uploadModal\" data-toggle=\"modal\">" + item[i] + "</a>\n"
                cell.getElementsByTagName("a").item(0).addEventListener("click", () => {
                    this.updateModalName(item[1])
                } )
            } else{
                cell.innerText = item[i]
            }
            row.append(cell)
        }
        return row
    }

    updateModalName(name){
        let span = document.getElementById("userName");
        span.innerText = "@" + name;
        return false
    }
    
    generateModalWindow(){
        let modal = document.createElement("div");
        modal.innerHTML = `<div class="modal fade" id="uploadModal" tabindex="-2" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true" data-backdrop="static">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="modalLabel">Настройка пользователя <span id="userName"></span></h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div>
                        <form name="userConfig" novalidate>
                            <div class="form-group row">
                                    <label for="inputPassword" class="col-sm-4 col-form-label">Изменить пароль</label>
                                    <div class="col-sm-5">
                                        <input type="password" class="form-control" id="inputPassword" name="password">
                                    </div>
                                </div>
                            <button type="submit" class="btn btn-primary col" name="submit" value="Conf">Применить изменения</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
`
        modal.getElementsByTagName("form").item(0).addEventListener("submit", (event) => this.configureUser(event))
        return modal
    }

    configureUser(event){
        event.preventDefault();
        console.log(this, this.api)
        let request = this.api.getXmlHttp()
        let form = document.forms.userConfig
        let name = document.getElementById("userName").innerText.substring(1)
        request.open("POST", '/api/user', false)
        let formData = new FormData()
        formData.append("name", name)
        formData.append("password", this.md5(form.password))
        formData.append("role", '1')
        request.send(formData)
    }

    /*
    <a href="#uploadModal" class="btn btn-primary" data-toggle="modal">Отправить csv</a>
     */
}