<template>
  <div class="container">
    <h1>登録</h1>
    <form>
      <div class="mb-3">
        <label for="shain_cd" class="form-label">コード</label>
        <input type="text" class="form-control" id="shain_cd" v-model="pcd" />
      </div>
      <div class="mb-3">
        <label for="shain_cd" class="form-label">名称</label>
        <input type="text" class="form-control" id="shain_cd" v-model="pname" />
      </div>
      <div class="mb-3">
        <label for="shain_cd" class="form-label">製品名称</label>
        <input
          type="text"
          class="form-control"
          id="shain_cd"
          v-model="ppname"
        />
      </div>
      <div class="mb-3">
        <label for="first_name" class="form-label">版数（リビジョン）</label>
        <input
          type="text"
          class="form-control"
          id="first_name"
          v-model="prevision"
        />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">手配先</label>
        <select
          class="form-select"
          aria-label="Default select example"
          v-model="pvendor"
        >
          <option selected>-</option>
          <option value="1">株式会社AVAIL</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">型式</label>
        <input
          type="text"
          class="form-control"
          id="last_name"
          v-model="ptype"
        />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">材質</label>
        <input
          type="text"
          class="form-control"
          id="last_name"
          v-model="pmaterial"
        />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">内外策</label>
        <select
          class="form-select"
          aria-label="Default select example"
          v-model="pio"
        >
          <option selected>-</option>
          <option value="1">内策</option>
          <option value="2">外策</option>
          <option value="3">内策＋外策</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">主要材料費</label>
        <input
          type="text"
          class="form-control"
          id="last_name"
          v-model="pmtlmain_cost"
        />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">補助材料費</label>
        <input
          type="text"
          class="form-control"
          id="last_name"
          v-model="pmtlsub_cost"
        />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">外注加工費</label>
        <input
          type="text"
          class="form-control"
          id="last_name"
          v-model="pprocdict_cost"
        />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">直接労務費</label>
        <input
          type="text"
          class="form-control"
          id="last_name"
          v-model="pprocsub_cost"
        />
      </div>
      <button type="submit" class="btn btn-primary" v-on:click="regist">
        登録
      </button>
    </form>
  </div>
</template>
<script>
import axios from "axios";
import CONST from "../const";
export default {
  data() {
    return {
      pid: 0,
      pctid: 0,
      pcd: "",
      pname: "A",
      ppname: "A",
      prevision: "A",
      pvendor: "A",
      ptype: "A",
      pmaterial: "A",
      pio: "A",
      pmtlmain_cost: 0,
      pmtlsub_cost: 0,
      pprocdict_cost: 0,
      pprocsub_cost: 0,
    };
  },
  methods: {
    regist: function () {
      const TO = CONST.BACK_END_IP + "/parts/regist";

      console.log(this.$data);
      axios
        .post(TO, this.$data)
        .then((res) => {
          console.log(res);
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  mounted: function () {
    this.pctid = this.$store.state.id;
    this.pcd = this.$store.state.cd;
  },
};
</script>
