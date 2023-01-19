<template>
  <div class="container">
    <div>
      <h1>共通</h1>
      <ul>
        <li>
          <router-link to="/junbi">共通</router-link>
          <ul>
            <li><router-link to="/shain_toroku">社員マスタ</router-link></li>
            <li><router-link to="/tori_toroku">取引先マスタ</router-link></li>
            <li><router-link to="/saiban">採番登録</router-link></li>
            <li><router-link to="/saibanshow">採番一覧</router-link></li>
          </ul>
        </li>
      </ul>
    </div>
    <div>
      <h1>PLM</h1>
      <ul>
        <li>
          <router-link to="/junbi">PDM</router-link>
          <ul>
            <li><router-link to="/e_bom">BOMマスタ登録</router-link></li>
            <li><router-link to="/junbi">BOMマスタ編集</router-link></li>
            <li><router-link to="/junbi">BOMマスタ一覧</router-link></li>

            <li>
              <router-link to="/code_regist">コードマスタ登録</router-link>
            </li>
            <li><router-link to="/junbi">コードマスタ編集</router-link></li>
            <li><router-link to="/code_list">コードマスタ一覧</router-link></li>
          </ul>
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

<script>
</script>
