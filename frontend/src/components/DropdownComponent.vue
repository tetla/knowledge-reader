<template>
  <v-select
    :items="items"
    v-model="select"
    :item-text="item_text"
    :item-value="item_value"
    :label="label"
    v-on:change="updateValue"
  ></v-select>
</template>

<script>
export default {
  name: "DropdownComponent",
  data() {
    return {
      select: "",
    };
  },
  props: {
    items: {
      type: Array,
      require: false,
      default: () => [], // Objectを生成する関数を指定する
    },
    item_text: {
      type: String,
      require: true,
      default: "",
    },
    item_value: {
      type: String,
      require: true,
      default: "",
    },
    label: {
      type: String,
      require: true,
      default: "",
    },
  },
  methods: {
    updateValue() {
      this.$emit("parentMethod", this.select);
    },
  },
};
</script>
