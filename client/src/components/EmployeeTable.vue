<template>
  <div id="employee-table">
    <p
      v-if="employees.length < 1"
      class="empty-table"
    >
      No employees
    </p>
    <table class="table table-dark table-striped table-hover table-responsive" v-else>
      <thead>
        <tr>
          <th>Empid</th>
          <th>Name</th>
          <th>Role</th>
          <th>Joining Date</th>
          <th>email</th>
          <th>password</th>
          <th>Actions</th>
          <th>View details</th>
        </tr>
      </thead>
      <tbody>
        <tr
          :key="employee.empid"
          v-for="employee in employees"
        >
          <td v-if="editing === employee.empid">
            <input
              type="text"
              v-model="employee.empid"
            readonly>
          </td>
          <td v-else>{{employee.empid}}</td>

          <td v-if="editing === employee.empid">
            <input
              type="text"
              v-model="employee.emp_name"
            >
          </td>
          <td v-else>{{employee.emp_name}}</td>

          <td v-if="editing === employee.empid">
            <select v-model="employee.emp_role"> 
               <option disabled value="">Please select one</option>
               <option>HR</option>
               <option>User</option>
            </select></td>
          <td v-else>{{employee.emp_role}}</td>

          <td v-if="editing === employee.empid">
            <input
              type="date"
              v-model="employee.emp_date"
            >
          </td>
          <td v-else>{{employee.emp_date}}</td>

          <td v-if="editing === employee.empid">
            <input
              type="email"
              v-model="employee.emp_email"
            >
          </td>
          <td v-else>{{employee.emp_email}}</td>

          <td v-if="editing === employee.empid">
            <input
              type="password"
              v-model="employee.emp_password"
            readonly>
          </td>
          <td v-else>{{employee.emp_password}}</td>

          <td v-if="editing === employee.empid">
            <button @click="editEmployee(employee)" class="btn btn-primary btn-sm">Save</button>
            <button
              class="muted-button btn btn-warning btn-sm"
              @click="cancelEdit(employee)" 
            >Cancel</button>
          </td>
          <td v-else>
            <button @click="editMode(employee, employee.empid)" class="btn btn-primary btn-sm"><i class="fa fa-edit" aria-hidden="true"></i></button> 
            <button @click="$emit('delete:employee', employee.empid)" class="btn btn-warning btn-sm"><i class="fa fa-remove" aria-hidden="true"></i></button>
          </td>
          <td>
            <form action="Empdetail.vue" v-on:submit.prevent="see"> 
              <input type="hidden" name="empid" v-model="employee.empid" value="employee.empid">
              <button class="btn btn-warning btn-sm" name="see" 
              value="see"><i class="fa fa-eye" aria-hidden="true"></i></button>
            </form>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'
import router from '../router'

export default {
  name: 'employee-table',
  props: {
    employees: Array,
  },
  data() {
    return {
      editing: null,
    }
  },
  methods: {
    editMode(employee) {
      this.cachedEmployee = Object.assign({}, employee)
      this.editing = employee.empid
    },

    cancelEdit(employee) {
      Object.assign(employee, this.cachedEmployee)
      this.editing = null;
    },

    editEmployee(employee) {
      if (employee.emp_name === '' || employee.emp_email === '' || employee.emp_role === '' || employee.emp_date === '') return
      this.$emit('edit:employee', employee.empid, employee)
      this.editing = null
    },
    deleteMode(employee) {
      return this.$emit('edit:employee', employee.empid, employee)
      this.editing = null
    },
    see() {
      axios.post('/users/empdetail',{
      empid: this.empid,
      }).then((res)=>{
      localStorage.setItem('usertoken', res.data)
      console.log(res.data)
      this.empid = ''
      router.push({name: 'Empdetail'})
      }).catch((err) => {
      alert("data canot accessible!")
      console.log(err)
      })
    },

  }
}
</script>

<style scoped>

.empty-table {
  text-align: center;
}
</style>
