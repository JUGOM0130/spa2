<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import TreeViewComponent from "./TreeViewComponent.vue";
import { treeDataAdd, getTreeList } from "./Tree";
import TreeDetailsData from "./TreeDetailsData.vue";
import TableTree from "./TableTree.vue";

const route = useRoute();
let random_key = ref("aasdfdsaf");
let obj = ref([]);
let name = ref("");
let settingId = ref("");
let selected = ref({ id: "", name: "", child: [] });
let items = ref([]);

const add = () => {
  let sId = settingId.value;
  let sName = name.value;
  let data = { id: sId, name: sName, child: [] };
  random_key.value = Math.random();
  //同じ要素があるかチェック
  let flag = true;
  items.value.forEach((element) => {
    if (element.id == sId) {
      //あればフラグをDOWN
      flag = false;
    }
  });

  //同じ要素がない場合オブジェクトに追加処理
  if (flag) {
    let parentObjectId = String(selected.value.id);
    let o = treeDataAdd(parentObjectId, JSON.stringify(obj.value), data);
    obj.value.pop();
    obj.value.push(o[0]);
    //selectに表示する
    items.value.push({ id: sId, name: sName, child: [] });
  } else {
    console.log(`ID${sId}は既に存在します。`);
  }

  console.log(obj.value);
};

const test = () => {
  const o = {
    id: "1111",
    name: "AAA",
    class: "",
    child: [
      {
        id: "5555",
        name: "BBB",
        class: "",
        child: [{ id: "1212", name: "CCC", child: [] }],
      },
      {
        id: "2222",
        name: "DDD",
        class: "",
        child: [
          {
            id: "3333",
            name: "EEE",
            class: "",
            child: [{ id: "4444", name: "FFF", child: [] }],
          },
        ],
      },
      { id: "9983", name: "GGG", class: "", child: [] },
      { id: "3222", name: "HHH", class: "", child: [] },
    ],
  };
  obj = ref([]);
  let b = ref(o);
  obj.value.push(b.value);
  let arr = [];
  arr.push(o);
  items = ref(getTreeList(arr));
  selected.value = items.value[0];
  random_key.value = Math.random().toString(32).substring(2);
};

onMounted(() => {
  const query = route.query;
  items.value.push({ id: query.number, name: query.name, child: [] });
  obj.value.push({ id: query.number, name: query.name, child: [] });
  selected = ref({ id: query.number, name: query.name, child: [] });
  console.log(obj);
});
</script>
<template>
  <div>
    <v-container class="table_container" fluid>
      <v-row>
        <v-col cols="3">
          <div>
            <v-row>
              <v-col>部品名</v-col>
            </v-row>
            <v-row>
              <v-col>
                <TreeViewComponent
                  :data1="obj"
                  :key="random_key"
                ></TreeViewComponent>
              </v-col>
            </v-row>
          </div>
        </v-col>
        <v-col cols="9">
          <div class="overflow-x-auto" max-width="4000">
            <div style="width: 2000px">
              <TreeDetailsData :items="items"></TreeDetailsData>
            </div>
          </div>
        </v-col>
      </v-row>
    </v-container>
    <v-select
      v-model="selected"
      label="対象の子ノードに下記要素を追加"
      :items="items"
      item-title="name"
      item-value="id"
      return-object
    ></v-select>
    <v-text-field label="追加要素" v-model="name"></v-text-field>
    <v-text-field label="追加要素ID" v-model="settingId"></v-text-field>

    <TableTree></TableTree>
    <v-btn @click="add">追加</v-btn>
    <v-btn @click="test">test</v-btn>
  </div>
</template>

<style>
.yoko_scroll_outer {
  padding: 5px;
  border: 1px;
  border-style: solid;
  margin-bottom: 5px;
}
.table_container {
  padding: 5px;
  border: 1px;
  border-style: solid;

  margin-bottom: 5px;
}
</style>
