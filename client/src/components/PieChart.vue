
<script>
import { Pie } from "vue-chartjs";

export default {
  extends: Pie,
  name: "PieChart",
  props: ["data"],
  mounted() {
    // color list below came from https://stackoverflow.com/a/45489530/52160
    // reformat in the way the lib wants
    let chartData = {
      labels: [],

      datasets: [
        {
          label: "Views by EMS",
          backgroundColor: ["blue", "green"],
          data: [], 
        }
      ]
    };

    for (let category in this.data) {
      chartData.labels.push(category);
      chartData.datasets[0].data.push(this.data[category]);
    }

    this.renderChart(chartData, {
      responsive: true,
      maintainAspectRatio: false
    });
  }
};
</script>
