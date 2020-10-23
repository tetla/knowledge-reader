<template>
  <v-app>
    <AppBarComponent />
    <v-main>
      <KnowledgeView />
    </v-main>
  </v-app>
</template>

<script>
import AppBarComponent from "./components/AppBarComponent";
import KnowledgeView from "./components/KnowledgeView";

export default {
  name: "App",

  components: {
    AppBarComponent,
    KnowledgeView,
  },

  data: () => ({}),
};
</script>
