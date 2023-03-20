<script setup>
import { useRoute } from "vue-router";
import TableTree from "./TableTree.vue";

const route = useRoute();
const id = route.query.number;
const name = route.query.name;
const root = [{ id: id, name: name, lv: "1", parentId: "0", order: "" }];
</script>
<template>
  <div>
    <TableTree :root="root"></TableTree>
  </div>
</template>

<style>
.yoko_scroll_outer {
  padding: 5px;
  border: 1px;
  border-style: solid;
  margin-bottom: 5px;
}
.table_container {
  padding: 5px;
  border: 1px;
  border-style: solid;

  margin-bottom: 5px;
}
</style>
