import {
    createRouter,
    createWebHashHistory
} from 'vue-router'

const routes = [{
        path: '/',
        name: 'tree',
        component: () => import('@/pages/tree/TableTreeList.vue')
    }, {
        path: '/root_select',
        name: 'treecreate',
        component: () => import('@/pages/tree/TreeRootSelect.vue')
    }, {
        path: '/tree_create',
        name: 'tree_create',
        component: () => import('@/pages/tree/TreeCreate.vue')
    }, {
        path: '/table_tree',
        name: 'table_tree',
        component: () => import('@/pages/tree/TreeCreate.vue')
    },

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
