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
      path: '/interstrate',
      name: 'interestrate',
      component: () => import('../views/InterestRatesView.vue')
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
      path: '/test',
      name: 'test',
      component: TestView
    },

  ]
})

export default router
