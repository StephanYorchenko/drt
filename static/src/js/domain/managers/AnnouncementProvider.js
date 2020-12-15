export class AnnouncementProvider {
    constructor(api, deskFactory, loginManager) {
        this.loginManager = loginManager
        this.api = api;
        this.deskFactory = deskFactory;
        this.MAX_COUNT = 1
    }

    getAnnouncementsData(page) {
        const data = this.api.get("/api/announcement?page_number=" + page)
        this.MAX_COUNT = +data.count
        return data.announcements
    }

    previousPage(n) {
        this.announcementPage.contentUpdate(this.updateContent(n))
    }

    nextPage(n) {
        this.announcementPage.contentUpdate(this.updateContent(n))
    }

    updateContent(number) {
        let data = this.getAnnouncementsData(number || 1)
        return this.deskFactory.makeWidget(number || 1, data, this).generateHTML()
    }

    setPage(page) {
        this.announcementPage = page
        return this.updateContent()
    }

    sendNew(data){
        let form = document.forms.newAnnouncement
        let formData = new FormData()
        formData.append("title", data.title)
        formData.append("text", data.text)
        formData.append("username", this.loginManager.user.name)
        this.api.post('/api/announcement', formData)
        form.reset()
    }
}