import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import loginView from '@/components/login.vue'
import userRegister from '@/components/userRegister.vue'
import dashboard from '@/components/dashboard.vue'
import PersonasView from '@/components/personas.vue'
import piePaginaView from '@/components/piePagina.vue'

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
    },
    {
      path: '/piePagina',
      name: 'piePagina',
      component: piePaginaView
    }
    
  ]
})

export default router
