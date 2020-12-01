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
import {HeaderBuilder} from "@/components/HeaderBuilder";
import {LinkFactory} from "@/components/LinkBuilder";


function register_container() {
  const awilix = require("awilix")
  const container = awilix.createContainer({
    injectionMode: awilix.InjectionMode.CLASSIC,
  })

  container.register({
    api: awilix.asClass(Api),
    linkFactory: awilix.asValue(new LinkFactory()),
    deskFactory: awilix.asClass(DeskFactory),
    roleFactory: awilix.asClass(RoleFactory),
    userFactory: awilix.asClass(UserFactory),
    authFactory: awilix.asClass(AuthorizeFormFactory),
    manager: awilix.asClass(Manager),
    md5: awilix.asValue(CryptoJS.MD5),
    loginManager: awilix.asClass(LoginManager).singleton(),
    loginPage: awilix.asFunction((authFactory) => (new PageBuilder(authFactory)).build()),
    header: awilix.asFunction((linkFactory, loginManager) => (new HeaderBuilder(linkFactory))
        .setBrand("DRT")
        .addLink(linkFactory.make("Главная", "active"))
        .addLink(linkFactory.make("Заявки"))
        .build()
        .subscribeUserStorage(loginManager)),
    page: awilix.asFunction((deskFactory, header) => (new PageBuilder(deskFactory))
        .addHeader(header)
        .build()),
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