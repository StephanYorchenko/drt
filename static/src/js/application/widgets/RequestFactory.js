import React from "react";

export class RequestFactory {
    makeRequest(props) {
        return (
            <div className='card announcement'>
                <form className='card-body' onSubmit={(event) => props.provider.Approve(this, event)}>
                    <span hidden={true} id="__id">{props.id}</span>
                    <h4 className='card-title'>{props.topic}</h4>
                    <p className='card-text'>{props.comment}</p>
                    <div className="card-footer text-muted">{props.user}{props.date}</div>
                    <button type='submit' className="btn btn-primary btn-light-green" >Принять</button>
                </form>
            </div>
        )
    }
}