<script setup>
import { ref } from "vue";
import axios from "axios";

let data = ref({});
data.value.tname1 = "";
data.value.tname2 = "";
data.value.zipcd = "";
data.value.address1 = "";
data.value.address2 = "";
data.value.address3 = "";
data.value.address4 = "";
data.value.tel1 = "";

/**
 * 登録処理
 */
const regist = () => {
  const TO = process.env.VUE_APP_BACKEND_IP.concat("/torihiki/regist");
  axios
    .post(TO, data.value)
    .then((res) => {
      console.log(res);
    })
    .then((err) => {
      console.log(err);
    });
};
</script>
<template>
  <div>
    <v-text-field label="取引先名" v-model="data.tname1"></v-text-field>
    <v-text-field label="取引先名(カナ)" v-model="data.tname2"></v-text-field>
    <v-text-field label="郵便番号" v-model="data.zipcd"></v-text-field>
    <v-text-field label="住所1(県)" v-model="data.address1"></v-text-field>
    <v-text-field
      label="住所2(市区町村)"
      v-model="data.address2"
    ></v-text-field>
    <v-text-field label="住所3(番地)" v-model="data.address3"></v-text-field>
    <v-text-field
      label="住所4(アパートビル名)"
      v-model="data.address4"
    ></v-text-field>
    <v-text-field label="電話番号" v-model="data.tel1"></v-text-field>
    <v-btn variant="outlined" color="black" @click="regist">登録</v-btn>
  </div>
</template>
