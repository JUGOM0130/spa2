import {
    createRouter,
    createWebHashHistory
} from 'vue-router'

const routes = [{
        path: '/',
        name: 'tree',
        component: () => import('@/pages/tree/TreeRoot.vue')
    }, {
        path: '/root_select',
        name: 'treecreate',
        component: () => import('@/pages/tree/TreeRootSelect.vue')
    }, {
        path: '/tree_create',
        name: 'tree_create',
        component: () => import('@/pages/tree/TreeCreate.vue')
    },

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
