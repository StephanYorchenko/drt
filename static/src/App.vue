<template>
  <div id="app">
  </div>
</template>

<script>
import {Api} from "@/components/Api";
import {DeskFactory} from "@/components/DeskFactory";
import {RoleFactory} from "@/components/RoleFactory";
import {UserFactory} from "@/components/UserFactory";
import {AuthorizeFormFactory} from "@/components/AuthorizeFormFactory";
import {LoginManager} from "@/components/LoginManager";
import CryptoJS from "crypto-js";
import {PageBuilder} from "@/components/PageBuilder";
import {Manager} from "@/components/Manager";
import {LinkFactory} from "@/components/LinkBuilder";
import {AdminFactory} from "@/components/AdminFactory";
import {TableFactory} from "@/components/TableFactory";
import {Header} from "@/components/HeaderBuilder";


function register_container() {
  const awilix = require("awilix")
  const container = awilix.createContainer({
    injectionMode: awilix.InjectionMode.CLASSIC,
  })

  container.register({
    api: awilix.asClass(Api),
    brand: awilix.asValue("DRT"),
    linkFactory: awilix.asValue(new LinkFactory()),
    tableFactory: awilix.asValue(new TableFactory()),
    deskFactory: awilix.asClass(DeskFactory),
    roleFactory: awilix.asClass(RoleFactory),
    userFactory: awilix.asClass(UserFactory),
    adminFactory: awilix.asClass(AdminFactory),
    authFactory: awilix.asClass(AuthorizeFormFactory),
    widgets: awilix.asFunction((deskFactory, adminFactory) => [deskFactory, adminFactory]),
    manager: awilix.asClass(Manager),
    md5: awilix.asValue(CryptoJS.MD5),
    loginManager: awilix.asClass(LoginManager).singleton(),
    loginPage: awilix.asFunction((authFactory) => (new PageBuilder([authFactory])).build()),
    header: awilix.asClass(Header),
    page: awilix.asFunction((widgets, header) => (new PageBuilder(widgets))
        .addHeader(header)
        .build()) ,
  })
  return container
}

export default {
  name: 'App',
  mounted(){
    const container = register_container()
    document.addEventListener("DOMContentLoaded", () => {
          container.resolve('manager').start()
    })
  }
}
</script>

<style>
@import "assets/style.css";
@import "assets/util.css";
</style>