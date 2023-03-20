<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import constant from "@/const";
const router = useRouter();
let items = ref([
  { pid: "1", name: "VELLFIRE" },
  { pid: "2", name: "RANDCRUISER" },
  { pid: "3", name: "HIACE" },
]);
let select_item = ref({ pid: "1", name: "VELLFIRE" });
const nextScreen = () => {
  router.push({
    path: "/tree_create",
    query: {
      number: select_item.value.pid,
      name: select_item.value.name,
    },
  });
};
onMounted(() => {
  const TO = constant.BACK_END_IP + "/tree/get_root_list";
  axios
    .get(TO)
    .then((res) => {
      const alias = res.data.result.data;
      items = ref([]);
      console.log(res);
      alias.forEach((e) => {
        items.value.push({ pid: e.pid, name: e.pcd });
      });
      select_item.value = {
        pid: items.value[0].pid,
        name: items.value[0].name,
      };
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>

<template>
  <div>
    <v-select
      label="製品"
      v-model="select_item"
      :items="items"
      item-title="name"
      item-value="pid"
      :hint="`${select_item.pid}, ${select_item.name}`"
      persistent-hint
      return-object
    ></v-select>
    <v-btn @click="nextScreen">次へ</v-btn>
  </div>
</template>


<style scoped>
</style>
