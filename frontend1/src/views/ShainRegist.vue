<template>
  <div class="container">
    <h1>登録</h1>
    <form>
      <div class="mb-3">
        <label for="shain_cd" class="form-label">{{ row1 }}</label>
        <input type="text" class="form-control" id="shain_cd" v-model="cd" />
      </div>
      <div class="mb-3">
        <label for="first_name" class="form-label">{{ row2 }}</label>
        <input
          type="text"
          class="form-control"
          id="first_name"
          v-model="first_name"
        />
      </div>
      <div class="mb-3">
        <label for="last_name" class="form-label">{{ row3 }}</label>
        <input
          type="text"
          class="form-control"
          id="last_name"
          v-model="last_name"
        />
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
<style>
</style>
<script>
import axios from "axios";
export default {
  data: function () {
    return {
      row1: "社員番号",
      row2: "氏",
      row3: "名",
      cd: "",
      first_name: "",
      last_name: "",
    };
  },
  methods: {
    regist: axios
      .post("/reg_shain_data")
      .then(function () {})
      .catch((err) => {
        console.log(err);
      }),
  },
};
</script>
