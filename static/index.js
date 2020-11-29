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
        this.mainWidget = this.widgetFactory.makeWidget(this.manager, data)
        this.show()
    }

}

class Header{
    constructor(builder){
        this.brand = builder.brand || false
        this.links = builder.links
        this.userName = false
    }

    generateHTML(){
        this.getUserName()
        let navBar = document.createElement("nav")
        navBar.className = "navbar navbar-expand-lg navbar-dark bg-dark"

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

    subscribeUserStorage(userStorage){
        this.userStorage = userStorage
        return this
    }
    
    getUserName(){
        let user = this.userStorage.user
        if (user !== undefined) {
            console.log(user, user.role, user.role.tag)
            this.userName = user.name
            if (user.role.role !== 0) {
                this.links[2] = (new LinkBuilder(user.role.tag)).build() //TODO: нет DIP
            } else if (this.links.length > 2)
                this.links.pop()

        }
    }
}

class HeaderBuilder{
    constructor(){
        this.links = []
        // this.linkBuilder = linkBuilder
    }

    setBrand(brand){
        this.brand = brand
        return this
    }

    addLink(link){
        this.links.push(link)
        return this
    }

    build() {
        return new Header(this);
    }
}
class RoleFactory{
    makeRole(role_id){
        return new Role(role_id)
    }
}

class UserFactory{
    roleFactory;
    constructor(roleFactory) {
        this.roleFactory = roleFactory
    }
    makeUser(name, role_id){
        let role = this.roleFactory.makeRole(role_id)
        return (new User(name)).setRole(role)
    }
}

class User{
    constructor(name) {
        this.name = name
    }

    setRole(role){
        this.role = role
        return this
    }

}

class Role{
    Roles = ["Администратор", "Заведующий"]
    TagNames = ["Администрирование", "Запросы"]
    constructor(role_id){
        this.role_name = this.Roles[role_id]
        this.tag = this.TagNames[role_id]
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

    addFooter(footer){
        this.footer = footer
        return this
    }

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
    // constructor(anBuilder) {
    //     this.anBuilder = anBuilder
    // }
    makeWidget(manager, pageNumber){
        if (pageNumber === undefined) pageNumber = 1;
        let data = this.getAnnouncementsData(pageNumber)
        let announcements = this.makeAnnouncements(data)
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
        if (this.pageNumber !== 1)
            this.updatePage(this.pageNumber - 1)
    }

    nextPage = () => {
        if (this.pageNumber !== globalThis.MAX_COUNT)
            this.updatePage(this.pageNumber + 1)
    }
}

class Manager{
    constructor(page) {
        this.page = page || false
        this.loginManager = false
    }

    updatePage(data){
        this.page.updateWidget(data)
        return this
    }

    setPage(page){
        this.page = page || this.main_page
        return this
    }

    setLoginManager(loginManager){
        this.loginManager = loginManager
        return this
    }

    start(){
        if (this.loginManager.checkAuthorize())
            this.updatePage(1)
        else
            this.showAuth(this.loginManager.loginPage)
    }

    showAuth(authPage){
        this.main_page = this.page
        authPage.show()
    }
}

class LoginManager{
    userFactory;
    user;

    constructor(userFactory, md5) {
        this.md5 = md5
        this.userFactory = userFactory;
        this.loginPage = false
        this.is_authorized = false
    }

    tryAuthorize(data){
        let xmlHttp = getXmlHttp();
        xmlHttp.open("POST", '/auth', false)
        let formData = new FormData()
        formData.append("name", data.name)
        formData.append("password", this.md5(data.password))
        xmlHttp.send(formData);
        const response = JSON.parse(xmlHttp.responseText);
        if (response.authorized){
            this.setUser(response.Name, response.Role)
            this.manager.updatePage(1)
        }
    }

    setUser(name, role){
        this.is_authorized = true
        this.user = this.userFactory.makeUser(name, role)
    }

    checkAuthorize(){
        let name = getCookie("name")
        if (name == null)
            return false
        let xmlHttp = getXmlHttp();
        xmlHttp.open("POST", '/check', false)
        let formData = new FormData()
        formData.append("name", name)
        xmlHttp.send(formData)
        let answer = JSON.parse(xmlHttp.responseText).result
        console.log(answer)
        if (answer){
            this.setUser(name, +getCookie("role"))
        } else{
            this.clearUser()
        }
        return answer
    }

    setManager(manager){
        this.manager = manager
    }

    setPage(loginPage){
        this.loginPage = loginPage
        return this
    }

    clearUser() {
        this.user = undefined
        this.is_authorized = false
        let xmlHttp = getXmlHttp();
        xmlHttp.open("GET", '/logout', false)
        xmlHttp.send()
        this.loginPage.show()
    }
}

class AuthorizeFormFactory{
    makeWidget(manager){
        return new AuthorizeForm(manager)
    }
}

class AuthorizeForm{
    constructor(manager) {
        this.manager = manager
        console.log(this.manager)
        this.form = document.createElement("div")
    }

    tryAuthorize = () => {
        this.manager.tryAuthorize(this.getFormData())
    }

    generateHTML(){
        let limiter_div = document.createElement("div")
        limiter_div.className = "limiter"
        let container_login = document.createElement("div")
        container_login.className = "container-login100"
        let wrap_div = document.createElement("div")
        wrap_div.className = "wrap-login100 p-l-85 p-r-85 p-t-55 p-b-55"
        this.form.className = "login100-form validate-form flex-sb flex-w"
        this.form.innerHTML = "" +
            "<span class=\"login100-form-title p-b-32\">Авторизация</span>\n" +
            "<span class=\"txt1 p-b-11\">Имя пользователя</span>\n" +
            "<div class=\"wrap-input100 validate-input m-b-36\">\n" +
            "<input class=\"input100\" type=\"text\" id=\"username\" >\n" +
            "<span class=\"focus-input100\"></span>\n" +
            "</div>\n" +
            "<span class=\"txt1 p-b-11\">Пароль</span>\n" +
            "<div class=\"wrap-input100 validate-input m-b-12\">\n" +
            "<input class=\"input100\" type=\"password\" id=\"password\" >\n" +
            "<span class=\"focus-input100\"></span>\n" +
            "</div>"
        let btn_container = document.createElement("div")
        btn_container.className = "container-login100-form-btn"
        let btn = document.createElement("button")
        btn.className = "login100-form-btn"
        btn.addEventListener('click', this.tryAuthorize)
        btn.innerText = "Войти"

        limiter_div.append(container_login)
        container_login.append(wrap_div)
        wrap_div.append(this.form)
        this.form.append(btn_container)
        btn_container.append(btn)

        return limiter_div
    }

    getFormData(){
        return {
            name: document.getElementById("username").value,
            password: document.getElementById("password").value
        }
    }
}

document.addEventListener('DOMContentLoaded', () =>
{
    const deskFactory = new DeskFactory()
    const roleFactory = new RoleFactory()
    const userFactory = new UserFactory(roleFactory)
    const authFactory = new AuthorizeFormFactory()
    const loginManager = new LoginManager(userFactory, CryptoJS.MD5)

    const loginPage = (new PageBuilder(authFactory, loginManager))
        .build()

    const manager = new Manager()

    loginManager.setPage(loginPage)
        .setManager(manager)

    const header = (new HeaderBuilder(LinkBuilder))
        .setBrand("DRT")
        .addLink((new LinkBuilder("Главная")).setClassName("active").build())
        .addLink((new LinkBuilder("Заявки")).build())
        .build()
        .subscribeUserStorage(loginManager)

    const page = (new PageBuilder(deskFactory, manager)
        .addHeader(header)
        .build())

    manager.setPage(page)
        .setLoginManager(loginManager)
        .start()
});
