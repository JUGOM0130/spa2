<script setup>
import { defineProps, ref } from "vue";

const props = defineProps({
  items: Array,
});

let items = ref(props.items);
</script>
<template>
  <div>
    <v-row>
      <v-col> 名称 </v-col>
      <v-col> 製品名称 </v-col>
      <v-col> 版数 </v-col>
      <v-col> 員数 </v-col>
      <v-col> 母数 </v-col>
      <v-col> 型式 </v-col>
      <v-col> 材質 </v-col>
      <v-col> 内外策 </v-col>
      <v-col> ステータス </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-row v-for="item in items" :key="item" class dense no-gutters>
          <v-col class="ma-1 pa-0">
            <v-text-field label="名称" hide-details="auto"> </v-text-field>
          </v-col>
          <v-col class="ma-1 pa-0">
            <v-text-field hide-details="auto" label="製品名称"></v-text-field>
          </v-col>
          <v-col class="ma-1 pa-0">
            <v-text-field hide-details="auto" label="版数"></v-text-field>
          </v-col>
          <v-col class="ma-1 pa-0">
            <v-text-field hide-details="auto" label="員数"></v-text-field>
          </v-col>
          <v-col class="ma-1 pa-0">
            <v-text-field hide-details="auto" label="母数"></v-text-field>
          </v-col>
          <v-col class="ma-1 pa-0">
            <v-text-field hide-details="auto" label="型式"></v-text-field>
          </v-col>
          <v-col class="ma-1 pa-0">
            <v-text-field hide-details="auto" label="材質"></v-text-field>
          </v-col>
          <v-col class="ma-1 pa-0">
            <v-text-field hide-details="auto" label="内外策"></v-text-field>
          </v-col>
          <v-col class="ma-1 pa-0">
            <v-text-field hide-details="auto" label="ステータス"></v-text-field>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </div>
</template>
