<template>
  <div id="venuename" style="height: 60px; text-align: center; padding-top: 10px; font-size: 30px; font-weight: bold;">家园食堂</div>
  <div id="closebutton">
      <el-button type="danger" circle icon="Close" color="aliceblue" @click="close"/>
  </div>
  
  <div id="opening-hours">
    <div style="font-size: 20px; text-align: left; height: 30px; font-weight: bold; padding-left: 10px;">
      营业时间
    </div>
      一层：早餐 0700 - 1000 午餐 1100 - 1300 晚餐 1700 - 1900 <br>
      二层：午餐 1100 - 1300 晚餐 1700 - 1900 <br>
      三层与四层：1000 - 2300 
  </div>

  <div id="Description">
    <div style="font-size: 20px; text-align: left; padding-top: 10px; height: 30px; font-weight: bold; padding-left: 10px;">
      地点简介
    </div>
      北京大学燕园校区内最大的食堂
  </div>

  <div id="Comments">
    <div style="font-size: 20px; text-align: left; padding-top: 10px; height: 30px; font-weight: bold; padding-left: 10px;">
      评论区
    </div>
    <el-skeleton :rows="6" animated />
    <el-input
      placeholder="Please input"
      v-model="input"
      clearable>
    </el-input>
  </div>

  <div id="tags" style="padding-top: 10px">
    <el-tag>食堂</el-tag>
    <el-tag>31楼附近</el-tag>
    <el-tag>0700 - 2300</el-tag>
  </div>

</template>

<script>

export default{
  name: "VenueSidebar",
  emits: ['close-venue'],
  props:{
      str: String,
      num: Number,
  },
  data() {
    return {
      input: ''
    }
  }
};
</script>

<style>
#venuename {
width: 300px;
height: 60px;
text-align: center;
padding-top: 10px;
font-size: 30px;
font-weight: bold;
}
#closebutton {
position: absolute;
right: 10px;
top: 10px;
}

#description {
  font-size: 20px; 
  text-align: left; 
  padding-top: 10px; 
  height: 30px; 
}
</style>