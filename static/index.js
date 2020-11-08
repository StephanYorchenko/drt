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

function previous_page() {
    let current = document.getElementById('current');
    if (+current.innerText !== 1){
        current.innerText = +current.innerText - 1 + '';
        get_count(+current.innerText);
    }
}

function next_page() {
    let current = document.getElementById('current');
    if (+current.innerText !== globalThis.MAX_COUNT){
        current.innerText = +current.innerText + 1 + '';
        get_count(+current.innerText);
    }
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


function create_announcement_card(an) {
    let card = document.createElement('div');
    card.className = 'card announcement';
    let body = document.createElement('div');
    body.className = 'card-body';
    let title = document.createElement('h4');
    title.className = 'card-title';
    title.innerText = an['title'];
    let content = document.createElement('p');
    content.className = 'card-text';
    content.innerText = an['text'];
    let footer = document.createElement('div');
    footer.className = "card-footer text-muted";
    footer.innerText = an['date'];

    card.append(body);
    body.append(title);
    body.append(content);
    body.append(footer);

    return card;
}

function update_card_container(announcements) {
    let container = document.getElementById("card-container");
    container.innerHTML = '';
    for (let an of announcements){
        container.append(create_announcement_card(an))
    }
}

function get_count(page) {
    if (page === undefined) page = 1;
    let xmlHttp = getXmlHttp();
    xmlHttp.onload = function () {
        const data = JSON.parse(xmlHttp.responseText);
        globalThis.MAX_COUNT = +data.count;
        console.log(data.count);
        update_card_container(data.announcements);
     }
    xmlHttp.open("GET", '/get_count?page_number=' + page, false);
    xmlHttp.send();
}

class Page{
    constructor(builder){
        this.header = builder.header || false
        this.mainWidget = builder.mainWidget
        this.footer = builder.footer || false
    }

    show() {
        for (let element of this.generate()){
            document.body.append(element)
        }
    }

    *generate(){
        if (this.header)
            yield this.header.generateHTML()
        yield this.mainWidget
        if (this.footer)
            yield this.footer.generateHTML()
    }
}

class Header{
    constructor(builder){
        this.brand = builder.brand || false
        this.links = builder.links
        this.userName = builder.userName || false
    }

    generateHTML(){
        let navBar = document.querySelector('#navbar')
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
    constructor(mainWidget){
        this.mainWidget = mainWidget
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

document.addEventListener('DOMContentLoaded', () =>
{
    document.cookie = "name=Stepan;role=1"
    const header = (new HeaderBuilder())
        .setBrand("DRT")
        .addLink((new LinkBuilder("Главная")).setClassName("active").build())
        .addLink((new LinkBuilder("Заявки")).build())
        .build()
    let mainWidget = document.createElement("div")
    mainWidget.innerHTML = "<div id=\"card-container\"></div>"

    const page = (new PageBuilder(mainWidget)
        .addHeader(header)
        .build())
    page.show()
    get_count()
});