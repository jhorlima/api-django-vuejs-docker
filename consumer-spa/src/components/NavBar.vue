<template>
  <div class="layout-row layout-align-center-center toolbar md-whiteframe-z1">
      <h3>Consumers</h3>
  </div>
</template>
<script>
export default {
    name: 'NavBar',
        props: {
            msg: String
        }
}
</script>

<style scoped lang="scss">
h3 {
  margin: 0;
}
.toolbar {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    position: relative;
    z-index: 2;
    font-size: 20px;
    min-height: 64px;
    width: 100%;
}
    
</style>