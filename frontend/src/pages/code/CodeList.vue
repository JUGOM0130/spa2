<template>
  <div>
    <div class="row g-2">
      <div class="col">
        <div class="form-check">
          <input
            class="form-check-input"
            type="radio"
            name="kind0"
            id="kind0"
            value="0"
            v-model="ckind"
            checked
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
            v-model="ckind"
          />
          <label class="form-check-label" for="kind1"> XXX-AxxxxZ000 </label>
        </div>
        <div class="form-check">
          <input
            class="form-check-input"
            type="radio"
            name="kind2"
            id="kind2"
            value="2"
            v-model="ckind"
          />
          <label class="form-check-label" for="kind2"> XXX-AAxxxZ000 </label>
        </div>
        <div class="form-check">
          <input
            class="form-check-input"
            type="radio"
            name="kind3"
            id="kind3"
            value="3"
            v-model="ckind"
          />
          <label class="form-check-label" for="kind3"> XX-xxxxZ0 </label>
        </div>
      </div>
      <div class="col">
        <input
          class="form-control"
          type="text"
          name="serchword"
          id="serchword"
          placeholder="検索キーワード"
          v-model="serchword"
        />
      </div>
    </div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col" v-for="col in columns" :key="col">{{ col }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="data in datas" :key="data" v-show="data.isDisplay">
          <th scope="row">{{ data.cid }}</th>
          <td>{{ data.ckind }}</td>
          <td>{{ data.chead }}</td>
          <td>{{ data.cenumber }}</td>
          <td>{{ data.cnumber }}</td>
          <td>{{ data.cfoot }}</td>
          <td>{{ data.format }}</td>
          <td>{{ data.pname }}</td>
          <td>
            <v-btn
              variant="outlined"
              @click="moveNextScreen(data)"
              class="text-light-blue-darken-4"
            >
              登録・更新
            </v-btn>
          </td>
          <td>
            <v-btn variant="outlined" class="text-purple-lighten-2">
              工程追加
            </v-btn>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from "axios";
import constant from "../../const";
export default {
  data() {
    return {
      serchword: "",
      ckind: 0,
      columns: [
        "ID",
        "種別",
        "ヘッダ",
        "英番号",
        "番号",
        "フッダ",
        "フォーマット",
        "名称",
        "",
        "",
      ],
      datas: [
        {
          isDisplay: false,
          cid: "",
          ckind: "",
          chead: "",
          cenumber: "",
          cnumber: "",
          cfoot: "",
          format: "",
          pname: "",
          pid: "",
        },
      ],
    };
  },
  methods: {
    /**
     * コード一覧取得
     */
    getList: function () {
      const TO = constant.BACK_END_IP + "/code_taikei/read/" + this.ckind;
      axios
        .get(TO)
        .then((req) => {
          const list = req.data;
          this.datas = [];
          for (let i = 0; i < list.length; i++) {
            this.datas.push({
              isDisplay: true,
              cid: list[i].cid,
              ckind: list[i].ckind,
              chead: list[i].chead,
              cenumber: list[i].cenumber,
              cnumber: list[i].cnumber,
              cfoot: list[i].cfoot,
              format: "",
              pname: list[i].pname,
              pid: list[i].pid,
            });
            //登録種別でフォーマットを変える
            if (this.ckind == 1 || this.ckind == 3) {
              this.datas[i].format =
                list[i].chead +
                "-" +
                list[i].cenumber +
                ("0000" + list[i].cnumber).slice(-4) +
                list[i].cfoot;
            } else {
              this.datas[i].format =
                list[i].chead +
                "-" +
                list[i].cenumber +
                ("000" + list[i].cnumber).slice(-3) +
                list[i].cfoot;
            }
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
    /**
     * 詳細画面に遷移する
     */
    moveNextScreen: function (data) {
      console.log(data);
      this.$store.commit("dataset", {
        id: data.cid,
        cd: data.format,
        parts_id: Number(data.pid),
      });
      this.$router.push({
        path: "/code_data_regist",
      });
    },
    /**
     * 検索ワードと一致するものを検索
     */
    serch: function () {
      this.datas.forEach((e, idx) => {
        //検索ワードと一致するものを検索
        if (this.serchword != "") {
          if (e.pname == null || e.pname == "") {
            e.pname = "";
          }
          if (e.pname.indexOf(this.serchword) != -1) {
            this.datas[idx].isDisplay = true;
          } else if (e.format.indexOf(this.serchword) != -1) {
            this.datas[idx].isDisplay = true;
          } else {
            this.datas[idx].isDisplay = false;
          }
        } else {
          this.datas[idx].isDisplay = true;
        }
      });
    },
  },
  /**
   * 変数の状態監視
   * ckind（ラジオ）に変化があれば一覧を更新する
   */
  watch: {
    ckind: function () {
      this.getList();
    },
    serchword: function () {
      this.serch();
    },
  },
  /**
   * ライフサイクルフックcreated
   */
  created() {
    this.getList();
  },
};
</script>
