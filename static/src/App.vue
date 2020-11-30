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
import {LinkBuilder} from "@/components/LinkBuilder";

export default {
  name: 'App',
  mounted(){
    const awilix = require('awilix')
    const container = awilix.createContainer({
      injectionMode: awilix.InjectionMode.PROXY
    })

    container.register({
      api: awilix.asClass(Api)
    })

    const api = new Api()
    const deskFactory = new DeskFactory(container.resolve("api"))
    const roleFactory = new RoleFactory()
    const userFactory = new UserFactory(roleFactory)
    const authFactory = new AuthorizeFormFactory()
    const manager = new Manager()
    const loginManager = (new LoginManager(userFactory, CryptoJS.MD5, api))
        .setManager(manager)

    const loginPage = (new PageBuilder(authFactory, loginManager))
        .build()

    loginManager.setPage(loginPage)

    const header = (new HeaderBuilder(LinkBuilder))
        .setBrand("DRT")
        .addLink((new LinkBuilder("Главная")).setClassName("active").build())
        .addLink((new LinkBuilder("Заявки")).build())
        .build()
        .subscribeUserStorage(loginManager)

    const page = (new PageBuilder(deskFactory, manager))
        .addHeader(header)
        .build()

    document.addEventListener("DOMContentLoaded", () => {
      manager.setPage(page)
          .setLoginManager(loginManager)
          .start()
    })
  }
}
</script>

<style>
@import "assets/style.css";
@import "assets/util.css";
</style>
