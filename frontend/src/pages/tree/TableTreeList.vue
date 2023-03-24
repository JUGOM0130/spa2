<script setup>
import constant from "@/const";
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

let tree_roots = ref([]);
const router = useRouter();

/**
 * 一覧取得処理
 */
const getList = () => {
  const TO = constant.BACK_END_IP + "/tree/get_tree_list";
  axios
    .get(TO)
    .then((res) => {
      const a = res.data.result.data;
      a.forEach((e) => {
        tree_roots.value.push({ name: e.tree_id });
      });
    })
    .catch((err) => {
      console.log(err);
    });
};
/**
 * 編集画面へ遷移
 * @param {event} e
 */
const edit = (e) => {
  const select_id = e.currentTarget.dataset["id"];
  router.push({ query: { tree_id: select_id }, path: "/table_tree" });
};
/**
 * 削除処理
 * @param {event} e
 */
const deleteClick = (e) => {
  const TO = constant.BACK_END_IP + "/tree/delete/";
  const select_id = e.currentTarget.dataset["id"];

  axios.get(TO + select_id).then((res) => {
    const status = res.data.result.status;
    if (status == "OK") {
      router.go({ path: router.currentRoute.path });
    }
  });
};
/**
 * 登録画面へ遷移
 */
const registClick = () => {
  router.push("/root_select");
};
onMounted(() => {
  getList();
});
</script>
<template>
  <div>
    <v-container>
      <v-row justify="end">
        <v-btn
          @click="registClick()"
          variant="outlined"
          color="#00F"
          class="m-1"
        >
          <v-icon icon=" mdi-plus-box-multiple"></v-icon>
          ツリー登録
        </v-btn>
      </v-row>
    </v-container>

    <v-table>
      <thead>
        <tr>
          <th class="text-left">ツリー名</th>
          <th class="text-left row_icon">編集</th>
          <th class="text-left row_icon">削除</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in tree_roots" :key="item.name">
          <td>{{ item.name }}</td>
          <td class="text-left row_icon">
            <!-- data-hogeという属性を宣言すると$eventでhogeとして値が取得できる -->
            <v-icon
              icon="mdi-square-edit-outline"
              :data-id="item.name"
              @click="edit($event)"
              color="blue"
            ></v-icon>
          </td>
          <td class="text-left row_icon">
            <v-icon
              icon="mdi-trash-can-outline"
              :data-id="item.name"
              @click="deleteClick($event)"
              color="red"
            ></v-icon>
          </td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>
<style scoped lang="scss">
.row_icon {
  width: 100px;
}
</style>
