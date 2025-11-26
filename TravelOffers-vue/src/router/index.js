import { createRouter, createWebHistory } from 'vue-router'
import AgendaContactos from '../components/AgendaContactos.vue' 

// ========= 1. definir las rutas =========//
const routes = [
  {
    path: '/',
    name: 'AgendaPrincipal',
    component: AgendaContactos
  }
]

// ========= 2. creación de la instancia del router =========
const router = createRouter({
  // utilizamos el historial basado en el navegador
  history: createWebHistory(),
  routes
})

// ========= 3. exportación del router =========
export default router