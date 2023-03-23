<script setup>
import constant from "@/const";
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

let tree_roots = ref([]);
const router = useRouter();
const getList = () => {
  const TO = constant.BACK_END_IP + "/tree/get_tree_list";
  axios
    .get(TO)
    .then((res) => {
      console.log(res);
      const a = res.data.result.data;
      a.forEach((e) => {
        tree_roots.value.push({ name: e.tree_id });
      });
    })
    .catch((err) => {
      console.log(err);
    });
};
const edit = (e) => {
  const select_id = e.currentTarget.dataset["id"];
  router.push({ query: { tree_id: select_id }, path: "/table_tree" });
};
onMounted(() => {
  getList();
});
</script>
<template>
  <v-table>
    <thead>
      <tr>
        <th class="text-left">ツリー名</th>
        <th class="text-left">編集</th>
        <th class="text-left">削除</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="item in tree_roots" :key="item.name">
        <td>{{ item.name }}</td>
        <td class="text-left">
          <v-btn
            :data-id="item.name"
            variant="outlined"
            color="blue"
            @click="edit($event)"
            >編集</v-btn
          >
        </td>
        <td class="text-left">
          <v-btn variant="outlined" color="red">削除</v-btn>
        </td>
      </tr>
    </tbody>
  </v-table>
</template>
