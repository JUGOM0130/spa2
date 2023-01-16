<template>
  <div>
    <div class="form-check">
      <input
        class="form-check-input"
        type="radio"
        name="flexRadioDefault"
        id="flexRadioDefault1"
        value="0"
        v-model="ctkind"
        checked
      />
      <label class="form-check-label" for="flexRadioDefault1"> ALL </label>
    </div>
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
    <table class="table">
      <thead>
        <tr>
          <th scope="col" v-for="col in columns" :key="col">{{ col }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="data in datas" :key="data">
          <th scope="row">{{ data.ctid }}</th>
          <td>{{ data.ctkind }}</td>
          <td>{{ data.cthead }}</td>
          <td>{{ data.ctenumber }}</td>
          <td>{{ data.ctnumber }}</td>
          <td>{{ data.ctfoot }}</td>
          <td>{{ data.format }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from "axios";
import constant from "../const";
export default {
  data() {
    return {
      ctkind: 0,
      columns: [
        "ID",
        "種別",
        "ヘッダ",
        "英番号",
        "番号",
        "フッダ",
        "フォーマット",
      ],
      datas: [
        {
          ctid: "",
          ctkind: "",
          cthead: "",
          ctenumber: "",
          ctnumber: "",
          ctfoot: "",
          format: "",
        },
      ],
    };
  },
  methods: {
    getList: function () {
      const TO = constant.BACK_END_IP + "/code_taikei/read/" + this.ctkind;
      axios
        .get(TO)
        .then((req) => {
          console.log(req);
          const list = req.data;
          this.datas = [];
          for (let i = 0; i < list.length; i++) {
            this.datas.push({
              ctid: "",
              ctkind: "",
              cthead: "",
              ctenumber: "",
              ctnumber: "",
              ctfoot: "",
              format: "",
            });
            this.datas[i].ctid = list[i].ctid;
            this.datas[i].ctkind = list[i].ctkind;
            this.datas[i].cthead = list[i].cthead;
            this.datas[i].ctenumber = list[i].ctenumber;
            this.datas[i].ctnumber = list[i].ctnumber;
            this.datas[i].ctfoot = list[i].ctfoot;
            if (this.ctkind == 1 || this.ctkind == 3) {
              this.datas[i].format =
                list[i].cthead +
                "-" +
                list[i].ctenumber +
                ("0000" + list[i].ctnumber).slice(-4) +
                list[i].ctfoot;
            } else {
              this.datas[i].format =
                list[i].cthead +
                "-" +
                list[i].ctenumber +
                ("000" + list[i].ctnumber).slice(-3) +
                list[i].ctfoot;
            }
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
  watch: {
    ctkind: function () {
      this.getList();
    },
  },
  created() {
    this.getList();
  },
};
</script>
