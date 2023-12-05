<template>
    <div id="roadname">{{ str }}</div>
    <div id="closebutton">
        <el-button type="danger" circle icon="Close" color="aliceblue" @click="close"/>
    </div>
    <div style="height: 30px; text-align: left; padding: auto; font-size: 18px;">拥挤指数</div>
    <div id="progressbar">
        <el-progress :percentage=num :stroke-width="25" :show-text="false" :color="color" />
    </div>
    <el-divider />
    <div id="description">
        {{Percentage2Text(num)}}
    </div>

    <div  style="width: 300px; height: 200px; text-align: center">
        <div style="font-size: 15px; text-align: left; height: 30px">
            选择实时路况,感谢您的反馈！
        </div>
        <el-button id="feedbackbutton" color="#46bc1d" @click="FeedBack(1)">
            良好
        </el-button>
        <el-button id="feedbackbutton" color="#dfe534" @click="FeedBack(2)">
            适中
        </el-button>
        <el-button id="feedbackbutton" color="#df7401" @click="FeedBack(3)">
            拥堵
        </el-button>
        <el-button id="feedbackbutton" color="#ff3333" @click="FeedBack(4)">
            严重拥堵
        </el-button>
    </div>
</template>

<script>
export default{
    name: "Roadsidebar",
    emits: ['close-road'],
    props:{
        str: String,
        num: Number,
    },
    methods:{
        Percentage2Text(percentage) {
            if (percentage <= 20) {
                return "路况良好，顺畅通行！";
            } else if (percentage <= 40) {
                return "路况适中，您可以从这里通行";
            } else if (percentage <= 60) {
                return "道路拥挤，您最好选择绕行";
            } else {
                return "严重堵塞，您不会想来这里的！";
            }
        },
        color(percentage){
            if(percentage <= 25){
                return "#46bc1d";
            }else if(percentage <= 50){
                return "#dfe534";
            }else if(percentage <= 75){
                return "#df7401";
            }else{
                return "#ff3333";
            }
        },
        close(){
            this.$emit('close-road')
        }
    }
};
</script>

<style>
#roadname {
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