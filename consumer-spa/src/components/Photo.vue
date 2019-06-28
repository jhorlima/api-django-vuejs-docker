<template>
  <img ref="picture" :src="loading">
</template>

<script>

  export default {
    name: 'Picture',
    props: {
      image: {
        type: String,
        default: ''
      },
      fallback: {
        type: String,
        default: require('@/assets/icons/fallback-image.svg')
      }
    },
    data: () => ({
      loading: require('@/assets/icons/circular-loading.svg')
    }),
    created() {
      this.loadImage();
    },
    methods: {
      loadImage() {
        let image = new Image();
        image.onload = () => this.$refs.picture.src = image.src;
        image.onerror = () => this.$refs.picture.src = this.fallback;
        image.src = this.image;
      }
    }
  };
</script>
