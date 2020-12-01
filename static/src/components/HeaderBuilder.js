export class HeaderBuilder{
    constructor(linkBuilder){
        this.links = []
        this.linkBuilder = linkBuilder
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

export class Header{
    constructor(headerBuilder){
        this.brand = headerBuilder.brand || false
        this.links = headerBuilder.links
        this.linkBuilder = headerBuilder.linkBuilder
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
        let logout = document.createElement("button")
        logout.className = "dropdown-item"
        logout.onclick = () => this.userStorage.clearUser()
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
        console.log(this.linkBuilder)
        if (user !== undefined) {
            this.userName = user.name
            if (user.role.role !== 0) {
                this.links[2] = this.linkBuilder.make(user.role.tag)
            } else if (this.links.length > 2)
                this.links.pop()

        }
    }
}
