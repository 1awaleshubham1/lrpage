<template>
<div>

<!-- add Modal -->
<div class="modal fade" id="employeeModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Add Employee Data</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
                <form v-on:submit.prevent="register">
                    <h1 class="h3 mb3 font-weight-normal"></h1>
                    <div class="form-group">
                        <label for="emp_name"><i class="fa fa-user-circle-o" aria-hidden="true"> </i> Employee Full Name</label>
                        <input type="text" v-model="emp_name" class="form-control" name="emp_name" placeholder="Enter employee name" required>
                    </div>
                    <div class="form-group">
                        <label for="emp_date"><i class="fa fa-calendar-check-o" aria-hidden="true"> </i> Joining Date</label>
                        <input type="date" v-model="emp_date" class="form-control" name="emp_date" placeholder="Enter joining date" required>
                    </div>
                    <div class="form-group">
                        <label for="emp_role"><i class="fa fa-shield" aria-hidden="true">  Employee Role</i></label>
                        <select name="emp_role" v-model="emp_role" required>
                            <option disabled value="">Please select one</option>
                            <option>HR</option>
                            <option>User</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="emp_email"><i class="fa fa-envelope-open" aria-hidden="true"></i>  Email address</label>
                        <input type="email" v-model="emp_email" class="form-control" name="emp_email" placeholder="Enter email" required>
                    </div>
                    <div class="form-group">
                        <label for="emp_password"> <i class="fa fa-lock" aria-hidden="true"></i> Password</label>
                        <input type="password" v-model="emp_password" class="form-control" name="emp_password" placeholder="Enter password" required>
                    </div>
                    <div class="modal-footer">
                    <button type="button" class="btn btn-danger" data-dismiss="modal"> <i class="fa fa-dropbox" aria-hidden="true"></i> Close</button>
                    <button class="btn btn-primary"> <i class="fa fa-download" aria-hidden="true"></i> save data</button>
                    </div>
                </form>
        </div>
    </div>
  </div>
</div>

<div class="container">
        <div class="jumbotron">
            
               <!-- Button trigger modal -->
                <h3>Add Employee data               
                <button type="button" class="btn btn-primary btn-sm" data-toggle="modal" data-target="#employeeModal">
                  <i class="fa fa-plus-square-o" aria-hidden="true"></i> Add Data
                </button></h3>
            
        </div>
        </div>
</div>
</template>


<script>
import axios from 'axios'
import router from '../router'
import EventBus from './EventBus'

export default {
    data (){
        return{
        dataArray: Array,
            emp_name: '',
            emp_date: '',
            emp_role: '',
            emp_email: '',
            emp_password: ''
        }
    },

    methods: {
        register() {
            axios.post('/users/register', {
                emp_name: this.emp_name,
                emp_date: this.emp_date,
                emp_role: this.emp_role,
                emp_email: this.emp_email,
                emp_password: this.emp_password
            }).then((res)=>{
                console.log(res)                
                swal({
                    title: " added successfully!",
                    icon: "success",
                    buttons: "ok",
                    dangerMode: "True"
                })
                location.reload(true)
            }).catch((err) => {
                alert('fill details?')
                console.log(err)
            })
        },

    },
    mounted()
    {
        axios.get('/users/table')
        .then(res=>{
          this.dataArray=res.data
          console.log(res.data)
        }) 
        
    }
    
}
</script>