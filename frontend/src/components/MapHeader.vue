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

    <div id="layerOption" style="display: flex; flex-direction: column;">
      <el-checkbox v-model="showRoad" style="margin-bottom: 5px; width: 100px;" label="路况" @change="UpdateRoadLayer" ref="layer1" border />
      <el-checkbox v-model="showVenue" style="width: 100px;" label="生活指南" @change="UpdateVenueLayer" ref="layer2" border />
    </div>
    <div id="avatar"><Avatar/></div>
    
  </div>
</template>

<script>
import { ElMessage } from 'element-plus';
import Avatar from "./Avatar.vue";

export default {
  emits: ['search', 'showRoadLayer', 'closeRoadLayer', 'showVenueLayer', 'closeVenueLayer'],
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
      showRoad: false,
      showVenue: false
    };
  },
  components: {
    Avatar,
  },
  methods: {
    Search(){
      // 用户必须指定至少一个功能
      if(this.value1.length === 0){
        ElMessage({
          message: "必须指定一个功能",
          type: "warning"
        })
      }
      else{
        this.$emit('search')
      }
    },
    getTags(){
      return [this.value1, this.value2, this.value3]
    },
    UpdateRoadLayer(){
      if(this.showRoad){
        this.$emit('showRoadLayer')
      }
      else{
        this.$emit('closeRoadLayer')
      }
    },
    UpdateVenueLayer(){
      if(this.showVenue){
        this.$emit('showVenueLayer')
      }
      else{
        this.$emit('closeVenueLayer')
      }
    }
  },
  mounted: function(){
    this.showRoad = true
  }
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
#layerOption {
  margin-left: 150px;
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