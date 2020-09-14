<template>
    <div class="container rounded responsive" style=" max-width:700px; ">
        <div class="vue-template">
        <b-jumbotron bg-variant="dark" text-variant="white" border-variant="white" class="mt-3">
        <div class="row">
            <div class="col-md-6 mt-1 mx-auto">
                <form v-on:submit.prevent="register">
                    <strong><h1 class="h3 mb3 font-weight-normal"> <center> Register </center> </h1></strong>
                    <div class="form-group">
                        <label for="emp_name"> <i class="fa fa-user-circle-o" aria-hidden="true">  Employee Full Name</i></label>
                        <input type="text" v-model="emp_name" class="form-control" name="emp_name" placeholder="Enter employee name" required>
                    </div>
                    <div class="form-group">
                        <label for="emp_date"> <i class="fa fa-calendar-check-o" aria-hidden="true">  Joining Date</i> </label>
                        <input type="date" v-model="emp_date" class="form-control" name="emp_date" placeholder="Enter joining date" required>
                    </div>
                    <div class="form-group">
                        <label for="emp_role"> <i class="fa fa-shield" aria-hidden="true">  Employee Role</i> </label>
                        <select name="emp_role" v-model="emp_role">
                            <option disabled value=""><i>  choose role</i></option>
                            <option>HR</option>
                            <option>User</option>
                        </select>
                    </div>
                    
                    <div class="form-group">
                        <label for="emp_email"> <i class="fa fa-envelope-open" aria-hidden="true"></i>  Email address </label>
                        <input type="email" v-model="emp_email" class="form-control" name="emp_email" placeholder="Enter email" autocomplete="" required>
                    </div>
                    <div class="form-group">
                        <label for="emp_password"> <i class="fa fa-lock" aria-hidden="true">  Password</i> </label>
                        <input type="password" v-model="emp_password" class="form-control" name="emp_password" placeholder="Enter password" required>
                    </div>
                    <button class="btn btn-lg btn-primary btn-block"> <i class="fa fa-sign-out" aria-hidden="true">  Register</i> </button>

                </form>
            </div>
        </div>
        </b-jumbotron>
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
                    title: "successfully registered!",
                    icon: "success",
                    button: "ok"
                })
                router.push({name: 'Login'})
            }).catch((err) => {
                alert('fill details?')
                console.log(err)
            })
        }
    }
    
}
</script>

<style scoped>
    .vue-template
    {
        box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.3);
    }
</style>