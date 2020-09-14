<template>
    <div class="container">
        <div class="jumbotron mt-5">
            <div class="col-sm-8 mx-auto">
                <h1></h1>
            </div>
            <table class="table col-md-6 mx-auto">
                <tr>
                    <td>Employee Name</td>
                    <td>{{emp_name}}</td>
                </tr>
                <tr>
                    <td>Employee role</td>
                    <td>{{emp_role}}</td>
                </tr>
                <tr>
                    <td>Employee Email</td>
                    <td>{{emp_email}}</td>
                </tr>
            </table>
        </div>
        
    </div>
</template>

<script>
import jwtDecode from 'jwt-decode'

export default {
    data(){
        const token = localStorage.usertoken
        const decoded = jwtDecode(token)
        return{
            emp_name: decoded.identity.emp_name,
            emp_role: decoded.identity.emp_role,
            emp_email: decoded.identity.emp_email
        }
    }    
}
</script>