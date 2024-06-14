import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import loginView from '@/components/login.vue'
import userRegister from '@/components/userRegister.vue'
import dashboard from '@/components/dashboard.vue'
import PersonasView from '@/components/personas.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: loginView
    },
    {
      path: '/register',
      name: 'register',
      component: userRegister
    }
    ,
    {
      path: '/dashboard',
      name: 'dashboard',
      component: dashboard,
      children:[{
        path: '/personas',
        name: 'personas',
        component: PersonasView 
      }]
    }
  
   
    
  ]
})

export default router
