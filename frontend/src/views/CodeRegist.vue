<template>
  <div class="container">
    <h1>登録</h1>
    <div class="form-check">
      <input
        class="form-check-input"
        type="radio"
        name="flexRadioDefault"
        id="flexRadioDefault1"
        value="1"
        v-model="ctkind"
        checked
      />
      <label class="form-check-label" for="flexRadioDefault1">
        XXX-AxxxxZ000
      </label>
    </div>
    <div class="form-check">
      <input
        class="form-check-input"
        type="radio"
        name="flexRadioDefault"
        id="flexRadioDefault2"
        value="2"
        v-model="ctkind"
      />
      <label class="form-check-label" for="flexRadioDefault2">
        XXX-AAxxxZ000
      </label>
    </div>
    <div class="form-check">
      <input
        class="form-check-input"
        type="radio"
        name="flexRadioDefault"
        id="flexRadioDefault3"
        value="3"
        v-model="ctkind"
      />
      <label class="form-check-label" for="flexRadioDefault3">
        XX-xxxxZ0
      </label>
    </div>
    <div>
      <!--  [1] XXX-A0001-Z000  -->
      <div class="d-flex flex-row bd-highlight mb-3 justify-content-center">
        <!--  ALD  -->
        <div class="p-2 bd-highlight">
          <input
            type="text"
            class="form-control"
            id="cthead"
            v-model="cthead"
            v-on:blur="getNewNo"
            tabindex="50"
          />
        </div>
        <!--  ハイフン  -->
        <div class="p-2 bd-highlight myset-haba1">
          <label for="shain_cd" class="form-label">-</label>
        </div>
        <!--  英語Number  -->
        <div class="p-2 bd-highlight">
          <input
            type="text"
            v-bind:class="[ctenumber_class]"
            id="ctenumber"
            v-model="ctenumber"
            v-on:blur="getNewNo"
            v-bind:readonly="readonly"
            tabindex="52"
          />
        </div>
        <!--  Number 0000 -->
        <div class="p-2 bd-highlight">
          <input
            type="text"
            class="form-control"
            id="ctnumber"
            readonly
            v-model="ctnumber"
            tabindex="-1"
          />
        </div>
        <!--  Z0000  -->
        <div class="p-2 bd-highlight">
          <input
            type="text"
            class="form-control"
            id="ctfoot"
            v-model="ctfoot"
            v-on:blur="getNewNo"
            tabindex="56"
          />
        </div>
      </div>
    </div>
    <button type="button" class="btn btn-primary" @click="regist">
      Submit
    </button>
  </div>
</template>
<script>
import axios from "axios";
import constant from "../const";

export default {
  data: function () {
    return {
      ctkind: "1",
      cthead: "",
      ctenumber: "",
      ctnumber: "",
      ctfoot: "",
      ctenumber_class: "form-control myset-haba-ctenumber",
      readonly: false,
    };
  },
  methods: {
    regist: function () {
      const TO = constant.BACK_END_IP + "/code_taikei/regist";
      const json = {
        ctkind: this.ctkind,
        cthead: this.cthead,
        ctenumber: this.ctenumber,
        ctnumber: this.ctnumber,
        ctfoot: this.ctfoot,
      };
      axios
        .post(TO, json)
        .then((res) => {
          console.log(res);
          this.getNewNo();
        })
        .catch((err) => {
          console.log("ERR_CATCH");
          console.log(err);
        });
    },
    getNewNo: function () {
      const TO = constant.BACK_END_IP + "/code_taikei/get_new_no";
      const json = {
        ctkind: this.ctkind,
        cthead: this.cthead,
        ctenumber: this.ctenumber,
        ctnumber: this.ctnumber,
        ctfoot: this.ctfoot,
      };
      let vm = this;
      let kind = this.ctkind;

      if (this.cthead != "" && this.ctfoot != "") {
        axios
          .post(TO, json)
          .then((res) => {
            //最新の値を取得する
            const number = res.data.max_number;
            if (kind == 1 || kind == 3) {
              vm.ctnumber = ("0000" + number).slice(-4);
            } else if (kind == 2) {
              vm.ctnumber = ("000" + number).slice(-3);
            } else {
              console.log("ERR");
            }
          })
          .catch((err) => {
            console.log("ERR_CATCH");
            console.log(err);
          });
      } else {
        //必須項目に入力漏れがある場合
        vm.ctnumber = "";
      }
    },
  },
  watch: {
    //ctkindの値に変化があった時
    ctkind: function () {
      if (this.ctkind == "1") {
        this.readonly = false;
      } else if (this.ctkind == "2") {
        this.readonly = false;
      } else if (this.ctkind == "3") {
        this.readonly = true;
        this.ctenumber = "";
      } else {
        console.log("例外");
      }
      this.getNewNo();
    },
  },
};
</script>
<style scoped>
.myset-haba1 {
  width: 60px;
  text-align: center;
  margin: auto 0;
}
.myset-haba1 > input {
  text-align: center;
}
.myset-haba-ctenumber {
  width: 60px;
  text-align: center;
}
</style>
