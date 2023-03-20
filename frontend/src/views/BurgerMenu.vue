<template>
  <Slide right disableEsc>
    <a href="/">Top</a>
    <a href="/code"></a>
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
