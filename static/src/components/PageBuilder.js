import {Page} from "./Page"

export class PageBuilder{
    constructor(widgetFactories){
        this.widgetFactories = widgetFactories
    }

    addHeader(header){
        this.header = header
        return this
    }

    addFooter(footer){
        this.footer = footer
        return this
    }

    build() {
        return new Page(this)
    }
}