import {Page} from "./Page"

export class PageBuilder{
    constructor(widgetFactory, manager){
        this.widgetFactory = widgetFactory
        this.manager = manager
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