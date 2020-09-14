import '@babel/polyfill'
import 'mutationobserver-shim'
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App'
import router from './router'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import swal from 'sweetalert'
require('../node_modules/bootstrap/dist/css/bootstrap.css')
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
import "font-awesome/css/font-awesome.min.css";
import { VuejsDatatableFactory } from 'vuejs-datatable'
import { ClientTable } from 'vue-tables-2'
import VueCharts from 'vue-chartjs'
import { VueCsvImport } from 'vue-csv-import';
import VueSession from 'vue-session'


Vue.use(VueSession)
Vue.use( VuejsDatatableFactory );
Vue.use( ClientTable );

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
