import { createRouter, createWebHistory} from 'vue-router'
//import 自定义组件名 from 路径
import Cashier from '@/cashier/components/cashier.vue'
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            redirect: '/manager'
        },
        {
            path: '/cashier',
            component: Cashier
        }
    ]
})

export default router