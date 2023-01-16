<template>
  <div class="container">
    <h1>登録</h1>
    <form>
      <div class="mb-3">
        <label for="shain_cd" class="form-label">コード</label>
        <input type="text" class="form-control" id="shain_cd" />
      </div>
      <div class="mb-3">
        <label for="shain_cd" class="form-label">名称</label>
        <input type="text" class="form-control" id="shain_cd" />
      </div>
      <div class="mb-3">
        <label for="shain_cd" class="form-label">製品名称</label>
        <input type="text" class="form-control" id="shain_cd" />
      </div>
      <div class="mb-3">
        <label for="first_name" class="form-label">版数（リビジョン）</label>
        <input type="text" class="form-control" id="first_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">手配先</label>
        <select class="form-select" aria-label="Default select example">
          <option selected>-</option>
          <option value="1">株式会社AVAIL</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">型式</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">材質</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">内外策</label>
        <select class="form-select" aria-label="Default select example">
          <option selected>-</option>
          <option value="1">内策</option>
          <option value="2">外策</option>
          <option value="3">内策＋外策</option>
        </select>
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">主要材料費</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">補助材料費</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">外注加工費</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">直接労務費</label>
        <input type="text" class="form-control" id="last_name" />
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>
