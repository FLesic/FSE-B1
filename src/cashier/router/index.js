import { createRouter, createWebHistory} from 'vue-router'
//import 自定义组件名 from 路径
import Cashier from '@/cashier/components/cashier.vue'
import Deposit from '@/cashier/components/deposit.vue'
import Withdrawl from '@/cashier/components/withdrawl.vue'
import Transfer from '@/cashier/components/transfer.vue'
import Query from '@/cashier/components/query.vue'
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
        },
        {
            path: '/deposit',
            component: Deposit
        },
        {
            path: '/withdrawl',
            component: Withdrawl
        },
        {
            path: '/transfer',
            component: Transfer
        },
        {
            path: '/query',
            component: Query
        }
    ]
})

export default router