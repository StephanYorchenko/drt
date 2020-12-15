import {Api} from "./domain/api/ApiProvider";
import {DeskFactory} from "./application/widgets/AnnouncementDeskFactory";
import {AnnouncementFactory} from "./application/widgets/AnnouncementFactory";
import {App} from "./App";
import {UserFactory} from "./domain/managers/User";
import {RoleFactory} from "./domain/managers/Role";
import {LoginManager} from "./domain/managers/LoginManager";
import {AuthorizeFormFactory} from "./application/pages/LoginPage";
import {PrivateRouteFactory} from "./application/components/PrivateRoute";
import {AdminFactory} from "./application/pages/AdminPage";
import {TableFactory} from "./application/widgets/AdminTableFactory";
import {AnnouncementDeskPage} from "./application/pages/AnnouncementDeskPage";
import {AnnouncementProvider} from "./domain/managers/AnnouncementProvider";
import {AdminProvider} from "./domain/managers/AdminProvider";
import {NavBar} from "./application/widgets/NavBar"
import {RequestPage} from "./application/pages/RequestPage";

import React from "react";
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Redirect } from "react-router-dom";

import axios from 'axios'
import CryptoJS from "crypto-js"
import Cookies from "js-cookie"


import {Modal} from "react-bootstrap";
import Button from "react-bootstrap/Button"
import {RequestFactory} from "./application/widgets/RequestFactory";
import {RequestProvider} from "./domain/managers/RequestProvider";
import {RequestDeskFactory} from "./application/widgets/RequestDeskFactory";



export function register_container() {
    const awilix = require("awilix")
    const container = awilix.createContainer({
        injectionMode: awilix.InjectionMode.CLASSIC,
    })
    container.register({
        //api providers
        api: awilix.asClass(Api),
        request: awilix.asValue(axios),
        md5: awilix.asValue(CryptoJS.MD5),
        cookie: awilix.asValue(Cookies),
        redirectPage: awilix.asValue((dest, redirect) => <Redirect to='/' />),

        //react components
        route: awilix.asValue(Route),
        router: awilix.asValue(Router),
        redirect: awilix.asValue(Redirect),
        privateRoute: awilix.asFunction((loginManager, privateRouteFactory) =>
            (props) => privateRouteFactory.make(() => loginManager.checkAuthorize(), '/login')(props)),
        loginRoute: awilix.asFunction((route) => route),
        adminRoute: awilix.asFunction((loginManager, privateRouteFactory) =>
            privateRouteFactory.make(() => loginManager.isAdmin(), '/')),

        //data providers
        announcementProvider: awilix.asClass(AnnouncementProvider),
        requestProvider: awilix.asClass(RequestProvider),
        adminProvider: awilix.asClass(AdminProvider),

        //pages
        mainPageView: awilix.asValue(AnnouncementDeskPage),
        loginPage: awilix.asFunction((authFormFactory) => authFormFactory.makeWidget().render()),
        adminPage: awilix.asFunction((adminFactory) => () => adminFactory.makeWidget().generateHTML()),
        requestPage: awilix.asValue(RequestPage),

        //managers
        loginManager: awilix.asClass(LoginManager),

        //pages factories
        adminFactory: awilix.asClass(AdminFactory),


        //widgets
        adminTableFactory: awilix.asClass(TableFactory),
        deskFactory: awilix.asClass(DeskFactory),
        announcementFactory: awilix.asClass(AnnouncementFactory),
        authFormFactory: awilix.asClass(AuthorizeFormFactory),
        navbar: awilix.asValue(NavBar),
        requestFactory: awilix.asClass(RequestFactory),
        requestDeskFactory: awilix.asClass(RequestDeskFactory),

        //bootstrap-components
        modal: awilix.asValue(Modal),
        button: awilix.asValue(Button),

        //domain
        userFactory: awilix.asClass(UserFactory),
        roleFactory: awilix.asClass(RoleFactory),
        role: awilix.asFunction((roleFactory) => (name) => roleFactory.makeRole(0).getIdByName(name)),
        roleList: awilix.asFunction((roleFactory) => roleFactory.makeRole(0).Roles),

        //components factories
        privateRouteFactory: awilix.asClass(PrivateRouteFactory),

        // application
        app: awilix.asClass(App).singleton(),
        start: awilix.asFunction((app) =>
              ReactDOM.render(<app.Render/>, document.getElementById('root'))),
    })
    return container
}