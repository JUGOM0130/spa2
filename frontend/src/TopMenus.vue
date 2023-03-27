<script setup>
const toCodeMenu = () => {
  window.location.href = "/code/";
};

const toTreeMenu = () => {
  window.location.href = "/tree/";
};
</script>
<template>
  <div>
    <h1>メニュー</h1>
    <v-container >
      <v-row justify="start">
        <v-col>
          <v-card class="mx-auto" max-width="200" variant="outlined">
            <v-card-item>
              <div>
                <div class="text-overline mb-1">CodeMenus</div>
                <div class="text-h6 mb-1">コードメニュー</div>
                <div class="text-caption">・テンプレート登録</div>
                <div class="text-caption">・コード登録</div>
              </div>
            </v-card-item>

            <v-card-actions>
              <v-btn class="mx-auto" variant="outlined" @click="toCodeMenu()">
                こちら
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col>
          <v-card class="mx-auto" max-width="200" variant="outlined">
            <v-card-item>
              <div>
                <div class="text-overline mb-1">TreeMenus</div>
                <div class="text-h6 mb-1">ツリーメニュー</div>
                <div class="text-caption">・ツリー作成</div>
                <div class="text-caption">・</div>
              </div>
            </v-card-item>

            <v-card-actions>
              <v-btn variant="outlined" class="mx-auto" @click="toTreeMenu()">
                こちら
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-spacer></v-spacer>
      </v-row>
    </v-container>
    <div>
      <h3>共通</h3>
      <ul>
        <li>
          <router-link to="/junbi">共通</router-link>
          <ul>
            <li><router-link to="/junbi">社員マスタ</router-link></li>
            <li><router-link to="/torihiki">取引先マスタ</router-link></li>
          </ul>
        </li>
      </ul>
    </div>
    <div>
      <h3>PLM</h3>
      <ul>
        <li>
          <a href="/code">コード系メニュー</a>
        </li>
        <li>
          <a href="/tree">ツリー系メニュー</a>
        </li>
        <li>
          <router-link to="/junbi">生産管理</router-link>
          <ul>
            <li><router-link to="/junbi">生産依頼</router-link></li>
            <li><router-link to="/junbi">生産計画</router-link></li>
          </ul>
        </li>
        <li>
          <router-link to="/junbi">在庫管理</router-link>
          <ul>
            <li><router-link to="/junbi">製品在庫</router-link></li>
            <li><router-link to="/junbi">部品在庫</router-link></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</template>

