<template>
  <div class="container">
    <h1>メニュー</h1>
    <div>
      <h3>共通</h3>
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
      <h3>PLM</h3>
      <ul>
        <li>
          <a href="/code">コード系メニュー</a>
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
