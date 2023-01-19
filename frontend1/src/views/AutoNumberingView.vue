<template>
  <div class="container">
    <h1>採番一覧</h1>
    <table class="table">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Number</th>
          <th scope="col">Name</th>
          <th scope="col">備考</th>
          <th scope="col">削除</th>
          <th scope="col">編集</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="d in numlist" :key="d.id">
          <td>{{ d.id }}</td>
          <td>{{ d.number }}</td>
          <td>{{ d.name }}</td>
          <td>{{ d.biko }}</td>
          <td>
            <button
              type="button"
              class="btn btn-outline-danger"
              v-on:click="delete_click()"
            >
              削除
            </button>
          </td>
          <td>
            <button
              type="button"
              class="btn btn-outline-dark"
              v-on:click="henshu_click(d.name)"
            >
              編集
            </button>
          </td>
        </tr>
      </tbody>
    </table>
    <button v-on:click="click">asdf</button>
  </div>
</template>

<script>
//import { ref } from "vue";
//import { useRouter } from "vue-router";
import axios from "axios";
import constant from "../const";

export default {
  data() {
    return {
      temp: [],
      numlist: [
        {
          id: "aa",
          number: 11,
          name: "vv",
          biko: "cc",
        },
      ],
      aaa: "sdfg",
    };
  },
  methods: {
    delete_click: function () {},
    henshu_click: function (id) {
      this.$router.push({ path: `/saiban/${id}` });
    },
    getdata: function () {
      const TO = constant.BACK_END_IP + "/saiban/read";
      const vm = this;
      axios
        .get(TO)
        .then(function (response) {
          let a = response.data.data;
          a.forEach((e) => {
            let o = {
              id: e.id,
              number: e.number,
              name: e.name,
            };
            vm.numlist.push(o);
          });
        })
        .catch((err) => {
          console.log("エラー");
          console.log(err);
        });
      let a = this.temp;
      for (const c of a) {
        console.log(c);
      }
    },
  },
  created() {
    this.getdata();
    //console.log(this.numlist);
  },
  mounted() {},
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
