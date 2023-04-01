
<script setup>
import { ref } from "vue";

let drawer = ref(false);
let items = [
  { title: "コード", icon: "mdi-folder", link: "/code#/" },
  { title: "ツリー", icon: "mdi-folder", link: "/tree#/" },
];

const menuclick = (item) => {
  window.location.href = item.link;
};
const logoclick = () => {
  window.location = "/";
};
</script>
<template>
  <v-app>
    <v-layout>
      <v-app-bar color="teal-darken-1">
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <v-img
          max-height="100"
          max-width="200"
          src="@/assets/avail_logo.png"
          @click="logoclick"
        ></v-img>

        <!-- ナビゲーションバー_コードメニューボタン -->
        <v-menu>
          <template v-slot:activator="{ props }">
            <v-btn color="white" v-bind="props">メニュー</v-btn>
          </template>
          <v-list>
            <v-list-item
              v-for="(item, index) in items"
              :key="index"
              :value="index"
              @click="menuclick(item)"
            >
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>
      <v-navigation-drawer v-model="drawer" absolute temporary>
        <v-list lines="one">
          <v-list-item
            prepend-avatar="https://randomuser.me/api/portraits/men/78.jpg"
            title="UserName"
            subtitle="avail@gmail.com"
          ></v-list-item>
        </v-list>
        <v-divider inset></v-divider>
        <v-list :lines="false" density="compact" nav>
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            :value="item"
            active-color="primary"
          >
            <template v-slot:prepend>
              <v-icon :icon="item.icon"></v-icon>
            </template>

            <v-list-item-title v-text="item.title"></v-list-item-title>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
      <v-main>
        <div class="my-3">
          <v-container>
            <!-- router-viewにURLと同じ物が表示される bodyに置き換わる -->
            <router-view />
          </v-container>
        </div>
      </v-main>
    </v-layout>
  </v-app>
</template>



<style scoped>
.back_ground {
  background-color: rgb(215, 215, 215);
  min-height: 100vh;
}
.header_icon {
  width: 15%;
  margin-bottom: 10px;
  margin-top: 10px;
}
</style>
