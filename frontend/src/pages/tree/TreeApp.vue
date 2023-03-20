<template>
  <v-app>
    <v-main>
      <div class="back_ground">
        <div class="container">
          <div class="header">
            <div>
              <a href="/">
                <v-img
                  lazy-src="@/assets/avail_logo.png"
                  max-height="100"
                  max-width="200"
                  src="@/assets/avail_logo.png"
                ></v-img>
              </a>
            </div>
            <nav>
              <router-link to="/">TreeTop</router-link> |
              <router-link to="/root_select">ツリー作成</router-link>
            </nav>
          </div>
          <hr />
          <!-- router-viewにURLと同じ物が表示される bodyに置き換わる -->
          <router-view />
        </div>
      </div>
    </v-main>
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

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
