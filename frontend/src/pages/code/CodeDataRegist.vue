<template>
  <div class="container">
    <h1>登録</h1>
    <form>
      <input type="hidden" name="pid" v-model="pid" />
      <input type="hidden" name="pcd" v-model="pcd" />
      <input type="hidden" name="pctid" v-model="pctid" />
      <div class="mb-3">
        <label for="pcd" class="form-label">コード</label>
        <input
          type="text"
          class="form-control"
          id="pcd"
          v-model="pcd"
          disabled
        />
      </div>
      <div class="row g-2">
        <div class="col mb-3">
          <label for="pname" class="form-label">名称</label>
          <input type="text" class="form-control" id="pname" v-model="pname" />
        </div>
        <div class="col mb-3">
          <label for="ppname" class="form-label">製品名称</label>
          <input
            type="text"
            class="form-control"
            id="ppname"
            v-model="ppname"
          />
        </div>
      </div>
      <div class="row g-3">
        <div class="col mb-3">
          <label for="prevision" class="form-label">版数（リビジョン）</label>
          <input
            type="text"
            class="form-control"
            id="prevision"
            v-model="prevision"
          />
        </div>
        <div class="col mb-3">
          <label for="pvendor" class="form-label">手配先</label>
          <select
            id="pvendor"
            class="form-select"
            aria-label="Default select example"
            v-model="pvendor"
          >
            <option selected>-</option>
            <option value="1">株式会社AVAIL</option>
            <option value="2">しまの</option>
            <option value="3">くれは</option>
          </select>
        </div>
        <div class="col mb-3">
          <label for="ptype" class="form-label">型式</label>
          <input
            type="text"
            id="ptype"
            name="ptype"
            class="form-control"
            v-model="ptype"
          />
        </div>
      </div>
      <div class="row g-3">
        <div class="col mb-3">
          <label for="pmaterial" class="form-label">材質</label>
          <input
            type="text"
            class="form-control"
            id="pmaterial"
            name="pmaterial"
            v-model="pmaterial"
          />
        </div>
        <div class="col mb-3">
          <label for="pio" class="form-label">内外策</label>
          <select
            id="pio"
            name="pio"
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
      </div>
      <div class="row g-4">
        <div class="mb-3 col">
          <label for="pmtlmain_cost" class="form-label">主要材料費</label>
          <input
            type="text"
            class="form-control"
            id="pmtlmain_cost"
            v-model="pmtlmain_cost"
          />
        </div>
        <div class="mb-3 col">
          <label for="pmaterialsub_cost" class="form-label">補助材料費</label>
          <input
            type="text"
            class="form-control"
            id="pmaterialsub_cost"
            v-model="pmtlsub_cost"
          />
        </div>
        <div class="mb-3 col">
          <label for="pprocdict_cost" class="form-label">外注加工費</label>
          <input
            type="text"
            class="form-control"
            id="pprocdict_cost"
            v-model="pprocdict_cost"
          />
        </div>
        <div class="mb-3 col">
          <label for="pprocsub_cost" class="form-label">直接労務費</label>
          <input
            type="text"
            class="form-control"
            id="pprocsub_cost"
            v-model="pprocsub_cost"
          />
        </div>
      </div>
      <div class="row row-cols-auto justify-content-end">
        <div class="col">
          <button type="button" class="btn btn-primary" @click="shori">
            登録・更新
          </button>
        </div>
      </div>
    </form>
  </div>
</template>
  <script>
import axios from "axios";
import CONST from "../../const";
export default {
  data() {
    return {
      pid: 0,
      pcid: 0,
      pcd: "",
      pname: "",
      ppname: "",
      prevision: "",
      pvendor: "",
      ptype: "",
      pmaterial: "",
      pio: "",
      pmtlmain_cost: 0,
      pmtlsub_cost: 0,
      pprocdict_cost: 0,
      pprocsub_cost: 0,
    };
  },
  methods: {
    shori: function () {
      if (this.pid != 0) {
        this.update();
      } else {
        this.regist();
      }
    },
    regist: function () {
      const TO = CONST.BACK_END_IP + "/parts/regist";

      console.log(this.$data);
      axios
        .post(TO, this.$data)
        .then((res) => {
          console.log(res);
          this.$router.push("/code_list");
        })
        .catch((e) => {
          console.log(e);
        });
    },
    update: function () {
      const TO = CONST.BACK_END_IP + "/parts/update";
      console.log(this.$data);
      axios
        .post(TO, this.$data)
        .then((res) => {
          console.log(res);
          this.$router.push("/code_list");
        })
        .catch((e) => {
          console.log(e);
        });
    },
    getPartsData: function () {
      const TO = CONST.BACK_END_IP + "/parts/read/" + this.pid;
      axios
        .get(TO, this.$data)
        .then((res) => {
          let dt = res.data;
          this.pcid = dt.pcid;
          this.pcd = dt.pcd;
          this.pname = dt.pname;
          this.ppname = dt.ppname;
          this.prevision = dt.prevision;
          this.pvendor = dt.pvendor;
          this.ptype = dt.ptype;
          this.pmaterial = dt.pmaterial;
          this.pio = dt.pio;
          this.pmtlmain_cost = dt.pmtlmain_cost;
          this.pmtlsub_cost = dt.pmtlsub_cost;
          this.pprocdict_cost = dt.pprocdict_cost;
          this.pprocsub_cost = dt.pprocsub_cost;
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  mounted: function () {
    this.pcid = this.$store.state.id;
    this.pcd = this.$store.state.cd;
    this.pid = this.$store.state.parts_id;
    if (this.pid != 0) {
      this.getPartsData();
    }
  },
};
</script>
