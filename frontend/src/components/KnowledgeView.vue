<template>
  <v-container>
    <v-row>
      <v-col>
        <DropdownComponent
          v-bind:items="pagelist"
          item_text="title"
          item_value="page_id"
          label="Course"
          @parentMethod="updatePageSelect"
        />
      </v-col>
      <v-col>
        <DropdownComponent
          v-bind:items="contentlist"
          item_text="title"
          item_value="content_id"
          label="Chapter"
          @parentMethod="updateContentSelect"
        />
      </v-col>
    </v-row>
    <v-row>
      <ContentView
        v-bind:description="contentDescription"
        v-bind:title="contentTitle"
      />
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";
import marked from "marked";

import ContentView from "./ContentView";
import DropdownComponent from "./DropdownComponent";

export default {
  name: "KnowledgeView",
  components: {
    ContentView,
    DropdownComponent,
  },
  data: () => ({
    pagelist: [],
    contentlist: [],
    contentOnject: null,
    selectedPageId: "",
    selectedContentId: "",
    contentDescription: "",
    contentTitle: "",
  }),
  created: function() {
    axios
      .get(process.env.VUE_APP_BACKEND_ENDPOINT + "/pagelist")
      .then((response) => {
        this.pagelist = response.data.pagelist;
      });
  },
  methods: {
    updatePageSelect(selectedPageId) {
      axios
        .get(
          process.env.VUE_APP_BACKEND_ENDPOINT + "/contents/" + selectedPageId
        )
        .then((response) => {
          this.selectedPageId = selectedPageId;
          this.contentlist = response.data.contents;
        });
    },
    updateContentSelect(selectedContentId) {
      axios
        .get(
          process.env.VUE_APP_BACKEND_ENDPOINT +
            "/contents/" +
            this.selectedPageId +
            "/" +
            selectedContentId
        )
        .then((response) => {
          this.selectedContentId = selectedContentId;
          this.contentDescription = marked(response.data.description);
          this.contentTitle = response.data.title;
        });
    },
  },
};
</script>
