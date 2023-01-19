<template>
  <div class="container">
    <h1>登録</h1>
    <form>
      <div class="mb-3">
        <label for="id" class="form-label">ID</label>
        <input type="text" class="form-control" id="id" v-model="id" />
        <div id="id" class="form-text">ID名はテキストです</div>
      </div>
      <div class="mb-3">
        <label for="number" class="form-label">Index</label>
        <input type="text" class="form-control" id="number" v-model="number" />
        <div id="number" class="form-text">登録開始番号を入力</div>
      </div>
      <div class="mb-3">
        <label for="name" class="form-label">採番名</label>
        <input type="text" class="form-control" id="name" v-model="name" />
      </div>
      <div class="mb-3">
        <label for="biko" class="form-label">備考</label>
        <input type="text" class="form-control" id="biko" v-model="biko" />
      </div>
      <button type="button" class="btn btn-primary" v-on:click="regist()">
        登録
      </button>
    </form>
  </div>
</template>

<script>
//import { ref } from "vue";
//import { useRouter } from "vue-router";
import axios from "axios";
import { onMounted } from "vue";
import constant from "../const";

export default {
  setup() {
    const st = this.$route.params;
    onMounted(() => {
      console.log(st);
    });
  },
  data: function () {
    return {
      id: "",
      number: 1,
      name: "",
      biko: "",
    };
  },
  methods: {
    regist: function () {
      const TO = constant.BACK_END_IP + "/saiban/create";
      console.log(TO);
      const DATA = {
        id: this.id,
        number: this.number,
        name: this.name,
        biko: this.biko,
      };
      axios
        .post(TO, DATA)
        .then(function (response) {
          console.log(response);
        })
        .catch((err) => {
          console.log("エラー");
          console.log(err);
        });
    },
  },
};
/*
<script setup>
const id = ref("");
const number = ref(1);
const name = ref("");
const biko = ref("");
const router = useRouter();

function regist() {
  const TO = constant.BACK_END_IP + "/saiban/create";
  console.log(TO);
  const DATA = {
    id: id.value,
    number: number.value,
    name: name.value,
    biko: biko.value,
  };
  axios
    .post(TO, DATA)
    .then(function (response) {
      console.log(response);
      router.go(router.currentRoute.value);
    })
    .catch((err) => {
      console.log("エラー");
      console.log(err);
    });
  return { id, number, name, biko, regist };
}

function delete(){
  const TO = constant.BACK_END_IP + "/saiban/delete";
  console.log(TO);
  const DATA = {
    id: id.value,
    number: number.value,
    name: name.value,
    biko: biko.value,
  };
  axios
    .post(TO, DATA)
    .then(function (response) {
      console.log(response);
      router.go(router.currentRoute.value);
    })
    .catch((err) => {
      console.log("エラー");
      console.log(err);
    });
  return { id, number, name, biko, regist };

}
*/
</script>
