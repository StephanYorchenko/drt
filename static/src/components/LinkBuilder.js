class Link{
    constructor(builder){
        this.text = builder.text
        this.onclick = builder.onclick || function () {console.log("click")}
        this.className = builder.className || ""
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

export class LinkBuilder{
    constructor(text) {
        this.text = text
    }

    setOnClick(onClickAction){
        this.onclick = onClickAction
        return this
    }

    setClassName(className){
        this.className = className
        return this
    }

    build(){
        return new Link(this)
    }
}