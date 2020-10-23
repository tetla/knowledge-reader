<template>
  <div>
    <h2>{{ title }}</h2>
    <p v-html="$sanitize(description)"></p>
  </div>
</template>

<script>
export default {
  name: "ContentView",
  props: {
    description: {
      type: String,
      require: false,
      default: "",
    },
    title: {
      type: String,
      require: false,
      default: "",
    },
  },
  data: () => ({}),
};
</script>
