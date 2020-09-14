<template>
<!--  <div class="container">
    <div class="jumbotron mt-5 mr-30 ml-50">
      <form v-on:submit.prevent="getreport">
        <h1 class="h3 mb3 font-weight-normal"></h1>
          <div class="form-group">
            <label for="end_date"><i class="fa fa-calendar-check-o" aria-hidden="true"> </i> Start Date</label>
              <input type="date" v-model="start_date" class="form-control" name="start_date" placeholder="Enter Start date" required>
          </div>
          <div class="form-group">
            <label for="end_date"><i class="fa fa-calendar-check-o" aria-hidden="true"> </i> End Date</label>
               <input type="date" v-model="end_date" class="form-control" name="end_date" placeholder="Enter End date" required>
          </div>
          <div>
            <button class="btn btn-primary"> <i class="fa fa-download" aria-hidden="true"></i> Get Report</button>
          </div>
      </form>

    </div>

-->
  <div class="container">
    <div class="jumbotron">
      <LineChart v-if="loaded" :data="pageViews" :styles="styles"/>
      <h3><center>EMS LineChart report</center></h3>
    </div>  
    <div class="jumbotron">
      <PieChart v-if="loaded" :data="pageCategory" :styles="styles"/>
      <h3><center>EMS PieChart report</center></h3>
    </div>    
  </div>
  
</template>

<script>
import LineChart from "@/components/LineChart";
import PieChart from "@/components/PieChart"

export default {

  components: {
    LineChart,
    PieChart
  },
  data() {
    return {
      loaded: false,
      pageViews: null,
      pageCategory: null,
      styles: {
        position: "relative"
      }
    };
  },
  async created() {
    let resp = await fetch(
      "/users/barchart"
    );

    let data = await resp.json();
    console.log("DATA", data);
    this.pageViews = data.pageViews;
    this.pageCategory = data.pageCategory;

    this.loaded = true;
  }
};
</script>


