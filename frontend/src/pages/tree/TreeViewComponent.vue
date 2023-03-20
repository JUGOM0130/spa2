<script setup>
import { defineProps, ref } from "vue";
import TreeViewComponent from "@/pages/tree/TreeViewComponent.vue";

const props = defineProps({
  data1: Array,
});
let data = ref(props.data1);
let src_id = "";

const dstart = (e) => {
  src_id = e.target.id;
  console.log(`dstart ${src_id}`);
  console.log(e.target);
};

const over = (e, id) => {
  console.log(`over:${id} src_id:${src_id}`);
  //console.log(e);
  console.log(e.target);
  if (id == src_id) {
    e.target.className = "font-color";
  } else {
    e.target.className = "style-test";
  }
  //e.target.className = "style-test";
};

const leave = (e, id) => {
  console.log(`leav:${id}`);
  e.target.className = "item";
};
console.log("TreeViewCmponent.vueが呼ばれました");
</script>
<template>
  <div>
    <ul v-for="d in data" :key="d.id">
      <li class="item">
        <div
          draggable="true"
          @dragstart="dstart($event)"
          @dragenter="over($event, d.id)"
          @dragleave="leave($event, d.id)"
          :class="d.class"
          :id="d.id"
        >
          {{ d.name }}
        </div>
      </li>
      <div style="height: 0.5px"></div>
      <template v-if="d.child.length > 0">
        <TreeViewComponent :data1="d.child" :key="d.id"></TreeViewComponent>
      </template>
    </ul>
  </div>
</template>

<style>
.item {
  background-color: aquamarine;
  margin: 4px;
  height: 56px;
  font-size: 25px;
}

.style-none {
  background-color: beige;
}

.style-test {
  background-color: red;
  font-size: 40px;
}

.font-color {
  color: greenyellow;
}
</style>
