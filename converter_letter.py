text = input('Escribe algo con tilde para formatear:\n')

text = text.strip().lower()

text = text.replace('á', 'a')
text = text.replace('é', 'e')
text = text.replace('í', 'i')
text = text.replace('ó', 'o')
text = text.replace('ú', 'u')

print(f'Texto formateado: {text}')