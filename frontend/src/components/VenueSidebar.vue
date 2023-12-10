<template>
  <div id="Venue Name">{{ str }}</div>
  <div id="closebutton">
      <el-button type="danger" circle icon="Close" color="aliceblue" @click="close"/>
  </div>
  


  <div  style="width: 300px; height: 200px; text-align: center">
    <div id="description"> {{ str }} </div>
      
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
  methods:{
     
      close(){
          this.$emit('close-venue')
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
font-size: 25px;
font-weight: bold;
}
#closebutton {
position: absolute;
right: 10px;
top: 10px;
}
#progressbar {
height: 60px;
padding-top: 10px;
width: 280px;
overflow: hidden;
}
#feedbackbutton {
width: 250px;
margin: 5px;
}
#description {
width: 300px;
height: 60px;
text-align: left;
font-size: 15px;
padding-left: 10px;
}
</style>