<template>
    <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
        <a class="navbar-brand" href="#"><h3 style="color:blue">EMS</h3></a>
        <button class="navbar-toggler d-lg-none" type="button" data-toggle="collapse" data-target="#collapsibleNavId" aria-controls="collapsibleNavId"
            aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="collapsibleNavId">
            
            <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                <li class="nav-item active">
                    <router-link class="nav-link" to="/">Home</router-link>
                </li>
                <li v-if="auth==''" class="nav-item">
                    <router-link class="nav-link" to="/login">Login</router-link>
                </li>
                <li v-if="auth==''" class="nav-item">
                    <router-link class="nav-link" to="/register">Register</router-link>
                </li>
                <li v-if="auth=='loggedin'" class="nav-item">
                    <router-link class="nav-link" to="/profile">Profile</router-link>
                </li>
                <li v-if="auth=='loggedin'" class="nav-item">
                    <router-link class="nav-link" to="/emplist">Employee list</router-link>
                </li>
                <li v-if="auth=='loggedin'" class="nav-item">
                    <router-link class="nav-link" to="/tab">change data</router-link>
                </li>
                <li v-if="emp_ro==emp_role" class="nav-item">
                    <router-link class="nav-link" to="/tab">ch</router-link>
                </li>
                <li v-if="auth=='loggedin'" class="nav-item">
                    <router-link class="nav-link" to="/visual">view Report</router-link>
                </li>
                <li v-if="auth=='loggedin'" class="nav-item" >
                    <a class="nav-link" href="" v-on:click="logout">Logout</a>
                </li>
            </ul>
        </div>
    </nav>
</template>

<script>
import EventBus from './EventBus'
import jwtDecode from 'jwt-decode'


EventBus.$on('logged-in', test => {
    console.log(test)
})
export default {
   
    data()
    {
        const token = localStorage.usertoken
        const decoded = jwtDecode(token)
        
        return{
            emp_name: decoded.identity.emp_name,
            emp_role: decoded.identity.emp_role,
            emp_email: decoded.identity.emp_email,
        
            auth: '',
            user: '',
            emp_ro: ''

        }
    },
    methods: {
        logout() {
            this.$session.destroy()
            swal({
                    title: "Logout successfully",
                    icon: "success",
                    button: "ok"
                }),
            localStorage.removeItemk('usertoken')
        }
    },
    mounted()
    {
        EventBus.$on('logged-in', status => {
            this.auth = status
        })
    }
}
</script>
