<template>
  <div id="mapHeader">
    <div id="logo">
      <img id="logoImg" src="../assets/ERoad-logo.png" />
    </div>

    <div id="selector">
      <el-select-v2 v-model="value1" :options="options1" placeholder="功能" style="width: 150px" multiple />
      <el-select-v2 v-model="value2" :options="options2" placeholder="地点" style="width: 150px" multiple />
      <el-select-v2 v-model="value3" :options="options3" placeholder="时间" style="width: 150px" multiple />
      <el-button type="primary" icon="Search" @click="handleChange">Search</el-button>
    </div>

    <el-aside v-if="drawer" id="asideinfo">
      <div id="closebutton">
        <el-button type="danger" circle icon="Close" color="aliceblue" @click="close"/>
      </div>
    <el-table v-if="drawer" :data="tableData" id="table" stripe style="width: 100%">
      <el-table-column prop="id" label="ID" width="180"></el-table-column>
      <el-table-column prop="name" label="名称" width="180"></el-table-column>
      <el-table-column prop="star" label="推荐指数" width="180"></el-table-column>
    </el-table>
    </el-aside>

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
      value1: "",
      value2: "",
      value3: "",
      options1: [
        { value: 1, label: "食堂" },
        { value: 2, label: "教学楼" },
        { value: 3, label: "小卖部" },
      ],
      options2: [
        { value: 1, label: "31楼附近" },
        { value: 2, label: "二教附近" },
        { value: 3, label: "东南门附近" },
      ],
      options3: [
        { value: 1, label: "8：00-12：00" },
        { value: 2, label: "12：00-18：00" },
        { value: 3, label: "18：00-24：00" },
      ],
      drawer: false,
      radio: "",
      tableData: [
        {
          id: 1,
          name: "家园食堂",
          star: 5
        },
        {
          id: 2,
          name: "学一食堂",
          star: 5
        },
        {
          id: 3,
          name: "松林餐厅",
          star: 5
        }
      ]
    };
  },
  components: {
    Avatar,
  },
  methods: {
    handleChange() {
      // 判断用户的选择是否满足条件
      if (
        this.value1.includes(1) &&
        this.value2.includes(1) &&
        this.value3.includes(1)
      ) {
        // 如果满足条件，就显示侧边栏
        this.drawer = true;
      } else {
        // 如果不满足条件，就隐藏侧边栏
        this.drawer = false;
      }
    },
    close(){
      this.drawer = false;
    },
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
#asideinfo {
  position: absolute;
  z-index: 99;
  top: 95px;
  left: 35%;
  height: 200px;
  width: 30%;
  background-color: aliceblue;
  text-align: center;
}
#closebutton {
  position: absolute;
  right: 10px;
  top: 10px;
}
#feedbackbutton {
  width: 100%;
  margin: 0px;
}
#table {
  position: absolute;
  z-index: 99;
  top: 30px;
  left: 0%;
  height: 300px;
  width: 100%;
  text-align: center;
  background-color: lightblue;
}
</style>