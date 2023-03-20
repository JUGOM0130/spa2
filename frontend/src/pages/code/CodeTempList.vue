<script setup>
import axios from "axios";
import constant from "@/const";
import {
  reactive,
  ref,
  onMounted,
  defineExpose,
  defineEmits,
  watch,
} from "vue";

let ctkind = ref(0);
const columns = ["ID", "種別", "英番号", "ヘッダ"];
let datas = reactive([
  {
    ctid: 0,
    ctkind: 1,
    cthead: "",
    ctenumber: "",
    isDispay: true,
  },
]);
const getList = () => {
  const TO = constant.BACK_END_IP + "/code_template/select";
  axios
    .get(TO)
    .then((res) => {
      console.log(res)
      datas.splice(0); //配列の初期化
      res.data.result.data.forEach((element) => {
        datas.push(
          reactive({
            ctid: element.ctid,
            ctkind: element.ctkind,
            cthead: element.cthead,
            ctenumber: element.ctenumber,
            isDispay: true,
          })
        );
      });
    })
    .catch((e) => {
      console.log(e);
    });
};
//const target = (data) => {};
const emit = defineEmits(["codeTempData"]);
const clickevent = (data) => {
  emit("codeTempData", data);
};
watch(ctkind, () => {
  if (ctkind.value != 0) {
    datas.forEach((dt, i) => {
      if (dt.ctkind == ctkind.value) {
        datas[i].isDispay = true;
      } else {
        datas[i].isDispay = false;
      }
    });
  } else {
    datas.forEach((dt, i) => {
      datas[i].isDispay = true;
    });
  }
});
onMounted(() => {
  getList();
});
defineExpose({
  getList,
});
</script>
<template>
  <div>
    <div class="row g-2">
      <div class="col">
        <div class="form-check">
          <input
            class="form-check-input"
            type="radio"
            name="kind"
            id="kind0"
            value="0"
            v-model="ctkind"
          />
          <label class="form-check-label" for="kind0"> ALL </label>
        </div>
        <div class="form-check">
          <input
            class="form-check-input"
            type="radio"
            name="kind1"
            id="kind1"
            value="1"
            v-model="ctkind"
          />
          <label class="form-check-label" for="kind1"> XXX-AxxxxZ000 </label>
        </div>
        <div class="form-check">
          <input
            class="form-check-input"
            type="radio"
            name="kind"
            id="kind2"
            value="2"
            v-model="ctkind"
          />
          <label class="form-check-label" for="kind2"> XXX-AAxxxZ000 </label>
        </div>
        <div class="form-check">
          <input
            class="form-check-input"
            type="radio"
            name="kind"
            id="kind3"
            value="3"
            v-model="ctkind"
          />
          <label class="form-check-label" for="kind3"> XX-xxxxZ0 </label>
        </div>
      </div>
    </div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col" v-for="col in columns" :key="col">{{ col }}</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="data in datas"
          :key="data"
          @click="clickevent(data)"
          v-show="data.isDispay"
        >
          <th scope="row">{{ data.ctid }}</th>
          <td>{{ data.ctkind }}</td>
          <td>{{ data.ctenumber }}</td>
          <td>{{ data.cthead }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
