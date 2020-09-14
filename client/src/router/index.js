import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Register from '@/components/Register'
import Profile from '@/components/Profile'
import Empdetail from '@/components/Empdetail'
import Emplist from '@/components/Emplist'
import Tab from '@/components/Tab'
import Visual from '@/components/Visual'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/tab',
      name: 'Tab',
      component: Tab
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/empdetail',
      name: 'Empdetail',
      component: Empdetail
    },
    {
      path: '/emplist',
      name: 'Emplist',
      component: Emplist
    },

    {
      path: '/visual',
      name: 'Visual',
      component: Visual
    }, 

  ]
})
