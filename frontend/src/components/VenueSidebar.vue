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
      <div id="opening-hours-content" style="text-align: left; margin-left: 30px;">
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

  <div id="tags" style="padding-top: 10px; display: flex; justify-items: left;">
    <span v-for="tag1 in this.tags[0]" style="margin-left: 20px; margin-right: 5px;">
      <el-tag>{{this.Tag12String(tag1)}}</el-tag>
    </span>
    <span v-for="tag2 in this.tags[1]">
      <el-tag>{{this.Tag22String(tag2)}}</el-tag>
    </span>
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

  <div style="margin-top: 30px;">
    <el-pagination v-show="showSearchResult" v-model:current-page="currentPage" layout="prev, pager, next" :pager-count="5" :page-count="searchResultLength" :hide-on-single-page="true" small=true @current-change="UpdatePage" background style="justify-content: center;" />
  </div>

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
import { ElTag, ElInput, ElMessage } from "element-plus";
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
      showSearchResult: false,
      searchResult: [],
      currentPage: 1,
      searchResultLength: 0,
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
          this.name = res.data.name;
          this.id = res.data.id;
          this.opening_hours = res.data.opening_hours;
          this.description = res.data.description;
          if (res.data.comments.length > 0) {
            this.comments = res.data.comments;
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
          this.showSearchResult = false;
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
      this.showCommentDialog = false;
    },
    close() {
      this.showSearchResult = false;
      this.currentPage = 1;
      this.searchResultLength = 0;
      this.$emit("close-venue");
    },
    async Search(tags) {
      var senddata = {
        action: "search_location",
        tags: tags,
      };
      await axios
        .post("http://127.0.0.1:8000/api/Location/", senddata)
        .then((res) => {
          this.searchResult = res.data.result;
          if (this.searchResult.length === 0) {
            ElMessage({
              message: "没有找到符合条件的结果",
              type: "warning",
            });
          } else {
            this.searchResultLength = this.searchResult.length;
            this.showSearchResult = true;
            this.UpdatePage();
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    UpdatePage() {
      var venue = this.searchResult[this.currentPage - 1];
      this.name = venue.name;
      this.opening_hours = venue.opening_hours;
      this.description = venue.description;
      if (venue.comments.length > 0) {
        this.comments = venue.comments;
      } else {
        this.comments = [
          {
            content: "暂时没有评论",
            username: "",
            timestamp: "",
          },
        ];
      }
      this.tags = venue.tags;
    },
    Tag12String(tag1) {
      var func = ["", "商店", "食堂", "教室", "自习", "打印", "办公室", "运动"];
      return func[tag1];
    },
    Tag22String(tag2) {
      var place = [
        "",
        "宿舍区西",
        "宿舍区东",
        "教学楼区",
        "五四操场",
        "静园",
        "校园北部",
      ];
      return place[tag2];
    },
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