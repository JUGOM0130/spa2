import {
  createRouter,
  createWebHashHistory
} from 'vue-router'

const routes = [{
    path: '/',
    name: 'staff',
    component: () => import('@/pages/staff/StaffList')
  },

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
