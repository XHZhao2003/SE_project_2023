<template>
    
    <div class="wrapper">
        <div id="building">
            <project-name>
                <p>
                    e-road
                </p>
            </project-name>
            <start>
                <button @click="Start">start now</button>
                <router-view></router-view>
            </start>
        </div>
    </div>

</template>


<script>
export default{
    methods:{
        Start(){
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
  opacity: 0.75;
}
div project-name{
    margin:50px auto;
    font-size:100px;
    text-align: center;
    color: ivory;
}
div start button{
    width:99%;
    margin:50px auto;
    height:45px;
    background-color: darkviolet;
    color: whitesmoke;
    font-size: 16px;
    font-weight: bold;
    border-radius: 20px;
}
#building{
    margin: 200px auto;
    background-color: null;
    width: 400px;
    height: 200px;
    padding: 20px;
    border-radius: 10px;
}
</style>