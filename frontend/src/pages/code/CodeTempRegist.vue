<script setup>
import CodeTempList from "./CodeTempList.vue";
import { ref } from "vue";
import axios from "axios";
import constant from "@/const.js";

const childComponent = ref();
let dialog = ref(false);
let dialog_message = ref(
  "API通信でエラーが発生しました。システム管理者に連絡してください"
);
let ctkind = 1;
let cthead = "";
const regist = () => {
  const TO = constant.BACK_END_IP + "/code_template/regist";
  if (cthead != "") {
    axios
      .post(TO, { ctkind: ctkind, cthead: cthead })
      .then((res) => {
        console.log(res);
        childComponent.value.getList();
      })
      .catch((e) => {
        console.log(e);
        dialog.value = true;
      });
  }
};
</script>
<template>
  <div class="container">
    <h1 @click="log">テンプレート登録</h1>

    <div>
      <div class="row">
        <div class="col">
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="flexRadioDefault"
              id="flexRadioDefault1"
              value="1"
              v-model="ctkind"
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
          <div class="row">
            <input
              type="text"
              class="form-control col mx-3"
              id="cthead"
              v-model="cthead"
              tabindex="50"
            />
            <v-btn
              @click="regist"
              class="col-1 mx-2"
              variant="outlined"
              color="pink"
              >登録</v-btn
            >
          </div>
        </div>
        <div class="col">
          <CodeTempList ref="childComponent" @removeTodo="log"></CodeTempList>
        </div>
      </div>
    </div>
    <!-- エラーダイアログ -->
    <v-dialog v-model="dialog" activator="parent" width="auto">
      <v-card>
        <v-card-text>
          {{ dialog_message }}
        </v-card-text>
        <v-card-actions>
          <v-btn color="primary" block @click="dialog = false"
            >Close Dialog</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
