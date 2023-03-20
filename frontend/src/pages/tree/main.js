import {
    createApp
} from 'vue'
import App from './TreeApp.vue'
import router from '../../router/tree'
import vuetify from '../../plugins/vuetify'
import {
    loadFonts
} from '../../plugins/webfontloader'

loadFonts()

const app = createApp(App)

app.use(router)
app.use(vuetify)
app.mount('#app')
