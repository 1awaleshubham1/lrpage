<template>
<div>
    <div id="tab" class="container">
        <employee-form />
      
    </div>
    <div class="jumbotron">
        <div class="card-body table-responsive">
            <employee-table
                :employees="employees"
                @delete:employee="deleteEmployee"
                @edit:employee="editEmployee" 
                />
        </div>
    </div>
</div>
</template>

<script>

import axios from 'axios'
import router from '../router'
import EmployeeTable from '@/components/EmployeeTable.vue'
import EmployeeForm from '@/components/EmployeeForm.vue'


export default {
  name: "tab",
  components: {
    EmployeeTable,
    EmployeeForm,
   
  },
  data() {
    return {
      employees: []
    }
  },

  mounted() {
    this.getEmployees()
  },

  methods: {
    async getEmployees() {
      try {
        const response = await fetch('/users/emplist')
        const data = await response.json()
        
        this.employees = data
      } catch (error) {
        console.error(error)
      }
    },

    async editEmployee(empid, updatedEmployee) {
      try {
        const response = await fetch(`/users/update/${empid}`, {
          method: 'PUT',
          body: JSON.stringify(updatedEmployee),
          headers: { "Content-type": "application/json; charset=UTF-8" }
        })
        const data = await response.json()
        swal({
          title: "Data Updated succesfully!",
          icon: "success",
          button: "Ok",
        })    
        location.reload(True)
        this.employees = this.employees.map(employee => employee.empid === empid ? data : employee)

      } catch (error) {
        console.error(error)
      }
    },

    async deleteEmployee(empid) {
      try {
        await fetch(`/users/delete/${empid}`, {
          method: 'DELETE'
        })
        this.employees = this.employees.filter(employee => employee.empid !== empid)
        swal({
          icon: "warning",
          text: "data deleted succesfully",
          button: "Ok",
        })
      } catch (error) {
        console.error(error)
      }
    },
  }
}
</script>

<style scoped>
button {
  background: #009435;
  border: 1px solid #009435;
}

button:hover,
button:active,
button:focus {
  background: #32a95d;
  border: 1px solid #32a95d;
}

</style>
