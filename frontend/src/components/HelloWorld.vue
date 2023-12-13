<template>
    
    <div class="wrapper">
        <div id="building">
            <div id="project-name">
                <p>
                    Choose what you want!
                </p>
            </div>
            <div id="start">
                <button id="button-start" @click="Start">路况地图</button>
                <button id="button-goto" @click="Goto">生活指南</button>
                <router-view></router-view>
            </div>
        </div>
    </div>

</template>


<script>
export default{
    methods:{
        Start(){
            this.$router.push('/Map')
        },
        Goto(){
            this.$router.push('/Map')
        }
    }
}
</script>

<style>
.wrapper {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url(../assets/a0f30ffe928b426db745beafd9dd6299.jpeg);
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  opacity: 1;
}
#project-name{
    margin:50px auto;
    font-size:100px;
    text-align: center;
    color: darkviolet;
}
#start button{
    width:50%;
    margin:30px auto;
    height:65px;
    background-color: darkviolet;
    color: whitesmoke;
    font-size: 16px;
    font-weight: bold;
    border-radius: 20px;
}
#building{
    margin: 30px auto;
    background-color: rgb(239, 245, 252);
    width: 1000px;
    height: 600px;
    padding: 30px;
    border-radius: 10px;
    opacity: 0.8;
}
</style>