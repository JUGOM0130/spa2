<template>
  <div class="back_ground">
    <BurgerMenu></BurgerMenu>
    <div class="container">
      <div class="header">
        <div>
          <img src="./assets/header_logo5.png" alt="logo" class="header_icon" />
        </div>
        <nav>
          <router-link to="/">root</router-link> |
          <router-link to="/e_bom">E-BOM</router-link> |
          <router-link to="/code_list">製品コード一覧</router-link>
        </nav>
      </div>
      <hr />
      <!-- router-viewにURLと同じ物が表示される bodyに置き換わる -->
      <router-view />
    </div>
  </div>
</template>


<script>
import BurgerMenu from "./views/BurgerMenu.vue";
export default {
  components: {
    BurgerMenu,
  },
};
</script>

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
