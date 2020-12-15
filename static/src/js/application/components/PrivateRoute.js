import {Redirect, Route} from "react-router-dom";
import React from "react";


export class PrivateRouteFactory{
   make(checkUser, dest){
       return ({ component: Component, handleChildFunc, ...rest }) => {
           const user = checkUser()
           return <Route {...rest} render={(props) => (
               user
                   ? <Component {...props} user={user} handleChildFunc={handleChildFunc}/>
                   : <Redirect to={dest} />
           )}
           />
       }
   }
}

export class NavRoute{
    make(header){
        return ({exact, path, component: Component}) => (
            <Route exact={exact} path={path} render={
                (props) => (
                    <div>
                        {/*<header />*/}
                        <Component {...props}/>
                    </div>)
            }/>
            )
    }
}
