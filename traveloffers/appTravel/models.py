from django.db import models 

class Pais(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    icono = models.ImageField(upload_to='iconos_paises/', blank=True, null=True)
    class Meta:
        verbose_name_plural = "Países"
    def __str__(self): return self.nombre  

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    icono = models.ImageField(upload_to='iconos_categorias/', blank=True, null=True)
    def __str__(self): return self.nombre

class Oferta(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    fecha_publicacion = models.DateField(auto_now_add=True)
    imagen = models.URLField(blank=True, null=True)

    def __str__(self): return self.titulo

class Imagen(models.Model):
    titulo = models.CharField(max_length=100, blank=True)
    imagen = models.ImageField(upload_to='imagenes/')
    oferta = models.ForeignKey(
        Oferta,
        on_delete=models.CASCADE,
        related_name='galeria',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Imagenes"
    def __str__(self): return self.titulo or f"Imagen {self.pk}"

class ReservaInquiry(models.Model): 
    
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE, related_name='inquiries', verbose_name="Oferta") 
    nombre_completo = models.CharField(max_length=150)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_viaje_preferida = models.DateField()
    numero_personas = models.PositiveIntegerField(default=1)
    comentarios = models.TextField(blank=True, null=True)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = "Solicitud de Reserva"
        verbose_name_plural = "Solicitudes de Reserva"

    def __str__(self): 
        return f"Solicitud de {self.nombre_completo} para {self.oferta.titulo}"
