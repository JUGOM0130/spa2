import {
  createRouter,
  createWebHashHistory
} from 'vue-router'
/*import HomeView from '../views/HomeView.vue'*/

const routes = [
  /*
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  */
  {
    path: '/',
    name: 'top',
    component: () => import('@/TopMenus.vue')
  },
  {
    path: '/junbi',
    name: 'junbi',
    component: () => import('../views/PleaseWaite.vue')
  },
  {
    path: '/shain_toroku',
    name: 'shain_toroku',
    component: () => import('../views/ShainRegist.vue')
  },
  {
    path: '/torihiki',
    name: 'torihiki',
    component: () => import('@/pages/torihiki/ToriList.vue')
  }, {
    path: '/torihiki_regist',
    name: 'torihiki_regist',
    component: () => import('@/pages/torihiki/ToriRegist.vue')
  },
  {
    path: '/saiban',
    name: 'saiban',
    component: () => import('../views/AutoNumbering.vue')
  },
  {
    path: '/saibanshow',
    name: 'saibanshow',
    component: () => import('../views/AutoNumberingView.vue')
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
