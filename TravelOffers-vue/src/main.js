import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router' 

// ========= importaciones FIREBASE / VUEFIRE  =========
// Asegúrate de que solo se importen una vez en todo el archivo
import { initializeApp } from 'firebase/app' 
import { getFirestore } from 'firebase/firestore' 
import { VueFire } from 'vuefire' 

// los credenciales de configuración de firebase
const firebaseConfig = {
    apiKey: "AIzaSyAp9je3GEYv0CTpf9CKrAXrRWKXME4IpGw",
    authDomain: "traveloffers-d2c1a.firebaseapp.com",
    projectId: "traveloffers-d2c1a",
    storageBucket: "traveloffers-d2c1a.firebasestorage.app",
    messagingSenderId: "444478743158",
    appId: "1:444478743158:web:e8f8e2526dc8346ab5b557",
};

// icialización de firebase 
const firebaseApp = initializeApp(firebaseConfig)
const db = getFirestore(firebaseApp) 

const app = createApp(App)

// para conectar vuefire a la app de firebsae
app.use(VueFire, {
    firebaseApp,
    modules: [],
    firestore: db, 
})

// lineas para usar el router que hemos creado
app.use(router)

app.mount('#app')