<template>
<div class="home-component">
  <div>{{ msg }}</div>
</div>
</template>

<script>
import axios from "axios"
export default {
  data() {
    return {
      msg: ''
    }
  },
  methods: {
    init() {
      const URL = "http://localhost:4000"
      axios.get(URL).then((res) => this.msg = res.data.msg)
    }
  },
  mounted() {
    this.init()
  }
}
</script>