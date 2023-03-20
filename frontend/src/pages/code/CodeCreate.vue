<template>
  <div>
    <div class="row">
      <div class="col">
        <v-fade-transition>
          <v-alert
            v-model="isError"
            type="error"
            title="ERR"
            v-text="errorMessage"
          ></v-alert>
        </v-fade-transition>
        <h1>登録</h1>
      </div>
    </div>
    <div class="row">
      <div class="col">
        <div class="form-check">
          <input
            class="form-check-input"
            type="radio"
            name="flexRadioDefault"
            id="flexRadioDefault1"
            value="1"
            v-model="ckind"
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
            v-model="ckind"
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
            v-model="ckind"
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
                id="chead"
                v-model="chead"
                v-on:blur="getNewNoInputDirect"
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
                v-bind:class="[cenumber_class]"
                id="cenumber"
                v-model="cenumber"
                v-on:blur="getNewNoInputDirect"
                v-bind:readonly="readonly"
                tabindex="52"
              />
            </div>
            <!--  Number 0000 -->
            <div class="p-2 bd-highlight">
              <input
                type="text"
                class="form-control"
                id="cnumber"
                readonly
                v-model="cnumber"
                tabindex="-1"
              />
            </div>
            <!--  Z0000  -->
            <div class="p-2 bd-highlight">
              <input
                type="text"
                class="form-control"
                id="cfoot"
                v-model="cfoot"
                v-on:blur="getNewNoInputDirect"
                tabindex="56"
              />
            </div>
          </div>
        </div>
        <v-btn variant="outlined" color="pink" @click="regist">登録</v-btn>
      </div>
      <div class="col">
        <CodeTempList @code-temp-data="templateClick"></CodeTempList>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import constant from "../../const";
import CodeTempList from "./CodeTempList.vue";

export default {
  data: function () {
    return {
      ckind: "1",
      chead: "",
      cenumber: "",
      cnumber: "",
      cfoot: "",
      cenumber_class: "form-control myset-haba-cenumber",
      readonly: false,
      isError: false,
      errorMessage: "",
    };
  },
  components: {
    CodeTempList,
  },
  methods: {
    regist: function () {
      if (this.cnumber != "") {
        const TO = constant.BACK_END_IP + "/code_taikei/regist";
        const json = {
          ckind: this.ckind,
          chead: this.chead,
          cenumber: this.cenumber,
          cnumber: this.cnumber,
          cfoot: this.cfoot,
        };
        axios
          .post(TO, json)
          .then((res) => {
            console.log(res);
            const st = res.data.result.status;

            if (st == "100" || st == "200") {
              //画面リロード
              this.$router.go({
                path: this.$router.currentRoute.path,
                force: true,
              });
            } else if (st == "300") {
              console.log("カウンタカンスト");
            } else {
              console.log("default");
            }
          })
          .catch((err) => {
            console.log("ERR_CATCH");
            console.log(err);
          })
          .finally(() => {
            this.getNewNoInputDirect();
          });

        this.cnumber = "";
      } else {
        this.isError = true;
        this.errorMessage = "ERROR：番号が取得できていません確認してください";

        window.setTimeout(() => {
          this.isError = false;
          this.errorMessage = "";
        }, 3000);
      }
    },
    getNewNoInputDirect: function () {
      const TO = constant.BACK_END_IP + "/code_taikei/get_new_no_input_direct";
      const json = {
        ckind: this.ckind,
        chead: this.chead,
        cenumber: this.cenumber,
        cnumber: this.cnumber,
        cfoot: this.cfoot,
      };
      let vm = this;
      let kind = this.ckind;

      if (this.chead != "" && this.cfoot != "" && this.cenumber != "") {
        axios
          .post(TO, json)
          .then((res) => {
            //最新の値を取得する
            const number = res.data.max_number;
            if (kind == 1 || kind == 3) {
              vm.cnumber = ("0000" + number).slice(-4);
            } else if (kind == 2) {
              vm.cnumber = ("000" + number).slice(-3);
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
        vm.cnumber = "";
      }
    },
    getNewNoSelectList: function () {
      const TO = constant.BACK_END_IP + "/code_taikei/get_new_no_select_list";
      const json = {
        ckind: this.ckind,
        chead: this.chead,
        cenumber: this.cenumber,
        cnumber: this.cnumber,
        cfoot: this.cfoot,
      };
      let vm = this;
      let kind = this.ckind;
      if (this.chead != "" && this.cfoot != "") {
        axios
          .post(TO, json)
          .then((res) => {
            //最新の値を取得する
            const number = res.data.max_number;
            if (kind == 1 || kind == 3) {
              vm.cnumber = ("0000" + number).slice(-4);
            } else if (kind == 2) {
              vm.cnumber = ("000" + number).slice(-3);
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
        vm.cnumber = "";
      }
    },
    templateClick: function (data) {
      this.cnumber = "";
      this.ckind = data.ctkind;
      this.cenumber = data.ctenumber;
      this.chead = data.cthead;
      if (data.ctkind == 1 || data.ctkind == 2) {
        this.cfoot = "Z000";
      } else if (data.ctkind == 3) {
        this.cfoot = "Z0";
      } else {
        this.cfoot = "";
      }
      console.log(this.$data);
      this.getNewNoSelectList();
    },
  },
  watch: {
    //ckindの値に変化があった時
    ckind: function () {
      if (this.ckind == "1") {
        this.readonly = false;
      } else if (this.ckind == "2") {
        this.readonly = false;
      } else if (this.ckind == "3") {
        this.readonly = true;
        this.cenumber = "";
      } else {
        console.log("例外");
      }
      this.getNewNoInputDirect();
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

.myset-haba-cenumber {
  width: 60px;
  text-align: center;
}
</style>
