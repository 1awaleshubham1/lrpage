
<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  name: "LineChart",
  props: ["data"],
  mounted() {
    // reformat in the way the lib wants
    let chartData = {
      labels: ['No. of Employee', 'Active Employee', 'Leave Employee'],
      datasets: [
        {
          label: "Employee management system",
          backgroundColor: "blue",
          data: [],

        }
      ]

    };

    for (let i = 0; i < this.data.length; i++) {
      //chartData.labels.push(this.data[i].active);
      chartData.datasets[0].data.push(this.data[i].value);
    }

    this.renderChart(chartData, {
      responsive: true,
      maintainAspectRatio: false
    });
  }
};
</script>
