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
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import('../views/AboutView.vue')
  },
  */
  {
    path: '/',
    name: 'top',
    component: () => import('../views/TopMenus.vue')
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
    path: '/tori_toroku',
    name: 'tori_toroku',
    component: () => import('../views/ToriRegist.vue')
  },
  {
    path: '/e_bom',
    name: 'e_bom',
    component: () => import('../views/E_Bom.vue')
  },
  {
    path: '/code_regist',
    name: 'code_regist',
    component: () => import('../views/CodeRegist.vue')
  },
  {
    path: '/code_list',
    name: 'code_list',
    component: () => import('../views/CodeList.vue')
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
