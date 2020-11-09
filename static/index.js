const MAX_COUNT = 0;

function getCookie(c_name) {
    let c_value = " " + document.cookie;
    let c_start = c_value.indexOf(" " + c_name + "=");
    if (c_start === -1) {
        c_value = null;
    }
    else {
        c_start = c_value.indexOf("=", c_start) + 1;
        let c_end = c_value.indexOf(";", c_start);
        if (c_end === -1) {
            c_end = c_value.length;
        }
        c_value = unescape(c_value.substring(c_start,c_end));
    }
    return c_value;
}

function getXmlHttp() {
    let xmlhttp;
    try {
      xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
    } catch (e) {
    try {
      xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    } catch (E) {
      xmlhttp = false;
    }
    }
    if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
      xmlhttp = new XMLHttpRequest();
    }
    return xmlhttp;
}



class Page{
    constructor(builder){
        this.header = builder.header || false
        this.widgetFactory = builder.widgetFactory
        this.manager = builder.manager
        this.updateWidget()
        this.footer = builder.footer || false
    }

    show() {
        document.body.innerHTML = ""
        for (let element of this.generate()){
            document.body.append(element)
        }
    }

    *generate(){
        if (this.header)
            yield this.header.generateHTML()
        yield this.mainWidget.generateHTML()
        if (this.footer)
            yield this.footer.generateHTML()
    }

    updateWidget(data){
        console.log("updateWidget")
        this.mainWidget = this.widgetFactory.makeWidget(this.manager, data)
        this.show()
    }

}

class Header{
    constructor(builder){
        this.brand = builder.brand || false
        this.links = builder.links
        this.userName = builder.userName || false
    }

    generateHTML(){
        //<nav class="navbar navbar-expand-lg navbar-dark bg-dark" id="navbar"></nav>
        let navBar = document.createElement("nav")
        navBar.className = "navbar navbar-expand-lg navbar-dark bg-dark"
        //let navBar = document.querySelector('#navbar')
        if (this.brand){
            let brand = document.createElement("a")
            brand.className = "navbar-brand"
            brand.innerText = "DoubleRT"
            brand.href = "#"
            navBar.append(brand)
        }
        let collapse = document.createElement("div")
        collapse.className = "collapse navbar-collapse"
        collapse.id = "navbarSupportedContent"
        let ul_left = document.createElement("ul")
        ul_left.className = "navbar-nav mr-auto"
        collapse.append(ul_left)
        for (let link of this.links){
            ul_left.append(link.generateHTML())
        }

        let ul_right = document.createElement("ul")
        ul_right.className = "navbar-nav ml-auto"
        let user_li = document.createElement("li")
        user_li.className = "nav-item dropdown"
        /*
        <a class= href="#" id= role="button" data-toggle="dropdown" ="true" ="false" style="">
                {{ session['name'] or 'user_name' }}
            </a>
         */
        let user_name = document.createElement("a")
        user_name.className = "nav-link dropdown-toggle"
        user_name.id = "navbarDropdown"
        user_name.href = "#"
        user_name.role = "button"
        user_name.setAttribute("data-toggle", "dropdown")
        user_name.setAttribute("aria-haspopup", "true")
        user_name.setAttribute("aria-expanded", "false")
        user_name.setAttribute("style", "margin-right: 80px !important;")
        user_name.innerText = this.userName
        let user_logout = document.createElement("div")
        /*
        <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                <a class="dropdown-item" href="#">Выход</a>
            </div>
         */
        user_logout.className = "dropdown-menu"
        user_name.setAttribute("aria-labelledby", "navbarDropdown")
        let logout = document.createElement("a")
        logout.className = "dropdown-item"
        logout.href = "/logout"
        logout.innerText = "Выход"
        user_logout.append(logout)

        user_li.append(user_name)
        user_li.append(user_logout)

        ul_right.append(user_li)

        navBar.append(ul_left)
        navBar.append(ul_right)

        return navBar
    }
}

class HeaderBuilder{
    constructor(){
        this.links = []
        this.setUser()
    }

    setBrand(brand){
        this.brand = brand
        return this
    }

    addLink(link){
        this.links.push(link)
        return this
    }

    setUser(){
        this.userName = getCookie("name")
        let role = getCookie("role")
        if (+role === 1){
            this.addLink(
                (new LinkBuilder("Администрирование"))
                    .build()
            )
        }
        else if (+role === 2){
            this.addLink(
                (new LinkBuilder("Заявки"))
                    .build()
            )
        }
        return this
    }

    build() {
        return new Header(this);
    }
}

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

class LinkBuilder{
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

class PageBuilder{
    constructor(widgetFactory, manager){
        this.widgetFactory = widgetFactory
        this.manager = manager
    }

    addHeader(header){
        this.header = header
        return this
    }

    // addFooter(footer){
    //     this.footer = footer
    //     return this
    // }

    build() {
        return new Page(this)
    }
}

class Announcement{
    constructor(builder) {
        this.title = builder.title
        this.text = builder.text
        this.date = builder.date
        this.attachment = builder.attachment || false
    }

    generateHTML(){
        let card = document.createElement('div');
        card.className = 'card announcement';
        let body = document.createElement('div');
        body.className = 'card-body';
        let title = document.createElement('h4');
        title.className = 'card-title';
        title.innerText = this.title;
        let content = document.createElement('p');
        content.className = 'card-text';
        content.innerText = this.text;
        let footer = document.createElement('div');
        footer.className = "card-footer text-muted";
        footer.innerText = this.date;

        card.append(body);
        body.append(title);
        body.append(content);
        body.append(footer);

        return card;
    }
}

class AnnouncementBuilder{
    constructor(title) {
        this.title = title
    }

    addAttachment(type, data){
        if (type !== undefined)
            this.attachment = {type: type, data: data}
        return this
    }

    addText(text){
        this.text = text
        return this
    }

    addDate(date){
        this.date = date
        return this
    }

    build(){
        return new Announcement(this)
    }
}

class DeskFactory {
    makeWidget(manager, pageNumber){
        if (pageNumber === undefined) pageNumber = 1;
        console.log(manager, pageNumber)
        let data = this.getAnnouncementsData(pageNumber)
        let announcements = this.makeAnnouncements(data)
        console.log(announcements)
        return new AnnouncementDesk(announcements, pageNumber, manager)
    }

    getAnnouncementsData(page) {

        let xmlHttp = getXmlHttp();
        xmlHttp.open("GET", '/get_count?page_number=' + page, false);
        xmlHttp.send()
        const data = JSON.parse(xmlHttp.responseText)
        globalThis.MAX_COUNT = +data.count
        return data.announcements
    }

    *makeAnnouncements(data){
        for (let announcement of data){
            yield (new AnnouncementBuilder(announcement.title)
                .addText(announcement.text)
                .addDate(announcement.date)
                .addAttachment(announcement.attachmentType, announcement.attachmentData)
                .build())
        }
    }
}

class AnnouncementDesk{
    constructor(announcements, pageNumber, manager){
        this.announcements = announcements
        this.pageNumber = pageNumber
        this.manager = manager
    }

    updatePage(targetPage){
        console.log("here!!!")
        this.manager.updatePage(targetPage)
    }

    generateHTML() {
        let desk = document.createElement("div")
        let container = document.createElement("div")
        container.id = "card-container"
        for (let an of this.announcements){
            container.append(an.generateHTML())
        }
        let footer = this.generateFooter()
        desk.append(container)
        desk.append(footer)
        return desk
    }

    generateFooter(){
        let footer = document.createElement("footer")
        let nav = document.createElement("nav")
        nav.className = "horizontal-centered"
        let ul_nav = document.createElement("ul")
        ul_nav.className = "pagination announcement-nav"
        let pr_but = document.createElement('li')
        let cur_al = document.createElement("li")
        let next_but = document.createElement("li")

        let a = document.createElement("a")
        a.className = "page-link"
        a.onclick = this.previousPage
        a.innerText = "Previous"
        pr_but.append(a)

        let cur = document.createElement("a")
        cur.className = "page-link"
        cur.innerText = this.pageNumber
        cur_al.append(cur)

        let aa = document.createElement("a")
        aa.className = "page-link"
        aa.onclick = this.nextPage
        aa.innerText = "Next"
        next_but.append(aa)

        ul_nav.append(pr_but, cur_al, next_but)
        nav.append(ul_nav)
        footer.append(nav)

        return footer

    }

    previousPage = () => {
        console.log("previous")
        if (this.pageNumber !== 1)
            this.updatePage(this.pageNumber - 1)
    }

    nextPage = () => {
        console.log(this.pageNumber, globalThis.MAX_COUNT)
        if (this.pageNumber !== globalThis.MAX_COUNT)
            this.updatePage(this.pageNumber + 1)
    }
}

class Manager{
    constructor(page) {
        this.page = page || false
    }

    updatePage(data){
        console.log(data, "manager")
        this.page.updateWidget(data)
    }

    setPage(page){
        this.page = page
    }

}

document.addEventListener('DOMContentLoaded', () =>
{
    document.cookie = "name=Stepan;role=1"
    const header = (new HeaderBuilder())
        .setBrand("DRT")
        .addLink((new LinkBuilder("Главная")).setClassName("active").build())
        .addLink((new LinkBuilder("Заявки")).build())
        .build()
    const deskFactory = new DeskFactory()
    const manager = new Manager()

    const page = (new PageBuilder(deskFactory, manager)
        .addHeader(header)
        .build())

    manager.setPage(page)
    manager.updatePage(1)
});