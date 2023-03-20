<script setup>
import { ref } from "vue";
import { treeDataAdd } from "@/pages/tree/Tree.js";
import TreeViewComponent from "./TreeViewComponent.vue";
let where = ref(1);
let id = ref(0);
let name = ref("");

let data = ref([
  {
    id: 1,
    name: "takahasi",
    child: [
      {
        id: 2,
        name: "takeda",
        child: [
          {
            id: 3,
            name: "jugom",
            child: [],
          },
        ],
      },
    ],
  },
]);
</script>
<template>
  <div>
    <div>
      <div>
        <label for="where">where:</label>
        <input type="number" name="where" id="where" v-model="where" />
      </div>
      <div>
        <label for="target_id">target_id:</label>
        <input type="number" name="target_id" id="target_id" v-model="id" />
      </div>
      <div>
        <label for="name">name:</label>
        <input type="text" name="name" id="name" v-model="name" />
      </div>
    </div>
    <button
      @click="treeDataAdd(where, data, { id: id, name: name, child: [] })"
    >
      追加ボタン
    </button>
    <TreeViewComponent :data1="data"></TreeViewComponent>
  </div>
</template>
