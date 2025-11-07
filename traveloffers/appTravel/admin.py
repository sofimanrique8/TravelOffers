# appTravel/admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Pais, Categoria, Oferta, Imagen


# ----- Inlines -----
class ImagenInline(admin.TabularInline):
    model = Imagen
    extra = 1
    fields = ("imagen", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if getattr(obj, "imagen", None):
            try:
                return format_html(
                    '<img src="{}" width="100" height="70" style="object-fit:cover;border-radius:6px;" />',
                    obj.imagen.url,
                )
            except Exception:
                return "—"
        return "—"
    preview.short_description = "Vista previa"


# ----- Admins -----
@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "preview_icono")
    search_fields = ("nombre", "descripcion")
    fields = ("nombre", "descripcion", "icono", "icono_preview")
    readonly_fields = ("icono_preview",)

    def preview_icono(self, obj):
        """Miniatura en la lista de categorías."""
        icono = getattr(obj, "icono", None)
        if icono:
            try:
                return format_html(
                    '<img src="{}" width="32" height="32" style="object-fit:contain;" />',
                    icono.url,
                )
            except Exception:
                return "—"
        return "—"
    preview_icono.short_description = "Icono"

    def icono_preview(self, obj):
        """Vista previa grande en el panel de edición."""
        icono = getattr(obj, "icono", None)
        if icono:
            try:
                return format_html(
                    '<img src="{}" width="80" height="80" style="object-fit:contain;border:1px solid #eee;border-radius:8px;padding:4px;" />',
                    icono.url,
                )
            except Exception:
                return "—"
        return "—"
    icono_preview.short_description = "Vista previa"


@admin.register(Oferta)
class OfertaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "pais", "precio")
    list_filter = ("pais",)
    search_fields = ("titulo", "descripcion")
    inlines = [ImagenInline]
    # Si queréis ordenar por precio por defecto:
    ordering = ("precio",)

    # Opcional: vista previa rápida de la primera imagen de galería
    def portada(self, obj):
        first = obj.galeria.first() if hasattr(obj, "galeria") else None
        if first and getattr(first, "imagen", None):
            try:
                return format_html(
                    '<img src="{}" width="60" height="45" style="object-fit:cover;border-radius:4px;" />',
                    first.imagen.url,
                )
            except Exception:
                return "—"
        return "—"
    portada.short_description = "Portada"


# ----- Registro simple de Imagen (si queréis verla fuera del inline) -----
@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ("oferta", "thumb")
    search_fields = ("oferta__titulo",)

    def thumb(self, obj):
        if getattr(obj, "imagen", None):
            try:
                return format_html(
                    '<img src="{}" width="80" height="60" style="object-fit:cover;border-radius:6px;" />',
                    obj.imagen.url,
                )
            except Exception:
                return "—"
        return "—"
    thumb.short_description = "Vista previa"