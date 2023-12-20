<script setup>
import { ElMessage, ElProgress, ElButton, ElDivider } from "element-plus";
import axios from "axios";

</script>


<template>
  <div id="roadname">{{ name }}</div>
  <div id="closebutton">
    <el-button type="danger" circle icon="Close" color="aliceblue" @click="close" />
  </div>
  <div style="height: 30px; text-align: left; padding-left: 15px; font-size: 18px;">拥挤指数</div>
  <div id="progressbar">
    <el-progress :percentage="Crowding2Percentage(crowding)" :stroke-width="25" :show-text="false"/>
  </div>
  <el-divider />
  <div id="description">
    {{Percentage2Text(Crowding2Percentage(crowding))}}
  </div>

  <div v-if="ShowFeedBackFlag" style="width: 400px; height: 200px; text-align: center">
    <div style="font-size: 18px; text-align: left; height: 30px; padding-top: 20px; padding-left: 15px; padding-bottom: 10px;">
      选择实时路况
    </div>
    <div class="feedbackbutton">
      <el-button style="width: 250px;" color="#46bc1d" @click="FeedBack(1)">
        良好
      </el-button>
    </div>
    <div class="feedbackbutton">
      <el-button style="width: 250px;" color="#dfe534" @click="FeedBack(2)">
        适中
      </el-button>
    </div>
    <div class="feedbackbutton">
      <el-button style="width: 250px;" color="#df7401" @click="FeedBack(3)">
        拥堵
      </el-button>
    </div>
    <div class="feedbackbutton">
      <el-button style="width: 250px;" color="#ff3333" @click="FeedBack(4)">
        严重拥堵
      </el-button>
    </div>

    <div style="text-align: right">
      <el-button type="text" @click="CloseFeedBack" style="width: 50px; margin-right: 30px;">
        返回
      </el-button>
    </div>
  </div>
  <el-button id="openFeedbackButton" v-else="ShowFeedBackFlag" type="primary" @click="ShowFeedBack" style="width: 250px; margin: 30px">
    反馈实时路况
  </el-button>
</template>

<script>

export default {
  name: "Roadsidebar",
  emits: ["close-road"],
  props: {
    name: String,
    crowding: Number,
    road_id: Number,
  },
  data() {
    return {
      ShowFeedBackFlag: false,
    };
  },
  methods: {
    Crowding2Percentage(crowding){
      return crowding * 20
    },
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
    color(percentage) {
      if (percentage <= 20) {
        return "#46bc1d";
      } else if (percentage <= 40) {
        return "#dfe534";
      } else if (percentage <= 60) {
        return "#df7401";
      } else {
        return "#ff3333";
      }
    },
    close() {
      this.$emit("close-road");
    },
    ShowFeedBack() {
      this.ShowFeedBackFlag = true;
      console.log("here");
    },
    CloseFeedBack() {
      this.ShowFeedBackFlag = false;
    },
    FeedBack(type) {
      var senddata = {
        action: "feedback_road_crowding",
        id: this.road_id,
        road_crowding: type - 1,
      };
      axios
        .post(this.SERVER + "/api/Road/", senddata)
        .then((res) => {
          console.log(res)
          var status = res.data.msg
          if (status === "feedback success") {
            ElMessage({
              message: "反馈成功!",
              type: "success",
            });
            this.CloseFeedBack();
          } else {
            console.log(res.data.msg);
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
#roadname {
  width: 300px;
  height: 60px;
  text-align: center;
  padding-left: 30px;
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
  width: 320px;
  overflow: hidden;
  margin-left: 20px;
  margin-right: 20px;
}
.feedbackbutton {
  margin-left: 60px;
  justify-self: center;
  width: 250px;
  margin-bottom: 10px;
}
#description {
  width: 300px;
  height: 60px;
  text-align: left;
  font-size: 20px;
  padding-left: 20px;
}
</style>