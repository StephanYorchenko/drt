export class TableFactory{
    makeTable(fields, items){
        let table = document.createElement("table")
        table.className = "table"
        table.style.width = "70%"
        table.style.margin = "auto"
        table.append(this.generateHead(fields))
        for (let item of items){
            table.append(this.generateRow(item))
        }
        return table
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
        for (let val of item){
            let cell = document.createElement("td")
            cell.innerText = val
            row.append(cell)
        }
        return row
    }
}