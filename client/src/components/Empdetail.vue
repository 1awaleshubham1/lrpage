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
        <b-button variant="primary" v-on:click="close">close</b-button>
    </div>
    
        
</template> 

<script>
import jwtDecode from 'jwt-decode'

export default {
  name: "empdetail",
    data(){
        const token = localStorage.usertoken
        const decoded = jwtDecode(token)
        return{
            emp_name: decoded.identity.emp_name,
            emp_role: decoded.identity.emp_role,
            emp_email: decoded.identity.emp_email
        }
    },    
  

  methods:
  {
    close: function()
    {
        this.$router.push({path: '/emplist'}); 
    }
  }
  
}
</script>

<style scoped>
    .empd{
        margin: 100px;
        box-shadow: 7px 7px 7px rgba(0, 0, 0, 0.3);
    }
    td{
        color:whitesmoke;
    }
    b-button{
        position: right;
    }
</style>