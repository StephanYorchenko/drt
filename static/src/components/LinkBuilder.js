class Link{
    constructor(text, className){
        this.text = text
        // this.onclick = builder.onclick || function () {console.log("click")}
        this.className = className || ""
    }

    generateHTML(){
        let li = document.createElement("li")
        li.className = "nav-item " + this.className
        let a = document.createElement("a")
        a.onclick = this.onclick
        a.className = "nav-link"
        a.innerText = this.text
        li.append(a)
        return li
    }
}

export class LinkFactory{
    make(text, className){
        return new Link(text, className)
    }
}