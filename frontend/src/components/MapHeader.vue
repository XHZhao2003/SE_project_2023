<template>
  <div id="mapHeader">
    <div id="logo">
      <img id="logoImg" src="../assets/ERoad-logo.png" />
    </div>
    <div id="selector">
      <el-select-v2 v-model="value1" :options="options1" placeholder="功能" style="width: 180px" multiple collapse-tags="true" clearable="true"/>
      <el-select-v2 v-model="value2" :options="options2" placeholder="地点" style="width: 200px" multiple collapse-tags="true" clearable="true"/>
      <el-select-v2 v-model="value3" :options="options3" placeholder="时间" style="width: 230px" multiple collapse-tags="true" clearable="true" item-height="30" />
      <el-button type="primary" icon="Search" @click="Search">Search</el-button>
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
  emits: ['search'],
  data() {
    return {
      value1: [],
      value2: [],
      value3: [],
      options1: [
        { value: 1, label: "商店" },
        { value: 2, label: "食堂" },
        { value: 3, label: "教室" },
        { value: 4, label: "自习" },
        { value: 5, label: "打印" },
        { value: 6, label: "办公室" },
        { value: 7, label: "图书馆" },
        { value: 8, label: "运动"}
      ],
      options2: [
        { value: 1, label: "宿舍区西" },
        { value: 2, label: "宿舍区东" },
        { value: 3, label: "教学区" },
        { value: 4, label: "五四操场" },
        { value: 5, label: "静园" },
        { value: 6, label: "校园北部" },
        { value: 7, label: "All"}
      ],
      options3: [
        { value: 1, label: "0：00" },
        { value: 2, label: "1：00" },
        { value: 3, label: "2：00" },
        { value: 4, label: "3：00" },
        { value: 5, label: "4：00" },
        { value: 6, label: "5：00" },
        { value: 7, label: "6：00" },
        { value: 8, label: "7：00" },
        { value: 9, label: "8：00" },
        { value: 10, label: "9：00" },
        { value: 11, label: "10：00" },
        { value: 12, label: "11：00" },
        { value: 13, label: "12：00" },
        { value: 14, label: "13：00" },
        { value: 15, label: "14：00" },
        { value: 16, label: "15：00" },
        { value: 17, label: "16：00" },
        { value: 18, label: "17：00" },
        { value: 19, label: "18：00" },
        { value: 20, label: "19：00" },
        { value: 21, label: "20：00" },
        { value: 22, label: "21：00" },
        { value: 23, label: "22：00" },
        { value: 24, label: "23：00" },
        { value: 25, label: "All"}
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
    tagValue2String(){
      var dic1 = {1: "商店", 2: "食堂", 3: "教室", 4: "自习",5: "打印",6: "办公室",7: "图书馆",8: "运动"}
      var dic2 = {1: "宿舍区西", 2:"宿舍区东", 3:"教学区", 4: "五四操场", 5:"静园", 6:"校园北部"}
    },
    handleChange() {
      console.log(this.value1)
      console.log(this.value2)
      console.log(this.value3)
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
    Search(){
      console.log(this.value1)
      this.$emit('search')
    },
    getTags(){
      return [this.value1, this.value2, this.value3]
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
  margin-right: 100px;
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