<template>
    <div id="amapcontainer" style="position:fixed;top:0;left:0;background-size:cover;background-repeat:no-repeat;background-position: center center;width: 100%; height: 100%;"></div>
</template>

<script>
import AMapLoader from '@amap/amap-jsapi-loader';
window._AMapSecurityConfig={
    securityJsCode: '6eb2566e8d90747b180cbb7c43e24641'
}
export default{
    data (){
        return{
            map: null
        }
    },
    methods:{
        initAMap(){
            AMapLoader.load({
                key:"6eefde9e350c9392e70bdf14f66fcfaa",
                plugins: ["AMap.Scale", "AMap.ToolBar", "AMap.ControlBar", 'AMap.Geocoder', 'AMap.Marker',
          'AMap.CitySearch', 'AMap.Geolocation', 'AMap.AutoComplete', 'AMap.InfoWindow']
            }).then((AMap)=>{
                this.map=new AMap.Map("amapcontainer",{
                    resizeEnable:true,
                    zoom: this.zroom,
                    zoomEnable:true,
                    dragEnable:true,
                    zoom:16,
                    center:[116.31088,39.99281]
                })
            }).catch(e=>{
                console.log(e)
            })
        }
    },
    mounted(){
        this.initAMap()
    }
}
</script>

<style lang="less">
</style>