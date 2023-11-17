import { createRouter, createWebHistory } from 'vue-router'
import MapView from '@/views/MapView.vue'
import TestView from '@/views/TestView.vue'
import MainView from '@/views/MainView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/deposit',
      name: 'DepositView',
      component: () => import('../views/DepositView.vue')
    },
    {
      path: '/saving',
      name: 'SavingView',
      component: () => import('../views/SavingView.vue')
    },
    {
      path: '/calculator',
      name: 'exchangecalculator',
      component: () => import('../views/ExchangeCalculatorView.vue')
    },
    {
      path: '/community',
      name: 'community',
      component: () => import('../views/CommunityView.vue')
    },
    {
      path: '/map',
      name: 'map',
      component: () => import('../views/MapView.vue')
    },
    {
      path: '/create/article',
      name: 'CreateArticleView',
      component: () => import('../views/CreateArticleView.vue')
    },
    {
      path: '/test',
      name: 'test',
      component: TestView
    },
    {
      path: '/article/:id',
      name: 'DetailView',
      component: () => import('@/views/ArticleDetailView.vue')
    },
    {
      path: '/login',
      name: 'LoginView',
      component: () => import('@/views/LoginView.vue')
    },
    {
      path: '/signUp',
      name: 'SignUpView',
      component: () => import('@/views/SignUpView.vue')
    },
    {
      path: '/profile/:id',
      name: 'ProfileView',
      component: () => import('@/views/ProfileView.vue')
    },
  ]
})

export default router
