<template>
  <div id="venuename" style="height: 60px; text-align: center; padding-top: 10px; font-size: 30px; font-weight: bold;">
    {{this.name}}
  </div>
  <div id="closebutton">
    <el-button type="danger" circle icon="Close" color="aliceblue" @click="close" />
  </div>

  <div id="opening-hours">
    <el-scrollbar height="100px">
      <div style="font-size: 20px; text-align: left; height: 30px; font-weight: bold; padding-left: 10px;">
        营业时间
      </div>
      <div style="text-align: left; margin-left: 30px;">
        {{this.opening_hours}}
      </div>
    </el-scrollbar>
  </div>

  <div id="Description">
    <div style="font-size: 20px; text-align: left; padding-top: 10px; height: 30px; font-weight: bold; padding-left: 10px;">
      简介
    </div>
    <div style="text-align: left; margin-left: 30px;">
      {{this.description}}
    </div>
  </div>

  <div id="tags" style="padding-top: 10px">
    <el-tag>食堂</el-tag>
    <el-tag>31楼附近</el-tag>
    <el-tag>0700 - 2300</el-tag>
  </div>

  <div id="conmentBox">
    <div style="font-size: 20px; text-align: left; padding-top: 10px; height: 30px; font-weight: bold; padding-left: 10px;">
      评论区
    </div>
    <el-scrollbar height="250px">
      <div v-for="comment in this.comments" class="commentItem">
        <div style="text-align: left; margin-left: 20px;">
          {{comment.username}}
        </div>
        <el-scrollbar height="80px">
          <div style="text-align: left; margin-left: 30px;">
            {{comment.content}}
          </div>
        </el-scrollbar>
      </div>
    </el-scrollbar>
  </div>

  <el-button type="primary" style="width: 200px; margin-top: 30px;" @click="showCommentDialog = true">
    发送评论
  </el-button>

  <el-dialog v-model="showCommentDialog">
    <div style="text-align: center; margin-bottom: 10px; font-size: 25px; font-weight: bold;">
      {{this.name}}
    </div>
    <el-input v-model="input" :rows="10" type="textarea" placeholder="Please input" style="margin-bottom: 10px;" />

    <div>
      <el-button type="primary" style="width: 150px;" @click="SendComment">发送</el-button>
    </div>

  </el-dialog>

</template>

<script>
import { ElTag, ElInput, ElSkeleton } from "element-plus";
import { ref } from "vue";
import axios from "axios";

export default {
  name: "Venuesidebar",
  emits: ["close-venue"],
  props: {
    id: Number,
  },
  data() {
    return {
      name: "",
      id: 0,
      opening_hours: "",
      description: "",
      comments: [
        {
          content: "暂时没有评论",
          username: "",
          timestamp: "",
        },
      ],
      tags: "",
      input: "",
      showCommentDialog: false,
      searchResult: []
    };
  },
  methods: {
    async GetVenue(id) {
      var senddata = {
        action: "get_location_by_id",
        id: id,
      };
      await axios
        .post("http://127.0.0.1:8000/api/Location/", senddata)
        .then((res) => {
          // update info
          this.name = res.data.name
          this.id = res.data.id
          this.opening_hours = res.data.opening_hours
          this.description = res.data.description
          if (res.data.comments.length > 0) {
            this.comments = res.data.comments
          } else {
            this.comments = [
              {
                content: "暂时没有评论",
                username: "",
                timestamp: "",
              },
            ];
          }
          this.tags = res.data.tags;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async SendComment() {
      var senddata = {
        action: "post_comment",
        id: this.id,
        content: this.input,
        username: localStorage.getItem("username"),
      };
      await axios
        .post("http://127.0.0.1:8000/api/Location/", senddata)
        .then((res) => {
          ElMessage({
              message: "发送成功!",
              type: "success",
            });
        })
        .catch((error) => {
          console.log(error);
        });
      this.showCommentDialog = false
    },
    close() {
      this.$emit("close-venue");
    },
    async Search(tags){
      var senddata = {
        action: "search_location",
        tags: tags,
      }
      await axios
        .post("http://127.0.0.1:8000/api/Location/", senddata)
        .then((res) => {
          console.log(res)
          this.searchResult = res.data
        })
        .catch((error) => {
          console.log(error);
        });
    }
  },
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
#commentBox {
  height: 150px;
}
.commentItem {
  margin-left: 20px;
  margin-right: 20px;
  margin-top: 8px;
  margin-bottom: 8px;
  border-radius: 10px;
  box-shadow: 5px 5px 3px 3px lightgray;
  background-color: blanchedalmond;
}
</style>