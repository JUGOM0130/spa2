<template>
  <div class="back">
    <BurgerMenu></BurgerMenu>
    <div class="container">
      <nav>
        <h1>メニュー</h1>
        <router-link to="/">root</router-link> |
        <router-link to="/e_bom">E-BOM</router-link>
      </nav>
      <hr />
      <router-view />
    </div>
  </div>
</template>

<style scoped>
.back {
  background-color: rgb(215, 215, 215);
  min-height: 100vh;
}
</style>

<script>
import BurgerMenu from "./views/BurgerMenu.vue";
export default {
  components: {
    BurgerMenu,
  },
};
</script>
