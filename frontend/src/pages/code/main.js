import {
    createApp
} from 'vue'
import App from './CodeApp'
import router from '../../router/code'
import store from '../../store/code'
import vuetify from '../../plugins/vuetify'
import {
    loadFonts
} from '../../plugins/webfontloader'

loadFonts()

const app = createApp(App)

app.use(router)
app.use(store)
app.use(vuetify)
app.mount('#app')
