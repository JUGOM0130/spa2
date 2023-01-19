<template>
  <Slide right disableEsc>
    <router-link to="/"><span>Top</span></router-link>
    <router-link to="e_bom"><span>E-BOM</span></router-link>
  </Slide>
</template>

<script>
import { Slide } from "vue3-burger-menu"; // import the CSS transitions you wish to use, in this case we are using `Slide`

export default {
  components: {
    Slide, // Register your component
  },
};
</script>
