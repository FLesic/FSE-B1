import { createRouter, createWebHistory} from 'vue-router'
//import 自定义组件名 from 路径
import AccountManage from "@/cashier/components/AccountStatus.vue";
import AccountOpen from "@/cashier/components/AccountOpen.vue";
const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            redirect: '/cashier'
        },
        {
            path: '/accountManage',
            component: AccountManage,
        },
        {
            path: '/accountOpen',
            component: AccountOpen,
        }
    ]
})

export default router