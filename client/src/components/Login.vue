<template>
    <div class="container rounded responsive" style=" max-width:700px; ">
        <div class="vue-template">
        <b-jumbotron bg-variant="dark" text-variant="white" border-variant="white" class="mt-3"> 
            <div class="row">
                <div class="col-md-6 mt-5 mx-auto">
                    <form v-on:submit.prevent="login">
                        <h3 class="text-center"> <i class="fa fa-lock fa-3x" aria-hidden="true"></i> </h3>
                        <div class="form-group">
                            <label for="emp_email"><i class="fa fa-envelope" aria-hidden="true"> Email Address</i></label>
                            <input type="email" v-model="emp_email" class="form-control" name="emp_email" placeholder="Enter mail" required>
                        </div>
                        <div class="form-group">
                            <label for="emp_password"> <i class="fa fa-lock" aria-hidden="true"> Password </i></label>
                            <input type="password" v-model="emp_password" class="form-control" name="emp_password" placeholder="Enter password" id="myInput" required>
                            
                        </div>
                        <button class="btn btn-lg btn-primary btn-block"> <i class="fa fa-sign-in" aria-hidden="true">  Login</i></button>
                    </form>
            </div>

        </div>
        <hr/>
        <div class="social-icons">
            <ul>
                <li><a href="#"><i class="fa fa-google"></i></a></li>
                <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                <li><a href="#"><i class="fa fa-twitter"></i></a></li>
            </ul>
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
            emp_email: '',
            emp_password: ''
        }
    },

    methods: {
        login() {
            axios.post('/users/login',{
                emp_email: this.emp_email,
                emp_password: this.emp_password
            }).then((res)=>{
                if (res.status === 200) {
                this.$session.start()
                this.$session.set('jwt', res.data)
                localStorage.setItem('usertoken', res.data)
                this.emp_email = ''
                this.emp_password = ''
                swal({
                    title: "successfully login!",
                    icon: "success",
                    button: "ok"
                }),
                
                router.push({name: 'Emplist'})
                EventBus.$emit('logged-in', 'loggedin')
                }
            }).catch((err) => {
                alert("login failed")
                EventBus.$emit('', '')
                console.log(err)
            })
            this.emitMethod()
        },
    }
    
}
</script>

<style scoped>
    .vue-template
    {
        box-shadow: 7px 7px 7px rgba(0, 0, 0, 0.3);
    }    
    .social-icons {
    text-align: center;
    font-family: "Open Sans";
    font-weight: 300;
    font-size: 1.5em;
    color: #222222;
    }
    ul {
       list-style: none; 
    }

    .social-icons ul {
    list-style: none;
    margin: 0;
    padding: 0;
    }
    .social-icons ul li {
    display: inline-block;
    zoom: 1;
    width: 65px;
    vertical-align: middle;
    border: 1px solid #e3e8f9;
    font-size: 15px;
    height: 40px;
    line-height: 40px;
    margin-right: 5px;
    background: #f4f6ff;
    }

    .social-icons ul li a {
    display: block;
    font-size: 1.4em;
    margin: 0 5px;
    text-decoration: none;
    }
    .social-icons ul li a i {
    -webkit-transition: all 0.2s ease-in;
    -moz-transition: all 0.2s ease-in;
    -o-transition: all 0.2s ease-in;
    -ms-transition: all 0.2s ease-in;
    transition: all 0.2s ease-in;
    }

    .social-icons ul li a:focus i,
    .social-icons ul li a:active i {
    transition: none;
    color: #222222;
    }

    h3{
        color: blue;
    }

</style>
