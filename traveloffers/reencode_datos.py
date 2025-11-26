from pathlib import Path

# Archivo original (el que ya tienes)
origen = Path("datos.json")

# Leemos el archivo asumiendo que está en Windows-1252 / Latin-1
texto = origen.read_text(encoding="latin-1")

# Escribimos un nuevo archivo, ahora SÍ en UTF-8
destino = Path("datos_utf8.json")
destino.write_text(texto, encoding="utf-8")

print("Convertido a UTF-8 como datos_utf8.json")
