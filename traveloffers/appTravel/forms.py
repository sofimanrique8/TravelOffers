from django import forms
from .models import ReservaInquiry

class ReservaInquiryForm(forms.ModelForm):
    # Personalizar el widget para el campo de fecha usando el tipo 'date' de HTML5
    fecha_viaje_preferida = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Fecha de viaje preferida'
    )

    class Meta:
        model = ReservaInquiry
        fields = [
            'nombre_completo',
            'email',
            'telefono',
            'fecha_viaje_preferida',
            'numero_personas',
            'comentarios'
        ]
        labels = {
            'nombre_completo': 'Nombre Completo',
            'email': 'Correo Electrónico',
            'telefono': 'Teléfono (opcional)',
            'numero_personas': 'Número de Personas',
            'comentarios': 'Comentarios/Solicitudes Especiales (opcional)'
        }
        # Agregar clases CSS de Bootstrap a los campos para un mejor estilo
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: +34 600 000 000'}),
            'numero_personas': forms.NumberInput(attrs={'class': 'form-control', 'min': '1'}),
            'comentarios': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Cualquier detalle extra que debamos saber'}),
        }