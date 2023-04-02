<script setup>
import { useRouter } from "vue-router";

const router = useRouter();
</script>
<template>
  <div>
    <h1>コード系メニュー</h1>
    <div class="d-flex">
      <!-- vcard１ 始まり-->
      <v-card class="mx-1" width="200" max-width="200" variant="outlined">
        <v-card-item>
          <div>
            <div class="text-overline mb-1">MenuNo.1</div>
            <div class="text-h6 mb-1">コード採番</div>
            <div class="text-caption">採番機能です</div>
            <div class="text-caption">-</div>
          </div>
        </v-card-item>

        <v-card-actions>
          <v-btn
            class="mx-auto"
            variant="outlined"
            @click="router.push('./code_create')"
          >
            こちら
          </v-btn>
        </v-card-actions>
      </v-card>
      <!-- vcard２ 始まり-->
      <v-card class="mx-1" width="200" max-width="200" variant="outlined">
        <v-card-item>
          <div>
            <div class="text-overline mb-1">MenuNo.2</div>
            <div class="text-h6 mb-1">コード一覧</div>
            <div class="text-caption">一覧表示</div>
            <div class="text-caption">内容登録</div>
          </div>
        </v-card-item>

        <v-card-actions>
          <v-btn
            class="mx-auto"
            variant="outlined"
            @click="router.push('./code_list')"
          >
            こちら
          </v-btn>
        </v-card-actions>
      </v-card>
      <!-- vcard３ 始まり-->
      <v-card class="mx-1" width="200" max-width="200" variant="outlined">
        <v-card-item>
          <div>
            <div class="text-overline mb-1">MenuNo.3</div>
            <div class="text-h6 mb-1">コードTMP登録</div>
            <div class="text-caption">テンプレートの登録</div>
            <div class="text-caption">-</div>
          </div>
        </v-card-item>

        <v-card-actions>
          <v-btn
            class="mx-auto"
            variant="outlined"
            @click="router.push('./code_template_regist')"
          >
            こちら
          </v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>
