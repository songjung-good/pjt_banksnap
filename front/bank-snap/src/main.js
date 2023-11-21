import { createApp } from 'vue'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import App from './App.vue'
import router from './router'
// import bootstrap5 from 'Bootstrap5'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

const app = createApp(App)
const pinia = createPinia()

pinia.use(piniaPluginPersistedstate)

// app.use(createPinia())
app.use(pinia)
app.use(router)
// app.use(bootstrap5)

app.mount('#app')
