<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

/**
 * 変数宣言
 */
const router = useRouter();
let items = ref([{}]);

/**
 * 一覧取得
 */
const getList = () => {
  const TO = process.env.VUE_APP_BACKEND_IP.concat("/torihiki/getListOfName");
  axios
    .get(TO)
    .then((res) => {
      items.value = res.data.result.data;
    })
    .catch((err) => {
      console.log(err);
    });
};

/**
 * マウント時処理
 */
onMounted(() => {
  getList();
});
</script>

<template>
  <div>
    <v-btn
      variant="outlined"
      color="#00F"
      @click="router.push('/torihiki_regist')"
      >登録</v-btn
    >
    <v-table>
      <thead>
        <tr>
          <th class="text-left">取引先名</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.tid">
          <td>{{ item.tname1 }}</td>
        </tr>
      </tbody>
    </v-table>
  </div>
</template>
