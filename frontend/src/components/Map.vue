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



//--------------------------------------------add polylines---------------------------------------------------
      var polyline1 = new AMap.Polyline({
        path: [new AMap.LngLat(116.30722,39.98872),new AMap.LngLat(116.308336,39.988757)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(0,128,0)', // 线条颜色
      });
      polyline1.on('mouseover', () => {
        polyline1.setOptions({
          strokeColor: 'rgb(0,255,0)'
        })
      })
      polyline1.on('mouseout', () => {
        polyline1.setOptions({
          strokeColor: 'rgb(0,128,0)'
        })
      })
      map.add(polyline1);
      AMap.event.addListener(polyline1, 'click', function () {
        infoWindow.open(map, [116.3088865,39.9887435]);
      });


      var polyline2 = new AMap.Polyline({
        path: [new AMap.LngLat(116.312438,39.991958),new AMap.LngLat(116.31261,39.989081)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(148,0,211)', // 线条颜色
      });
      polyline2.on('mouseover', () => {
        polyline2.setOptions({
          strokeColor: 'rgb(255,0,255)'
        })
      })
      polyline2.on('mouseout', () => {
        polyline2.setOptions({
          strokeColor: 'rgb(148,0,211)'
        })
      })
      map.add(polyline2);
      AMap.event.addListener(polyline2, 'click', function () {
        infoWindow.open(map, [116.3125,39.9904]);
      });


      var polyline3 = new AMap.Polyline({
        path: [new AMap.LngLat(116.312615,39.989085),new AMap.LngLat(116.312652,39.988493)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(255,165,0)', // 线条颜色
      });
      polyline3.on('mouseover', () => {
        polyline3.setOptions({
          strokeColor: 'rgb(255,255,0)'
        })
      })
      polyline3.on('mouseout', () => {
        polyline3.setOptions({
          strokeColor: 'rgb(255,165,0)'
        })
      })
      map.add(polyline3);
      AMap.event.addListener(polyline3, 'click', function () {
        infoWindow.open(map, [116.3126,39.9887]);
      });

      var polyline4 = new AMap.Polyline({
        path: [new AMap.LngLat(116.3127,39.988789),new AMap.LngLat(116.31431,39.988867)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(255,0,0)', // 线条颜色
      });
      polyline4.on('mouseover', () => {
        polyline4.setOptions({
          strokeColor: 'rgb(255,192,203)'
        })
      })
      polyline4.on('mouseout', () => {
        polyline4.setOptions({
          strokeColor: 'rgb(255,0,0)'
        })
      })
      map.add(polyline4);
      AMap.event.addListener(polyline4, 'click', function () {
        infoWindow.open(map, [116.313,39.9887]);
      });

      var polyline5 = new AMap.Polyline({
        path: [new AMap.LngLat(116.312552,39.990032),new AMap.LngLat(116.315867,39.990105)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(0,128,0)', // 线条颜色
      });
      polyline5.on('mouseover', () => {
        polyline5.setOptions({
          strokeColor: 'rgb(0,255,0)'
        })
      })
      polyline5.on('mouseout', () => {
        polyline5.setOptions({
          strokeColor: 'rgb(0,128,0)'
        })
      })
      map.add(polyline5);
      AMap.event.addListener(polyline5, 'click', function () {
        infoWindow.open(map, [116.3135,39.990]);
      });

      var polyline6 = new AMap.Polyline({
        path: [new AMap.LngLat(116.314204,39.990105),new AMap.LngLat(116.314306,39.98886)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(255,165,0)', // 线条颜色
      });
      polyline6.on('mouseover', () => {
        polyline6.setOptions({
          strokeColor: 'rgb(255,255,0)'
        })
      })
      polyline6.on('mouseout', () => {
        polyline6.setOptions({
          strokeColor: 'rgb(255,165,0)'
        })
      })
      map.add(polyline6);
      AMap.event.addListener(polyline6, 'click', function () {
        infoWindow.open(map, [116.3143,39.989]);
      });

      var polyline7 = new AMap.Polyline({
        path: [new AMap.LngLat(116.31245,39.991971),new AMap.LngLat(116.315701,39.992111)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(0,128,0)', // 线条颜色
      });
      polyline7.on('mouseover', () => {
        polyline7.setOptions({
          strokeColor: 'rgb(0,255,0)'
        })
      })
      polyline7.on('mouseout', () => {
        polyline7.setOptions({
          strokeColor: 'rgb(0,128,0)'
        })
      })
      map.add(polyline7);
      AMap.event.addListener(polyline7, 'click', function () {
        infoWindow.open(map, [116.3135,39.9915]);
      });

      var polyline8 = new AMap.Polyline({
        path: [new AMap.LngLat(116.312354,39.992892),new AMap.LngLat(116.312456,39.991975)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(255,0,0)', // 线条颜色
      });
      polyline8.on('mouseover', () => {
        polyline8.setOptions({
          strokeColor: 'rgb(255,192,203)'
        })
      })
      polyline8.on('mouseout', () => {
        polyline8.setOptions({
          strokeColor: 'rgb(255,0,0)'
        })
      })
      map.add(polyline8);
      AMap.event.addListener(polyline8, 'click', function () {
        infoWindow.open(map, [116.3124,39.9924]);
      });

      var polyline9 = new AMap.Polyline({
        path: [new AMap.LngLat(116.31112,39.992333),new AMap.LngLat(116.312391,39.992358)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(148,0,211)', // 线条颜色
      });
      polyline9.on('mouseover', () => {
        polyline9.setOptions({
          strokeColor: 'rgb(255,0,255)'
        })
      })
      polyline9.on('mouseout', () => {
        polyline9.setOptions({
          strokeColor: 'rgb(148,0,211)'
        })
      })
      map.add(polyline9);
      AMap.event.addListener(polyline9, 'click', function () {
        infoWindow.open(map, [116.311,39.9923]);
      });

      var polyline10 = new AMap.Polyline({
        path: [new AMap.LngLat(116.311345,39.99193),new AMap.LngLat(116.312456,39.99198)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(255,165,0)', // 线条颜色
      });
      polyline10.on('mouseover', () => {
        polyline10.setOptions({
          strokeColor: 'rgb(255,255,0)'
        })
      })
      polyline10.on('mouseout', () => {
        polyline10.setOptions({
          strokeColor: 'rgb(255,165,0)'
        })
      })
      map.add(polyline10);
      AMap.event.addListener(polyline10, 'click', function () {
        infoWindow.open(map, [116.311,39.9919]);
      });

      var polyline11 = new AMap.Polyline({
        path: [new AMap.LngLat(116.311184,39.991515),new AMap.LngLat(116.31245,39.991556)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(0,128,0)', // 线条颜色
      });
      polyline11.on('mouseover', () => {
        polyline11.setOptions({
          strokeColor: 'rgb(0,255,0)'
        })
      })
      polyline11.on('mouseout', () => {
        polyline11.setOptions({
          strokeColor: 'rgb(0,128,0)'
        })
      })
      map.add(polyline11);
      AMap.event.addListener(polyline11, 'click', function () {
        infoWindow.open(map, [116.311,39.9915]);
      });

      var polyline12 = new AMap.Polyline({
        path: [new AMap.LngLat(116.311206,39.991063),new AMap.LngLat(116.312493,39.991117)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(255,0,0)', // 线条颜色
      });
      polyline12.on('mouseover', () => {
        polyline12.setOptions({
          strokeColor: 'rgb(255,192,203)'
        })
      })
      polyline12.on('mouseout', () => {
        polyline12.setOptions({
          strokeColor: 'rgb(255,0,0)'
        })
      })
      map.add(polyline12);
      AMap.event.addListener(polyline12, 'click', function () {
        infoWindow.open(map, [116.3115,39.9911]);
      });

      var polyline13 = new AMap.Polyline({
        path: [new AMap.LngLat(116.311297,39.990229),new AMap.LngLat(116.312536,39.990274)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(255,165,0)', // 线条颜色
      });
      polyline13.on('mouseover', () => {
        polyline13.setOptions({
          strokeColor: 'rgb(255,255,0)'
        })
      })
      polyline13.on('mouseout', () => {
        polyline13.setOptions({
          strokeColor: 'rgb(255,165,0)'
        })
      })
      map.add(polyline13);
      AMap.event.addListener(polyline13, 'click', function () {
        infoWindow.open(map, [116.312536,39.990274]);
      });

      var polyline14 = new AMap.Polyline({
        path: [new AMap.LngLat(116.311372,39.989436),new AMap.LngLat(116.312574,39.989555)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(0,128,0)', // 线条颜色
      });
      polyline14.on('mouseover', () => {
        polyline14.setOptions({
          strokeColor: 'rgb(0,255,0)'
        })
      })
      polyline14.on('mouseout', () => {
        polyline14.setOptions({
          strokeColor: 'rgb(0,128,0)'
        })
      })
      map.add(polyline14);
      AMap.event.addListener(polyline14, 'click', function () {
        infoWindow.open(map, [116.312574,39.989555]);
      });

      var polyline15 = new AMap.Polyline({
        path: [new AMap.LngLat(116.311324,39.992341),new AMap.LngLat(116.311345,39.991934)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(255,0,0)', // 线条颜色
      });
      polyline15.on('mouseover', () => {
        polyline15.setOptions({
          strokeColor: 'rgb(255,192,203)'
        })
      })
      polyline15.on('mouseout', () => {
        polyline15.setOptions({
          strokeColor: 'rgb(255,0,0)'
        })
      })
      map.add(polyline15);
      AMap.event.addListener(polyline15, 'click', function () {
        infoWindow.open(map, [116.311345,39.991934]);
      });

      var polyline16 = new AMap.Polyline({
        path: [new AMap.LngLat(116.311361,39.991926),new AMap.LngLat(116.311388,39.991528)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(255,165,0)', // 线条颜色
      });
      polyline16.on('mouseover', () => {
        polyline16.setOptions({
          strokeColor: 'rgb(255,255,0)'
        })
      })
      polyline16.on('mouseout', () => {
        polyline16.setOptions({
          strokeColor: 'rgb(255,165,0)'
        })
      })
      map.add(polyline16);
      AMap.event.addListener(polyline16, 'click', function () {
        infoWindow.open(map, [116.311388,39.991528]);
      });

      var polyline17 = new AMap.Polyline({
        path: [new AMap.LngLat(116.311109,39.992345),new AMap.LngLat(116.311163,39.991503)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(0,128,0)', // 线条颜色
      });
      polyline17.on('mouseover', () => {
        polyline17.setOptions({
          strokeColor: 'rgb(0,255,0)'
        })
      })
      polyline17.on('mouseout', () => {
        polyline17.setOptions({
          strokeColor: 'rgb(0,128,0)'
        })
      })
      map.add(polyline17);
      AMap.event.addListener(polyline17, 'click', function () {
        infoWindow.open(map, [116.311163,39.991503]);
      });

      var polyline18 = new AMap.Polyline({
        path: [new AMap.LngLat(116.311157,39.991503),new AMap.LngLat(116.311211,39.991067)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(148,0,211)', // 线条颜色
      });
      polyline18.on('mouseover', () => {
        polyline18.setOptions({
          strokeColor: 'rgb(255,0,255)'
        })
      })
      polyline18.on('mouseout', () => {
        polyline18.setOptions({
          strokeColor: 'rgb(148,0,211)'
        })
      })
      map.add(polyline18);
      AMap.event.addListener(polyline18, 'click', function () {
        infoWindow.open(map, [116.311211,39.991067]);
      });

      var polyline19 = new AMap.Polyline({
        path: [new AMap.LngLat(116.311211,39.991059),new AMap.LngLat(116.311297,39.990233)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(255,165,0)', // 线条颜色
      });
      polyline19.on('mouseover', () => {
        polyline19.setOptions({
          strokeColor: 'rgb(255,255,0)'
        })
      })
      polyline19.on('mouseout', () => {
        polyline19.setOptions({
          strokeColor: 'rgb(255,165,0)'
        })
      })
      map.add(polyline19);
      AMap.event.addListener(polyline19, 'click', function () {
        infoWindow.open(map, [116.311297,39.990233]);
      });

      var polyline20 = new AMap.Polyline({
        path: [new AMap.LngLat(116.311302,39.990225),new AMap.LngLat(116.311372,39.989431)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(0,128,0)', // 线条颜色
      });
      polyline20.on('mouseover', () => {
        polyline20.setOptions({
          strokeColor: 'rgb(0,255,0)'
        })
      })
      polyline20.on('mouseout', () => {
        polyline20.setOptions({
          strokeColor: 'rgb(0,128,0)'
        })
      })
      map.add(polyline20);
      AMap.event.addListener(polyline20, 'click', function () {
        infoWindow.open(map, [116.311372,39.989431]);
      });

      var polyline21 = new AMap.Polyline({
        path: [new AMap.LngLat(116.308497,39.992493),new AMap.LngLat(116.310728,39.992629),new AMap.LngLat(116.311115,39.992337)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(148,0,211)', // 线条颜色
      });
      polyline21.on('mouseover', () => {
        polyline21.setOptions({
          strokeColor: 'rgb(255,0,255)'
        })
      })
      polyline21.on('mouseout', () => {
        polyline21.setOptions({
          strokeColor: 'rgb(148,0,211)'
        })
      })
      map.add(polyline21);
      AMap.event.addListener(polyline21, 'click', function () {
        infoWindow.open(map, [116.310728,39.992629]);
      });

      var polyline22 = new AMap.Polyline({
        path: [new AMap.LngLat(116.312359,39.992892),new AMap.LngLat(116.313255,39.992941)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(255,165,0)', // 线条颜色
      });
      polyline22.on('mouseover', () => {
        polyline22.setOptions({
          strokeColor: 'rgb(255,255,0)'
        })
      })
      polyline22.on('mouseout', () => {
        polyline22.setOptions({
          strokeColor: 'rgb(255,165,0)'
        })
      })
      map.add(polyline22);
      AMap.event.addListener(polyline22, 'click', function () {
        infoWindow.open(map, [116.312359,39.992892]);
      });

      var polyline23 = new AMap.Polyline({
        path: [new AMap.LngLat(116.313244,39.992941),new AMap.LngLat(116.315626,39.99304)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(0,128,0)', // 线条颜色
      });
      polyline23.on('mouseover', () => {
        polyline23.setOptions({
          strokeColor: 'rgb(0,255,0)'
        })
      })
      polyline23.on('mouseout', () => {
        polyline23.setOptions({
          strokeColor: 'rgb(0,128,0)'
        })
      })
      map.add(polyline23);
      AMap.event.addListener(polyline23, 'click', function () {
        infoWindow.open(map, [116.315626,39.99304]);
      });

      var polyline24 = new AMap.Polyline({
        path: [new AMap.LngLat(116.310374,39.988811),new AMap.LngLat(116.310363,39.989086),
               new AMap.LngLat(116.310653,39.989394),new AMap.LngLat(116.311361,39.989423)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(148,0,211)', // 线条颜色
      });
      polyline24.on('mouseover', () => {
        polyline24.setOptions({
          strokeColor: 'rgb(255,0,255)'
        })
      })
      polyline24.on('mouseout', () => {
        polyline24.setOptions({
          strokeColor: 'rgb(148,0,211)'
        })
      })
      map.add(polyline24);
      AMap.event.addListener(polyline24, 'click', function () {
        infoWindow.open(map, [116.310653,39.989394]);
      });

      var polyline25 = new AMap.Polyline({
        path: [new AMap.LngLat(116.30833,39.988762),new AMap.LngLat(116.309806,39.988803)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(255,165,0)', // 线条颜色
      });
      polyline25.on('mouseover', () => {
        polyline25.setOptions({
          strokeColor: 'rgb(255,255,0)'
        })
      })
      polyline25.on('mouseout', () => {
        polyline25.setOptions({
          strokeColor: 'rgb(255,165,0)'
        })
      })
      map.add(polyline25);
      AMap.event.addListener(polyline25, 'click', function () {
        infoWindow.open(map, [116.309806,39.988803]);
      });

      var polyline26 = new AMap.Polyline({
        path: [new AMap.LngLat(116.3098,39.988799),new AMap.LngLat(116.310363,39.988803)],  
        strokeWeight: 6, // 线条宽度，默认为 1
        strokeColor: 'rgb(0,128,0)', // 线条颜色
      });
      polyline26.on('mouseover', () => {
        polyline26.setOptions({
          strokeColor: 'rgb(0,255,0)'
        })
      })
      polyline26.on('mouseout', () => {
        polyline26.setOptions({
          strokeColor: 'rgb(0,128,0)'
        })
      })
      map.add(polyline26);
      AMap.event.addListener(polyline26, 'click', function () {
        infoWindow.open(map, [116.310363,39.988803]);
      });
//--------------------------------------------add polylines---------------------------------------------------








      //实例化信息窗体
      var title = '',
      content = [];
      content.push('<span style="font-size:20px;color:rgb(0,0,139);">当前路况是</span>');
      content.push('<a style="color:rgb(0,128,0);">畅通</a>');
      content.push('<a style="color:rgb(255,165,0);">适中</a>');
      content.push('<a style="color:rgb(255,0,0);">拥堵</a>');
      content.push('<a style="color:rgb(148,0,211);">极其拥堵</a>');

      var infoWindow = new AMap.InfoWindow({
      isCustom: true,  //使用自定义窗体
      content: createInfoWindow(title, content.join("<br/>")),
      //offset: new AMap.Pixel(16, -45)
      });


      //构建自定义信息窗体
      function createInfoWindow(title, content) {
        var info = document.createElement("div");
        info.className = "custom-info input-card content-window-card";

        //可以通过下面的方式修改自定义窗体的宽高
        //info.style.width = "400px";
        // 定义顶部标题
        var top = document.createElement("div");
        var titleD = document.createElement("div");
        var closeX = document.createElement("img");
        top.className = "info-top";
        titleD.innerHTML = title;
        closeX.src = "https://webapi.amap.com/images/close2.gif";
        closeX.onclick = closeInfoWindow;

        top.appendChild(titleD);
        top.appendChild(closeX);
        info.appendChild(top);
        // 定义中部内容
        var middle = document.createElement("div");
        middle.className = "info-middle";
        middle.style.backgroundColor = 'rgb(240,248,255)';
        middle.innerHTML = content;
        info.appendChild(middle);

        /*// 定义底部内容
        var bottom = document.createElement("div");
        bottom.className = "info-bottom";
        bottom.style.position = 'relative';
        bottom.style.top = '0px';
        bottom.style.margin = '0 auto';
        var sharp = document.createElement("img");
        sharp.src = "https://webapi.amap.com/images/sharp.png";
        bottom.appendChild(sharp);
        info.appendChild(bottom);*/
        return info;
      }

      //关闭信息窗体
      function closeInfoWindow() {
        map.clearInfoWindow();
      }


/*
//add polygons
      var path2 = [
        new AMap.LngLat(116.311263,39.990851),
        new AMap.LngLat(116.313377,39.991114),
        new AMap.LngLat(116.313688,39.989339),
        new AMap.LngLat(116.311392,39.989207)
      ];
      var polygon = new AMap.Polygon({
        path: path2,  
        fillColor: '#fff', // 多边形填充颜色
        borderWeight: 2, // 线条宽度，默认为 1
        strokeColor: 'red', // 线条颜色
        fillOpacity: 0.4
      });
      polygon.on('mouseover', () => {
        polygon.setOptions({
          fillOpacity: 0.7,
          fillColor: '#7bccc4'
        })
      })
      polygon.on('mouseout', () => {
        polygon.setOptions({
          fillOpacity: 0.5,
          fillColor: '#ccebc5'
        })
      })
      map.add(polygon);
*/


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
  