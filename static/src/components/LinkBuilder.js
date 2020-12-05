class Link{
    constructor(text, className){
        this.text = text
        this.onclick = function () {console.log("click")}
        this.className = className || ""
    }

    generateHTML(){
        let li = document.createElement("li")
        li.className = "nav-item " + this.className
        let a = document.createElement("a")
        a.addEventListener("click", this.onclick)
        a.className = "nav-link"
        a.innerText = this.text
        li.append(a)
        return li
    }

    setAction(action){
        this.onclick = action
    }
}

export class LinkFactory{
    make(text, className){
        return new Link(text, className)
    }
}