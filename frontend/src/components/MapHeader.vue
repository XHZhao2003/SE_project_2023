<template>
  <div id="mapHeader">
    <div id="logo">
      <img id="logoImg" src="../assets/ERoad-logo.png" />
    </div>

    <div id="selector">
      <el-select-v2 v-model="value" :options="options" placeholder="功能" style="width: 150px" multiple />
      <el-select-v2 v-model="value" :options="options" placeholder="地点" style="width: 150px" multiple />
      <el-select-v2 v-model="value" :options="options" placeholder="时间" style="width: 150px" multiple />
      <el-button type="primary" icon="Search">Search</el-button>
    </div>

    <div id="postButton">
      <el-button type="primary" icon="Edit" style="width: 120px; height: 50px">
        发布
      </el-button>
    </div>
    <div id="avatar"><Avatar/></div>
    
  </div>
</template>

<script>
import Avatar from "./Avatar.vue";

export default {
  data() {
    return {
      value: "",
      options: [
        { value: 1, label: 1 },
        { value: 2, label: 2 },
      ],
    };
  },
  components: {
    Avatar,
  },
};
</script>

<style>
#mapHeader {
  display: flex;
  align-items: center;
  position: absolute;
  top: 0%;
  left: 5px;
  width: 100%;
  height: 100px;
  z-index: 1;
  margin: 0px;
  padding: 0px;

}
#logo {
  height: 100%;
  margin-right: 250px;
}
#logoImg {
  height: 100%;
  object-fit: contain;
}
#selector {
  height: 100px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin-right: 50px;
}
#postButton {
  margin-left: 200px;
}
#avatar {
  margin-right: 35px;
  margin-left: 60px;
}
</style>