<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import constant from "@/const";

const route = useRoute();
const router = useRouter();
const pname = route.query.name;
const pid = route.query.id;
let display_type = ref("REGISTRATION");

let tree = ref([
  {
    parts_id: pid,
    name: pname,
    lv: "1",
    parent_id: "0",
    order: "",
    composition_id: "1",
    insu: 0,
    bosu: 0,
  },
]);
let selected = ref(tree.value[0]);
let add_id = ref("");
let add_name = ref("");
let parts = ref([{ pid: "PartsId", pname: "PartsName" }]);
let selected_parts = ref(parts.value[0]);

const treeListSort = () => {
  let new_tree = [];
  //配列オブジェクトにソートをかける
  tree.value.sort((a, b) => a.parent_id - b.parent_id);
  //配列の並びをツリー形式に見えるように変換
  tree.value.forEach((e) => {
    if (e.parent_id > 0) {
      //parent_idが１以上のもの
      let idx = 0;
      new_tree.forEach((el, i) => {
        if (el.composition_id == e.parent_id) {
          idx = i;
        }
      });
      new_tree.splice(idx, 0, e);
    } else {
      //ルート要素
      new_tree.unshift(e);
    }
  });
  new_tree = new_tree.reverse();
  tree.value = [];
  new_tree.forEach((e, i) => {
    let obj = e;
    obj.order = i;
    tree.value.push(obj);
  });

  console.log(new_tree);
};
const treeAdd = () => {
  let add_ID = add_id.value;
  let name = add_name.value;
  let flag = true;
  let obj = {
    parts_id: add_ID,
    name: name,
    lv: "1",
    parent_id: "0",
    order: "",
    composition_id: "0",
    insu: 0,
    bosu: 0,
  };

  //tree内の最大値取得
  let max = 0;
  tree.value.forEach((e) => {
    if (max < Number(e.composition_id)) {
      max = Number(e.composition_id);
    }
  });
  obj.composition_id = String(max + 1);

  //IDの重複が慣れけば配列に追加する
  if (flag) {
    let target = {};
    let index = 0;
    let eq_lv_counter = 0;
    tree.value.forEach((e, i) => {
      //セレクトボックスの選択値と配列のidが一致したら要素を保存
      if (e.composition_id == selected.value.composition_id) {
        target = e;
        index = i;
      }
    });

    eq_lv_counter = getInsertPosition(tree.value, target);

    console.log(
      `\tindex = ${index}\n\teq_lv_counter = ${eq_lv_counter}\n\tgetInsertPosition() = ${getInsertPosition(
        tree.value,
        target
      )}`
    );
    obj.lv = String(Number(target.lv) + 1);
    obj.parent_id = String(target.composition_id);
    tree.value.splice(index + 1 + eq_lv_counter, 0, obj);
    tree.value.forEach((e, i) => {
      e.order = i;
    });
  }
  console.log(tree.value);
};
const getInsertPosition = (tree, target) => {
  let eq_lv = [];
  let sum_arr = [];
  let sum = 0;
  eq_lv = tree.filter((t) => {
    return t.parent_id == target.composition_id;
  });
  eq_lv.forEach((new_target) => {
    sum_arr.push(getInsertPosition(tree, new_target));
  });
  sum = sum_arr.reduce(function (sum, element) {
    return sum + element;
  }, 0);

  return eq_lv.length + sum;
};
const getParts = () => {
  const TO = constant.BACK_END_IP + "/tree/get_root_list";
  axios
    .get(TO)
    .then((res) => {
      console.log(res);
      const alias = res.data.result.data;
      alias.forEach((e) => {
        parts.value.push({ pid: String(e.pid), pname: String(e.pcd) });
      });
      parts.value.shift();
      selected_parts.value.pid = parts.value[0].pid;
      selected_parts.value.pname = parts.value[0].pname;

      console.log(parts.value);
      console.log(selected_parts.value);
    })
    .catch((err) => {
      console.log(err);
    });
};
/**
 * ツリーへデータ追加処理
 */
const addClick = () => {
  add_id.value = selected_parts.value.pid;
  add_name.value = selected_parts.value.pname;
  treeAdd();
};
/**
 * ツリー登録処理
 */
const registClick = () => {
  const TO = constant.BACK_END_IP + "/tree/regist";
  let treeArray = tree.value;

  axios
    .post(TO, treeArray)
    .then((res) => {
      console.log(res);
      let status = res.data.result.status;
      if (status == "OK") {
        router.push("/");
      }
    })
    .catch((err) => {
      console.log(err);
    });
};
/**
 * ツリー更新
 */
const updateClick = () => {
  console.log("更新");
};

/**
 * 初期セットアップ_更新
 */
const edit_init = () => {
  display_type.value = "EDIT";
  const TO = constant.BACK_END_IP;
  axios
    .post(TO + "/tree/get_tree_datas", { tree_id: route.query.tree_id })
    .then((res) => {
      let td = res.data.result.data;
      console.log(res);
      tree.value = [];
      td.forEach((e) => {
        tree.value.push({
          parts_id: e.parts_id,
          name: e.pcd,
          lv: e.lv,
          parent_id: e.parent_id,
          order: e.order,
          composition_id: e.composition_id,
          insu: e.insu,
          bosu: e.bosu,
        });
      });
      selected.value = tree.value[0];
    })
    .catch((err) => {
      console.log(err);
    });
};

onMounted(() => {
  if (route.query.tree_id != "") {
    edit_init();
  }
  getParts();
  treeListSort();
});
</script>
<template>
  <div>
    <v-container>
      <v-row justify="end">
        <v-btn
          @click="registClick()"
          variant="outlined"
          color="red"
          v-if="display_type == 'REGISTRATION'"
          >登録</v-btn
        >
        <v-btn
          @click="updateClick()"
          variant="outlined"
          color="green"
          v-if="display_type == 'EDIT'"
          >更新</v-btn
        >
      </v-row>
    </v-container>

    <div class="table_wrappar">
      <table class="table">
        <tr>
          <th>コード</th>
          <th>名称</th>
          <th>製品名称</th>
          <th>版数</th>
          <th>員数</th>
          <th>母数</th>
          <th>型式</th>
          <th>材質</th>
          <th>内外策</th>
          <th>ステータス</th>
          <th>主要材料費</th>
          <th>補助材料費</th>
          <th>外注加工費</th>
          <th>直接労務費</th>
        </tr>
        <tr v-for="t in tree" :key="t.composition_id">
          <td>
            <div class="flex_box">
              <div class="space" v-for="k in t.lv - 1" :key="k"></div>
              <p class="flex_item">{{ t.name }}</p>
            </div>
          </td>

          <td><input type="text" class="myset_input" placeholder="名称" /></td>
          <td>
            <input type="text" class="myset_input" placeholder="製品名称" />
          </td>
          <td><input type="text" class="myset_input" placeholder="版数" /></td>
          <td>
            <input
              type="text"
              class="myset_input"
              placeholder="員数"
              v-model="t.insu"
            />
          </td>
          <td>
            <input
              type="text"
              class="myset_input"
              placeholder="母数"
              v-model="t.bosu"
            />
          </td>
          <td><input type="text" class="myset_input" placeholder="型式" /></td>
          <td><input type="text" class="myset_input" placeholder="材質" /></td>
          <td>
            <input type="text" class="myset_input" placeholder="内外作" />
          </td>
          <td>
            <input type="text" class="myset_input" placeholder="ステータス" />
          </td>
          <td>
            <input type="text" class="myset_input" placeholder="主要材料費" />
          </td>
          <td>
            <input type="text" class="myset_input" placeholder="補助材料費" />
          </td>
          <td>
            <input type="text" class="myset_input" placeholder="外注加工費" />
          </td>
          <td>
            <input type="text" class="myset_input" placeholder="直接労務費" />
          </td>
        </tr>
      </table>
    </div>
    <v-select
      label="選択ノード"
      v-model="selected"
      :items="tree"
      item-title="name"
      item-value="composition_id"
      :hint="`${selected.name} ,${selected.composition_id}`"
      persistent-hint
      return-object
    >
    </v-select>
    <v-select
      label="ツリー追加部品"
      v-model="selected_parts"
      :items="parts"
      item-title="pname"
      item-value="pid"
      :hint="`${selected_parts.pname} ,${selected_parts.pid}`"
      persistent-hint
      return-object
    >
    </v-select>
    <v-btn @click="addClick()">追加</v-btn>
  </div>
</template>
<style scoped lang="scss">
.space {
  display: inline;
  width: 30px;
  height: 30px;
}

.myset_input {
  width: auto;

  margin-left: 2.5px;
  margin-right: 2.5px;
  margin-top: 2.5px;
}

.table_wrappar {
  grid-area: content;
  overflow: scroll;
  border-style: solid;
  border-width: 1px;
  margin: 5px;

  * {
    padding: 0px;
    margin: 0px;
  }

  th {
    text-align: center;
    border-right-width: 1px;
    border-bottom-width: 1px;
    border-right-style: solid;
    border-bottom-style: solid;
    border-right-color: black;
    border-bottom-color: black;
  }

  .table {
    th:nth-child(1) {
      min-width: 200px;
      position: sticky;
      left: 0;
      z-index: 2;
      background-color: gainsboro;
    }
    td:nth-child(1) {
      max-width: max-content + 30px;
      min-width: 200px;
      position: sticky;
      left: 0;
      z-index: 1;
      padding-right: 5px;
      padding-left: 5px;

      border-right-style: solid;
      border-right-color: black;
      border-right-width: 1px;

      background-color: gainsboro;

      font-size: 24px;
      vertical-align: middle;
    }
    tr:nth-child(2n) {
      background-color: aquamarine;
      td {
        background-color: aquamarine;
      }
    }
  }
}

.flex_box {
  display: flex;
  flex-wrap: nowrap;

  .flex_item {
    flex-basis: content;
    white-space: nowrap;
  }
}
</style>
