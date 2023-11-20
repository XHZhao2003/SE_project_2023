<template>
  <div style="height: 100%; width: 100%">
    <el-container style="height: 100%; width: 100%">
      <el-header style="background-color: white" height="100px">
        this is a header
      </el-header>
      <el-container>
        <el-main style="overflow: hiddens; height: 700px">
          <!-- 高德地图容器 -->
          <div id="container"></div>
        </el-main>
        <Transition>
        <el-aside
          v-if="ShowRoadFlag"
          id="asideinfo"
          style="background-color: aliceblue; text-align: center"
        >
          <div
            style="
              width: 300px;
              text-align: center;
              font-size: 25px;
              font-weight: bold;
            "
          >
            This is a Road
          </div>

          <div style="position: absolute; right:10px; top:10px">
            <el-button type="danger" circle icon="Close" color="aliceblue"
            @click="CloseRoad"></el-button>
          </div>

          <div style="height: 30px">拥挤指数</div>

          <el-progress
            :percentage="crowded"
            :stroke-width="20"
            :format="Percentage2Text"
          />

          <div
            style="
              width: 300px;
              height: 60px;
              text-align: left;
              font-size: 15px;
            "
          >
            路况良好，适合通行
          </div>

          <div
            v-if="ShowFeedbackFlag"
            style="width: 300px; height: 200px; text-align: center"
          >
            <div style="font-size: 15px; text-align: left; height: 30px">
              选择实时路况
            </div>
            <el-button
              type="primary"
              @click="FeedBack(1)"
              style="width: 250px; margin: 5px"
            >
              良好
            </el-button>
            <el-button
              type="primary"
              @click="FeedBack(2)"
              style="width: 250px; margin: 5px"
            >
              适中
            </el-button>
            <el-button
              type="primary"
              @click="FeedBack(3)"
              style="width: 250px; margin: 5px"
            >
              拥堵
            </el-button>
            <el-button
              type="primary"
              @click="FeedBack(4)"
              style="width: 250px; margin: 5px"
            >
              严重拥堵
            </el-button>

            <div style="text-align: right">
              <el-button type="text" @click="CloseFeedBack" style="width: 50px">
                返回
              </el-button>
            </div>
          </div>
          
          <el-button
            v-else="ShowFeedBack"
            type="primary"
            @click="ShowFeedBack"
            style="width: 250px; margin: 30px"
          >
            反馈实时路况
          </el-button>
        </el-aside>
        </Transition>
      </el-container>
    </el-container>
  </div>
</template>
  
<script>
import { MapKey, MapSecretKey } from "../config/mapConfig";
//高德API加载器 安装命令： npm i @amap/amap-jsapi-loader
import AMapLoader from "@amap/amap-jsapi-loader";
import { Close } from "@element-plus/icons-vue";
import { ElMessage } from 'element-plus'
import { onBeforeMount, onMounted, ref } from "vue";

export default {
  data() {
    return {
      ShowRoadFlag: true,
      RoadInfoId: "",
      ShowFeedbackFlag: false,

      crowded: 20,
    };
  },
  methods: {
    ShowRoad(id) {
      this.ShowRoadFlag = true;
      this.RoadInfoId = id;
    },
    CloseRoad(){
      this.ShowRoadFlag = false;
      this.RoadInfoId = ""
    },
    InitMap() {
      // Map组件本身，下面箭头函数使用
      let that = this;

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

            var polyline1 = new AMap.Polyline({
              path: [
                new AMap.LngLat(116.30722, 39.98872),
                new AMap.LngLat(116.308336, 39.988757),
              ],
              strokeWeight: 6, // 线条宽度，默认为 1
              strokeColor: "rgb(0,128,0)", // 线条颜色
            });
            polyline1.on("mouseover", () => {
              polyline1.setOptions({
                strokeColor: "rgb(0,255,0)",
              });
            });
            polyline1.on("mouseout", () => {
              polyline1.setOptions({
                strokeColor: "rgb(0,128,0)",
              });
            });
            map.add(polyline1);
            AMap.event.addListener(polyline1, "click", function () {
              that.ShowRoad(1);
            });

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

      initMap
        .then((ok) => {
          initPlugins();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    Percentage2Text(percentage) {
      return "适中";
    },
    ShowFeedBack() {
      this.ShowFeedbackFlag = true;
    },
    CloseFeedBack() {
      this.ShowFeedbackFlag = false;
    },
    FeedBack(type) {
      console.log(type);
      ElMessage({
        message:"反馈成功!",
        type:'success'
      })
      this.CloseFeedBack();
    },
  },
  mounted: function () {
    this.InitMap();
  },
};

// window._AMapSecurityConfig = {
//   securityJsCode: `${MapSecretKey}`,
// };

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
  position: fixed;
  top: 110px;
  left: 10px;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  width: 1540px;
  height: 700px;
}
#controller {
  position: absolute;
  z-index: 99;
  top: 20px;
  left: 100px;
  background: rgb(255, 255, 255);
  list-style-type: none;
  width: 120px;
}
#asideinfo {
  position: absolute;
  z-index: 99;
  top: 110px;
  left: 80%;
  height: 700px;
  width: 20%;
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
  
