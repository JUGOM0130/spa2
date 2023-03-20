<script setup></script>
<template>
  <v-app>
    <v-main class="back_ground">
      <div class="container">
        <div class="header">
          <div>
            <a href="/">
              <v-img
                lazy-src=""
                max-height="100"
                max-width="200"
                src="@/assets/avail_logo.png"
              ></v-img>
            </a>
          </div>
          <nav>
            <router-link to="/">コード系メニューTop</router-link> |
            <router-link to="/">コード採番</router-link> |
            <router-link to="/">コード一覧</router-link>
          </nav>
        </div>
        <hr />
        <!-- router-viewにURLと同じ物が表示される bodyに置き換わる -->
        <router-view />
      </div>
    </v-main>
  </v-app>
</template>
