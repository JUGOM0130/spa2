<template>
  <div class="container">
    <h1>登録</h1>
    <form>
      <div class="mb-3">
        <label for="shain_cd" class="form-label">取引先コード</label>
        <input type="text" class="form-control" id="shain_cd" />
      </div>
      <div class="mb-3">
        <label for="shain_cd" class="form-label">取引先名</label>
        <input type="text" class="form-control" id="shain_cd" />
      </div>
      <div class="mb-3">
        <label for="shain_cd" class="form-label">取引先名（カナ）</label>
        <input type="text" class="form-control" id="shain_cd" />
      </div>
      <div class="mb-3">
        <label for="first_name" class="form-label">郵便番号</label>
        <input type="text" class="form-control" id="first_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">県</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">市町村</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">区</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">その他</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">担当者コード（社内）</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">担当者名（取引先）</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">Mail（取引先担当者）</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">TEL（取引先担当者）</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">Mail（取引先代表）</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">TEL（取引先代表）</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div>
        <div class="form-check form-check-inline">
          <input class="form-check-input" type="checkbox" value="1" id="man" />
          <label class="form-check-label" for="man"> 男 </label>
        </div>
        <div class="form-check form-check-inline">
          <input
            class="form-check-input"
            type="checkbox"
            value="2"
            id="woman"
            checked
          />
          <label class="form-check-label" for="woman"> 女 </label>
        </div>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>
