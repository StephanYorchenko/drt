export class DeskFactory {
    constructor(api) {
        this.api = api
    }
    makeWidget(manager, pageNumber){
        if (pageNumber === undefined) pageNumber = 1;
        let data = this.getAnnouncementsData(pageNumber)
        let announcements = this.makeAnnouncements(data)
        return new AnnouncementDesk(announcements, pageNumber, manager, this.api)
    }

    getAnnouncementsData(page) {
        let xmlHttp = this.api.getXmlHttp();
        xmlHttp.open("GET", '/api/get_count?page_number=' + page, false);
        xmlHttp.send()
        const data = JSON.parse(xmlHttp.responseText)
        this.api.MAX_COUNT = +data.count
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
    constructor(announcements, pageNumber, manager, api){
        this.api = api
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
        if (this.pageNumber !== this.api.MAX_COUNT)
            this.updatePage(this.pageNumber + 1)
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

