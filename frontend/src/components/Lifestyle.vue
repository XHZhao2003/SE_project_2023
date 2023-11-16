<template>

  <!-- 高德地图容器 -->
  <div id="container"></div>
  <ul id="controller">
    <li><input type="checkbox" checked @click="toolbarView($event.target.checked)">工具条</li>
    <li><input type="checkbox" checked @click="scaleView($event.target.checked)">比例条</li>
  </ul>
</template>

<script setup>
import {MapKey, MapSecretKey} from "../config/mapConfig"
//高德API加载器 安装命令： npm i @amap/amap-jsapi-loader
import AMapLoader from '@amap/amap-jsapi-loader'
import {onBeforeMount} from "vue";
window._AMapSecurityConfig = {
  securityJsCode: `${MapSecretKey}`,
}


onBeforeMount(() => {
  initMap.then((ok) => {
    initPlugins()
  }).catch((err) => {
    console.log(err)
  })
})

//工具条显示隐藏
function toolbarView(s){
  s?toolbar.show():toolbar.hide()
}
function scaleView(s) {
  s?scale.show():scale.hide()
}



// 地图容器
var map
//工具条控件
var toolbar
//比例尺控件
var scale
//图层切换控件
var mapType
//定位控件
var geolocation

// 初始化地图函数
const initMap = new Promise((resolve, reject) => {
  AMapLoader.load({
    "key": `${MapKey}`,
    "version": "1.4.15",
    "plugins": [
      'AMap.ToolBar',
      'AMap.Scale',
      'AMap.Marker',
    ],
  }).then((AMap) => {
    map = new AMap.Map('container', { //设置地图容器id
      viewMode: "3D",    //是否为3D地图模式
      pitch:70,
      zoom:16,
      center:[116.31088,39.99281],
    })

    toolbar=new AMap.ToolBar({
      position: 'LT'
    })
    map.addControl(toolbar)


    scale=new AMap.Scale()
    map.addControl(scale)


    //----------------add markers and content boxes---------------------//
    var marker_jiayuan = new AMap.Marker({
        position: [116.308148,39.988473],
    })
    map.add(marker_jiayuan);
    var info_jiayuan = new AMap.InfoWindow({
      content: '家园食堂 <br> 营业时间：1000-2200',
      offset: new AMap.Pixel(2, -20)
    });
    AMap.event.addListener(marker_jiayuan, 'click', function () {
      info_jiayuan.open(map, [116.308148,39.988473]);
    });


    var marker_liyi = new AMap.Marker({
        position: [116.312949,39.990931],
    })
    map.add(marker_liyi);
    var info_liyi = new AMap.InfoWindow({
      content: '理科一号楼 <br> 功能：打印、信科教务、健身房等',
      offset: new AMap.Pixel(2, -20)
    });
    AMap.event.addListener(marker_liyi, 'click', function () {
      info_liyi.open(map, [116.312949,39.990931]);
    });


    var marker_lier = new AMap.Marker({
        position: [116.314473,39.990696],
    })
    map.add(marker_lier);
    var info_lier = new AMap.InfoWindow({
      content: '理科二号楼 <br> 功能：?',
      offset: new AMap.Pixel(2, -20)
    });
    AMap.event.addListener(marker_lier, 'click', function () {
      info_lier.open(map, [116.314473,39.990696]);
    });


    var marker_45lou = new AMap.Marker({
        position: [116.305938,39.989155],
    })
    map.add(marker_45lou);
    var info_45lou = new AMap.InfoWindow({
      content: '45号楼 <br> 功能：超市、打印、照相',
      offset: new AMap.Pixel(2, -20)
    });
    AMap.event.addListener(marker_45lou, 'click', function () {
      info_45lou.open(map, [116.305938,39.989155]);
    });


    var marker_tongyuan = new AMap.Marker({
        position: [116.306764,39.991005],
    })
    map.add(marker_tongyuan);
    var info_tongyuan = new AMap.InfoWindow({
      content: '佟园食堂 <br> 营业时间：早餐：0700-0830  午餐：1100-1300   晚餐：1700-2200',
      offset: new AMap.Pixel(2, -20)
    });
    AMap.event.addListener(marker_tongyuan, 'click', function () {
      info_tongyuan.open(map, [116.306764,39.991005]);
    });


    //---------------------end of add markers and content boxes-----------------//


//bound the region
    var options = {
        areas: [{
          // visible: false, // 是否可见
          rejectTexture: true, // 是否屏蔽自定义地图的纹理
          path: [[
          [116.303959,39.997705],
          [116.309087,40.000302],
          [116.315761,40.000319],
          [116.317306,39.985852],
          [116.304946,39.985524]
          ]]
        }]
      }
      // 外多边形坐标数组和内多边形坐标数组
      var outer = [
        new AMap.LngLat(-360, 90, true),
        new AMap.LngLat(-360, -90, true),
        new AMap.LngLat(360, -90, true),
        new AMap.LngLat(360, 90, true),
      ]
      var pathArray = [ outer ]
      pathArray.push.apply(pathArray, options.areas[0].path) // options.areas[0].path 外部区域 遮罩
      // pathArray = [ outer ] // 整个地图遮罩
      // pathArray = options.areas[0].path // options.areas[0].path 内部区域 遮罩

      new AMap.Polygon({
        path: pathArray,
        map: map,
        bubble: true,
        fillColor: 'rgba(256,256,256)', // 多边形填充颜色
        fillOpacity: 1, // 多边形填充透明度，默认为0.9
        strokeColor: 'rgba(38,127,204)', // 线条颜色
        strokeWeight: 5,
        strokeOpacity: 1.0, // 轮廓线透明度，默认为0.9
        strokeStyle: 'solid', // 轮廓线样式，实线:solid，虚线:dashed
        /*勾勒形状轮廓的虚线和间隙的样式，此属性在strokeStyle 为dashed 时有效， 此属性在
          ie9+浏览器有效 取值：
          实线：[0,0,0]
          虚线：[10,10] ，[10,10] 表示10个像素的实线和10个像素的空白（如此反复）组成的虚线
          点画线：[10,2,10]， [10,2,10] 表示10个像素的实线和2个像素的空白 + 10个像素的实
          线和10个像素的空白 （如此反复）组成的虚线*/
        strokeDasharray:[10,2,10]
      })

    resolve()
  }).catch(e => {
    //操作失败
    reject(e)
  })
})

//异步加载多个插件
function initPlugins() {
  AMap.plugin(['AMap.MapType', 'AMap.Geolocation'], function () {
    // 在图面添加类别切换控件，实现默认图层与卫星图、实施交通图层之间切换的控制
    mapType = new AMap.MapType({

    })
    // 在图面添加定位控件，用来获取和展示用户主机所在的经纬度位置
    geolocation = new AMap.Geolocation({
      buttonPosition: 'LB',
      showButton:true //是否显示定位
    })
  })
  map.addControl(mapType)
  map.addControl(geolocation)
}


</script>

<style scoped>
#container {
  position:fixed;
  top:0;
  left:0;
  background-size:cover;
  background-repeat:no-repeat;
  background-position: center center;
  width: 100%; 
  height: 100%;
}
#controller{
  position: absolute;
  z-index: 99;
  top: 20px;
  left: 100px;
  background: rgb(255, 255, 255);
  list-style-type: none;
  width: 120px;
}
</style>
