import React from "react";

export class AnnouncementFactory {
    makeAnnouncement(props) {
        return (
            <div className='card announcement'>
                <div className='card-body'>
                    <h4 className='card-title'>{props.title}</h4>
                    <p className='card-text'>{props.text}</p>
                    <div className="card-footer text-muted">{props.date}</div>
                </div>
            </div>
        )
    }
}