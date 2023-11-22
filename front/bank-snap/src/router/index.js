import { createRouter, createWebHistory } from 'vue-router'
import MapView from '@/views/MapView.vue'
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
      path: '/product/:id',
      name: 'ProductDetailView',
      component: () => import('../views/ProductDetailView.vue')
    },
    {
      path: '/economynews',
      name: 'EconomyNews',
      component: () => import('../views/EconomyNewsView.vue')
    },
    {
      path: '/calculator',
      name: 'ExchangeCalculator',
      component: () => import('../views/ExchangeCalculatorView.vue')
    },
    {
      path: '/community',
      name: 'community',
      component: () => import('../views/CommunityView.vue')
    },
    {
      path: '/map/:bank',
      name: 'map',
      component: () => import('../views/MapView.vue')
    },
    {
      path: '/create/article',
      name: 'CreateArticleView',
      component: () => import('../views/CreateArticleView.vue')
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
    {
      path: '/propensity',
      name: 'PropensityView',
      component: () => import('@/views/PropensityView.vue')
    },
    {
      path: '/propensity/update',
      name: 'PropensityUpdateView',
      component: () => import('@/views/PropensityUpdateView.vue')
    },
    {
      path: '/price',
      name: 'PriceView',
      component: () => import('@/views/PriceView.vue')
    },
    
  ]
})

export default router
