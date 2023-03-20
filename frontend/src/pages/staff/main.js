import {
    createApp,
} from 'vue'
import App from './StaffApp.vue'
import router from '@/router/staff'
import vuetify from '@/plugins/vuetify'

let app = createApp(App)
app.use(router)
app.use(vuetify)
app.mount('#app')
