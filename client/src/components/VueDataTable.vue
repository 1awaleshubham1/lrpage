 <template>

    <v-client-table
      :data = "tableData"
      :columns = "columns"
      :options = "options">
    </v-client-table>
  
</template>

<script>

import axios from 'axios'
import router from '../router'
import VueAxios from 'vue-axios'

export default {
  data(){
    return{
      columns: ['empid', 'emp_name', 'emp_role', 'emp_date', 'emp_email', 'emp_password'],

      tableData: [],
      options: {
        headings: {
          empid: 'EMPID',
          emp_name: 'Employee name',
          emp_role: 'Employee role',
          emp_date: 'Employee date',
          emp_email: 'Employee email',
          emp_password: 'Employee password',
        },
        sortIcon:{
          base: 'fa',
          is: 'fas fa-sort',
          up: 'fa-arrow-circle-up',
          down: 'fa-arrow-circle-down'
        },
        sortable: ['empid', 'emp_name', 'emp_role', 'emp_date', 'emp_email', 'emp_password'],
        filtertable: ['empid', 'emp_name', 'emp_role', 'emp_date', 'emp_email']
      }
    }
  },

    mounted()
    {
        axios.get('/users/emplist')
        .then(res=>{
          this.tableData=res.data
          console.log(res.data)
        }) 
        
    }
}
</script>


<style>
#emplist {
  width: 95%;
  margin: 20px; 
}


.VuePagination {
  text-align: center;
}

.vue-title {
  text-align: center;
  margin-bottom: 20px;
  
}

.vue-pagination-ad {
  text-align: center;
}

.glyphicon.glyphicon-eye-open {
  width: 16px;
  display: block;
  margin: 0 auto;
}

th:nth-child(3) {
  text-align: center;
}
th{
    background-color: black;
    color: white;
}

.VueTables__child-row-toggler {
  width: 16px;
  height: 16px;
  line-height: 16px;
  display: block;
  margin: auto;
  text-align: center;
}

.VueTables__child-row-toggler--closed::before {
  content: "+";
}

.VueTables__child-row-toggler--open::before {
  content: "-";
}

</style>