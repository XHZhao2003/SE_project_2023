import { MapKey } from "../config/mapConfig";
import AMapLoader from '@amap/amap-jsapi-loader';
import { map, toolbar, scale, marker } from "./Lifestyle.vue";

// 初始化地图函数
export const initMap = new Promise((resolve, reject) => {
AMapLoader.load({
"key": `${MapKey}`,

//!!! 2.0 许多插件名与老版本不同
"version": "1.4.15",
"plugins": [
'AMap.ToolBar',
'AMap.Scale',
'AMap.Marker',
'AMap.AdvancedInfoWindow',
],
}).then((AMap) => {
map = new AMap.Map('container', {
viewMode: "3D",
pitch: 70,
zoom: 16,
center: [116.31088, 39.99281],
});

//同步加载的插件直接添加
// 在图面添加工具条控件，工具条控件集成了缩放、平移、定位等功能按钮在内的组合控件
toolbar = new AMap.ToolBar({
position: 'LT'
});
map.addControl(toolbar);
// 在图面添加比例尺控件，展示地图在当前层级和纬度下的比例尺
scale = new AMap.Scale();
map.addControl(scale);
// 在图面添加鹰眼控件，在地图右下角显示地图的缩略图
//添加一个点标记
marker = new AMap.Marker({
position: [116.308148, 39.988473],
});
map.add(marker);

var lnglat = [116.312931, 39.990494];
var marker2 = new AMap.Marker({
position: lnglat
});
marker2.setMap(map);

var content = '<div class="info-title">E路相伴</div><div class="info-content">' +
'<img src="https://cyzx.pku.edu.cn/images/2020-12/378534fd-a512-486e-905c-5c2669125808.jpeg">' +
'理科一号楼<br/>' + '营业时间：7:00 - 22:00<br/>';
'<a target="_blank" href = "https://mobile.amap.com/">点击下载高德地图</a></div>';

var InfoWindow = new AMap.AdvancedInfoWindow({
isCustom: true,
closeWhenClickMap: true,
content: content,
asOrigin: false,
asDestination: false,
offset: new AMap.Pixel(0, -30)
});
marker2.on("click", (e) => {
InfoWindow.open(
map
);
});


var options = {
areas: [{
// visible: false, // 是否可见
rejectTexture: true,
path: [[
[116.303959, 39.997705],
[116.309087, 40.000302],
[116.315761, 40.000319],
[116.317306, 39.985852],
[116.304946, 39.985524]
]]
}]
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
fillColor: 'rgba(256,256,256)',
fillOpacity: 1,
strokeColor: 'rgba(38,127,204)',
strokeWeight: 5,
strokeOpacity: 1,
strokeStyle: 'solid',






/*勾勒形状轮廓的虚线和间隙的样式，此属性在strokeStyle 为dashed 时有效， 此属性在
ie9+浏览器有效 取值：
实线：[0,0,0]
虚线：[10,10] ，[10,10] 表示10个像素的实线和10个像素的空白（如此反复）组成的虚线
点画线：[10,2,10]， [10,2,10] 表示10个像素的实线和2个像素的空白 + 10个像素的实
线和10个像素的空白 （如此反复）组成的虚线*/
strokeDasharray: [10, 2, 10]
});

resolve();
}).catch(e => {
//操作失败
reject(e);
});


});
