export class Page{
    constructor(builder){
        this.header = builder.header || false
        this.widgetFactories = builder.widgetFactories
        this.manager = false
        this.updateWidget()
        this.footer = builder.footer || false
    }

    show() {
        document.getElementById("app").innerHTML = ""
        for (let element of this.generate()){
            document.getElementById("app").append(element)
        }
    }

    *generate(){
        if (this.header)
            yield this.header.generateHTML()
        yield this.mainWidget.generateHTML()
        if (this.footer)
            yield this.footer.generateHTML()
    }

    updateWidget(widget, data){
        if (this.manager) {
            this.mainWidget = this.widgetFactories[widget].makeWidget(this.manager, data)
            this.show()
        }
    }

    setManager(manager){
        this.manager = manager
    }
}
