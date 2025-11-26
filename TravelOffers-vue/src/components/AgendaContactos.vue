<template>
  <div class="agenda-contactos">
    <h2>Mi Agenda de Contactos ({{ contactos ? contactos.length : 0 }})</h2>
    
    <div class="form-container">
      <h3>Crear Nuevo Contacto</h3>
      <input type="text" v-model="nuevoContacto.nombre" placeholder="Nombre" required />
      <input type="email" v-model="nuevoContacto.email" placeholder="Email" required />
      <input type="tel" v-model="nuevoContacto.telefono" placeholder="Teléfono" />
      <button @click="crearContacto" :disabled="!isFormValid">Guardar Contacto</button>
      <p v-if="!isFormValid" class="warning">Rellena al menos el Nombre y el Email.</p>
    </div>

    <hr>

    <h3>Listado de Contactos</h3>
    
    <ul v-if="contactos && contactos.length">
      <li v-for="contacto in contactos" :key="contacto.id">
        <div>
            <strong>{{ contacto.nombre }}</strong> 
            <p>Email: {{ contacto.email }} | Teléfono: {{ contacto.telefono || 'N/A' }}</p>
        </div>
        <button @click="borrarContacto(contacto.id)" class="delete-btn">Borrar</button>
      </li>
    </ul>
    <p v-else>No hay contactos en la agenda.</p>
  </div>
</template>

<script setup>
// las importaciones de Firebase para las operaciones crear, borrar, leer
import { collection, addDoc, deleteDoc, doc } from 'firebase/firestore'
// las importaciones de Vuefire para que podamos obtener la bbdd y la colección
import { useFirestore, useCollection } from 'vuefire'
// las importaciones de Vue para la reactividad
import { reactive, computed, ref } from 'vue'

// ================= 1. inicializar y leer =================
const db = useFirestore()
const contactosCollectionRef = collection(db, 'contactos') // Referencia a la colección 'contactos'

// utilizamos useCollection para sincronizar la variable 'contactos' con Firestore
const contactos = useCollection(contactosCollectionRef)


// ================= 2.inicializar nuevo contacto =================
const nuevoContacto = reactive({
  nombre: '',
  email: '',
  telefono: ''
})

// validación del formulario Nombre y Email obligatorios (teléfono opcional)
const isFormValid = computed(() => {
    return nuevoContacto.nombre.trim() !== '' && nuevoContacto.email.trim() !== ''
})

// ================= 3. crear nuevo contacto funcionalidad =================
const crearContacto = async () => {
  if (!isFormValid.value) return

  try {
    // utilizamos addDoc de Firebase para añadir un nuevo documento, en el que vamos a incluir los dayps del nombre, mail y teléfono (en firebase se va a guardar también la fecha en la que añadamos el contacto a nuestra agenda contactos)
    await addDoc(contactosCollectionRef, {
      nombre: nuevoContacto.nombre,
      email: nuevoContacto.email,
      telefono: nuevoContacto.telefono || null,
      fechaCreacion: new Date()
    })
    
    // limpiamos el formulario y notificar al usuario de que se ha creado su contacto con éxito, o de que ha habido un error al crearlo
    nuevoContacto.nombre = ''
    nuevoContacto.email = ''
    nuevoContacto.telefono = ''
    
    alert('Contacto creado con éxito.')
  } catch (e) {
    console.error("Error al añadir contacto: ", e)
    alert('Hubo un error al guardar el contacto.')
  }
}

// ================= 4. borrar contacto ================
const borrarContacto = async (id) => {
    if (confirm('¿Estás seguro de que quieres borrar este contacto?')) {
        try {
            const contactoRef = doc(db, 'contactos', id)
            // deleteDoc la función de Firebase para poder eliminar el documento
            await deleteDoc(contactoRef)
            // así vuefiere puede eliminar automáticamente el contacto (actualizar su lista)
            alert('Contacto eliminado.')
        } catch (e) {
            console.error("Error al eliminar contacto: ", e)
            alert('Hubo un error al eliminar el contacto.')
        }
    }
}
</script>



<style scoped>
.agenda-contactos { 
    background-color: #ffffff; 
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); 
    max-width: 600px; 
    margin: 20px auto; 
    padding: 20px; 
    border: none; 
    border-radius: 8px; 
    font-family: Arial, sans-serif;
    color: #333; 
}
.form-container {
    padding: 15px;
    border: 1px solid #eee;
    margin-bottom: 20px;
    border-radius: 4px;
}
.form-container input { 
    display: block; 
    width: 95%; 
    margin-bottom: 10px; 
    padding: 8px; 
    border: 1px solid #ddd; 
    border-radius: 4px;
    background-color: white; 
    color: #213547; 
}
.form-container button { 
    padding: 10px 15px; 
    background-color: #42b883; 
    color: white; 
    border: none; 
    cursor: pointer; 
    border-radius: 4px;
}
.form-container button:disabled { 
    background-color: #ccc; 
    cursor: not-allowed; 
}
.warning { 
    color: red; 
    font-size: 0.9em; 
    margin-top: 5px;
}
ul { 
    list-style: none; 
    padding: 0; 
}
li { 
    
    background-color: #f9f9f9; 
    border: 1px solid #ddd; 
    padding: 10px; 
    margin-bottom: 10px; 
    display: flex; 
    justify-content: space-between; 
    align-items: center; 
    border-radius: 4px;
}
li p { 
    margin: 0; 
    font-size: 0.9em; 
    color: #555;
}
.delete-btn { 
    background-color: #ff4d4f; 
    color: white; 
    border: none; 
    padding: 8px 12px; 
    cursor: pointer; 
    border-radius: 4px;
    transition: background-color 0.2s;
}
.delete-btn:hover {
    background-color: #e04446;
}
</style>