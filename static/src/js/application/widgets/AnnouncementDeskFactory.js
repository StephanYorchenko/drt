import React from 'react'

export class DeskFactory {
    constructor(announcementFactory) {
        this.announcementFactory = (props) => announcementFactory.makeAnnouncement(props)
        this.name = "Главная"

    }
    makeWidget(pageNumber, data, provider){
        let announcements = this.makeAnnouncements(data)
        return new AnnouncementDesk(announcements, pageNumber, provider)
    }

    *makeAnnouncements(data){
        for (let announcement of data){
            yield <this.announcementFactory text={announcement.text} date={announcement.date} title={announcement.title}/>
        }
    }
}

class AnnouncementDesk{
    constructor(announcements, pageNumber, provider){
        this.announcements = [...announcements]
        this.pageNumber = pageNumber
        this.provider = provider
    }

    generateHTML() {
        return (
            <div>
                <div id="card-container">
                    { this.announcements }
                </div>
                <footer>
                    <nav className="horizontal-centered">
                        <ul className="pagination announcement-nav">
                            <li><button onClick={() => this.previousPage(this.pageNumber, this.provider)} className="page-link">Previous</button></li>
                            <li><button className="page-link">{this.pageNumber}</button></li>
                            <li><button onClick={() => this.nextPage(this.pageNumber, this.provider)} className="page-link">Next</button></li>
                        </ul>
                    </nav>
                </footer>
            </div>
        )
    }

    previousPage(pn, provider) {
        console.log(pn, provider.MAX_COUNT)
        if (pn !== 1)
            provider.previousPage(pn - 1)
    }

    nextPage(pn, provider) {
        console.log(pn, provider.MAX_COUNT)
        if (pn !== provider.MAX_COUNT)
            provider.nextPage(pn + 1)
    }
}