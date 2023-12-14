<template>
  <div>
    <el-container>
      <el-header height="90px">
        <MapHeader ref="mapheader" 
        @search="Search"
        @showRoadLayer="ShowRoadLayer"
        @showVenueLayer="ShowVenueLayer"
        @closeRoadLayer="CloseRoadLayer"
        @closeVenueLayer="CloseVenueLayer" />
      </el-header>
      <el-container>
        <el-main style="overflow: hiddens; height: 700px; width: auto;margin:0px; padding: 0px;">
          <!-- 高德地图容器 -->
          <div id="container"></div>
        </el-main>
      </el-container>
    </el-container>
  </div>

  <transition>
    <el-aside v-if="ShowRoadFlag" class="asideinfo">
      <Roadsidebar :name="Roads.name[RoadInfoId - 1]" :crowding="crowding" :road_id="RoadInfoId" @close-road="CloseRoad" />
    </el-aside>
  </transition>
  <transition>
    <el-aside v-show="showVenueFlag" class="asideinfo">
      <!-- 这里设计成让子组件请求数据，v-if在mount阶段组件还不存在，也获取不到ref，改成v-show -->
      <Venuesidebar ref="venueComponent" :id="venueInfoId" @close-venue="CloseVenue" />
    </el-aside>
  </transition>

</template>
  
<script>
import { MapKey, MapSecretKey } from "../config/mapConfig";
//高德API加载器 安装命令： npm i @amap/amap-jsapi-loader
import AMapLoader from "@amap/amap-jsapi-loader";
import { Close, Edit, Search } from "@element-plus/icons-vue";
import { ElMessage } from "element-plus";
import axios from "axios";
import { ref } from "vue";
import Roadsidebar from "./Roadsidebar.vue";
import MapHeader from "./MapHeader.vue";
import Venuesidebar from "./Venuesidebar.vue";

export default {
  data() {
    return {
      Roads: "",
      venues: "",
      RoadPolylines: [],
      venueMarkers: [],
      ShowRoadFlag: false, // 侧边展示路况
      showVenueFlag: false, // 侧边展示生活指南
      RoadInfoId: 0, // 当前展示的路段id
      venueInfoId: 0, // 当前展示地点数据结构
      crowding: 0, // 用来显示的拥挤指数
    };
  },
  methods: {
    async InitMap() {
      const initMap = new Promise((resolve, reject) => {
        AMapLoader.load({
          key: `${MapKey}`,
          version: "1.4.15",
          plugins: ["AMap.ToolBar", "AMap.Scale"],
        })
          .then((AMap) => {
            map = new AMap.Map("container", {
              //设置地图容器id
              viewMode: "3D", //是否为3D地图模式
              pitch: 70,
              zoom: 16,
              center: [116.31088, 39.99281],
            });
            toolbar = new AMap.ToolBar({ position: "LT" });
            map.addControl(toolbar);
            scale = new AMap.Scale();
            map.addControl(scale);

            // add roads
            var num_of_road = this.Roads.id.length;
            for (var i = 0; i < num_of_road; i++) {
              var _path = [];
              var num_of_point = this.Roads.points[i].length;
              for (var j = 0; j < num_of_point; j++) {
                _path.push(
                  new AMap.LngLat(
                    this.Roads.points[i][j][0],
                    this.Roads.points[i][j][1]
                  )
                );
              }
              var polyline = new AMap.Polyline({
                path: _path,
                strokeWeight: 6, // 线条宽度，默认为 1
                strokeColor: "#c2c2c2", // 线条颜色
                extdata: {
                  id: i + 1,
                },
              });

              map.add(polyline);
              polyline.on("click", (event) => {
                var _id = event.target.w.extdata.id;
                this.ShowRoad(_id);
              });
              this.RoadPolylines[i] = polyline;
              this.RoadPolylines[i].hide()
            }

            // add venues
            var num_of_venues = this.venues.length;
            for (var i = 0; i < num_of_venues; i++) {
              var marker = new AMap.Marker({
                position: [this.venues[i].x, this.venues[i].y],
                extdata: {
                  id: i + 1,
                },
              });
              marker.on("click", (event) => {
                var _id = event.target.w.extdata.id;
                this.ShowVenue(_id);
              });
              map.add(marker);
              this.venueMarkers[i] = marker
              this.venueMarkers[i].hide()
            }

            //bound the region
            var options = {
              areas: [
                {
                  // visible: false, // 是否可见
                  rejectTexture: true, // 是否屏蔽自定义地图的纹理
                  path: [
                    [
                      [116.303959, 39.997705],
                      [116.309087, 40.000302],
                      [116.315761, 40.000319],
                      [116.317306, 39.985852],
                      [116.304946, 39.985524],
                    ],
                  ],
                },
              ],
            };
            // 外多边形坐标数组和内多边形坐标数组
            var outer = [
              new AMap.LngLat(-360, 90, true),
              new AMap.LngLat(-360, -90, true),
              new AMap.LngLat(360, -90, true),
              new AMap.LngLat(360, 90, true),
            ];
            var pathArray = [outer];
            pathArray.push.apply(pathArray, options.areas[0].path); // options.areas[0].path 外部区域 遮罩
            // pathArray = [ outer ] // 整个地图遮罩
            // pathArray = options.areas[0].path // options.areas[0].path 内部区域 遮罩

            new AMap.Polygon({
              path: pathArray,
              map: map,
              bubble: true,
              fillColor: "rgba(256,256,256)", // 多边形填充颜色
              fillOpacity: 1, // 多边形填充透明度，默认为0.9
              strokeColor: "rgba(38,127,204)", // 线条颜色
              strokeWeight: 5,
              strokeOpacity: 1.0, // 轮廓线透明度，默认为0.9
              strokeStyle: "solid", // 轮廓线样式，实线:solid，虚线:dashed
              /*勾勒形状轮廓的虚线和间隙的样式，此属性在strokeStyle 为dashed 时有效， 此属性在
            ie9+浏览器有效 取值：
            实线：[0,0,0]
            虚线：[10,10] ，[10,10] 表示10个像素的实线和10个像素的空白（如此反复）组成的虚线
            点画线：[10,2,10]， [10,2,10] 表示10个像素的实线和2个像素的空白 + 10个像素的实
            线和10个像素的空白 （如此反复）组成的虚线*/
              strokeDasharray: [10, 2, 10],
            });

            resolve();
          })
          .catch((e) => {
            //操作失败
            reject(e);
          });
      });

      // initMap
      //   .then((ok) => {
      //     initPlugins();
      //   })
      //   .catch((err) => {
      //     console.log(err);
      //   });
    },
    async InitRoad() {
      let senddata = {
        action: "get_all",
      };
      await axios
        .post("http://127.0.0.1:8000/api/Road/", senddata)
        .then((res) => {
          this.Roads = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async InitVenue() {
      let senddata = {
        action: "get_all_locations",
      };
      await axios
        .post("http://127.0.0.1:8000/api/Location/", senddata)
        .then((res) => {
          this.venues = res.data.locations;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // 点击Road Polyline触发的函数
    ShowRoad(id) {
      if (this.RoadInfoId !== 0) {
        this.CloseRoad();
      }
      if (this.VenueInfoId != 0) {
        this.CloseVenue();
      }
      this.ShowRoadFlag = true;
      this.RoadInfoId = id;

      // get crowding from backend
      let senddata = {
        action: "get_road_crowding",
        id: id,
      };
      axios
        .post("http://127.0.0.1:8000/api/Road/", senddata)
        .then((res) => {
          // updata color
          var polyline = this.RoadPolylines[id - 1];
          this.crowding = res.data.feedback;
          var color = this.Crowd2Color(this.crowding);
          polyline.setOptions({
            strokeColor: color,
          });
        })
        .catch((error) => {
          console.log(error);
        });
    },
    CloseRoad() {
      var polyline = this.RoadPolylines[this.RoadInfoId - 1];
      polyline.setOptions({
        strokeColor: "#c2c2c2",
      });
      this.ShowRoadFlag = false;
      this.RoadInfoId = 0;
    },
    async ShowVenue(id) {
      if (this.RoadInfoId != 0) {
        this.CloseRoad();
      }
      if (this.venueInfoId != 0) {
        this.CloseVenue();
      }
      this.showVenueFlag = true;
      this.venueInfoId = id;
      // 子组件自己获取数据
      await this.$refs.venueComponent.GetVenue(id);
    },
    CloseVenue() {
      this.showVenueFlag = false;
      this.venueInfoId = 0;
    },
    FeedBack(type) {
      // Post something to backend..
      this.InitRoad();
      ElMessage({
        message: "反馈成功!",
        type: "success",
      });
      this.CloseFeedBack();
    },
    Crowd2Color(crowding) {
      if (crowding === 4) return "#ff3333";
      else if (crowding === 3) return "#df7401";
      else if (crowding === 2) return "#dfe534";
      else return "#46bc1d";
    },
    async Search() {
      var header = this.$refs.mapheader;
      var tags = header.getTags();
      await this.$refs.venueComponent.Search(tags);
      if(this.$refs.venueComponent.searchResultLength > 0){
        this.showVenueFlag = true;
      }
    },
    ShowRoadLayer(){
      for(var roadPolyline of this.RoadPolylines){
        roadPolyline.show()
      }
    },
    CloseRoadLayer(){
      for(var roadPolyline of this.RoadPolylines){
        roadPolyline.hide()
      }
    },
    ShowVenueLayer(){
      for(var venueMarker of this.venueMarkers){
        venueMarker.show()
      }
    },
    CloseVenueLayer(){
      for(var venueMarker of this.venueMarkers){
        venueMarker.hide()
      }
    }
  },
  components: {
    MapHeader,
    Roadsidebar,
    Venuesidebar,
  },
  mounted: async function () {
    await this.InitRoad();
    await this.InitVenue();
    await this.InitMap();
  },
};

//工具条显示隐藏
function toolbarView(s) {
  s ? toolbar.show() : toolbar.hide();
}
function scaleView(s) {
  s ? scale.show() : scale.hide();
}

// 地图容器
var map;
//工具条控件
var toolbar;
//比例尺控件
var scale;
//图层切换控件
var mapType;
//定位控件
var geolocation;

//异步加载多个插件
function initPlugins() {
  AMap.plugin(["AMap.MapType", "AMap.Geolocation"], function () {
    // 在图面添加类别切换控件，实现默认图层与卫星图、实施交通图层之间切换的控制
    mapType = new AMap.MapType({});
    // 在图面添加定位控件，用来获取和展示用户主机所在的经纬度位置
    geolocation = new AMap.Geolocation({
      buttonPosition: "LB",
      showButton: true, //是否显示定位
    });
  });
  map.addControl(mapType);
  map.addControl(geolocation);
}
</script>

<style scoped>
#container {
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  width: 100%;
  height: 100%;
  margin: 0px;
  padding: 0px;
}
.asideinfo {
  position: absolute;
  z-index: 99;
  top: 95px;
  left: 80%;
  height: 705px;
  width: 20%;
  background-color: aliceblue;
  text-align: center;
}
#header {
  height: 100px;
  width: 1550px;
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  align-items: center;
  justify-content: flex-end;
  margin: 0px;
  padding: 0px;
}
#selector {
  height: 100px;
  width: 1000px;
  margin-right: auto;
  margin-left: auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
#avatar {
  height: 100px;
  width: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* 侧边栏的动画 */
.v-enter-active,
.v-leave-active {
  transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
  opacity: 0;
}
</style>
  