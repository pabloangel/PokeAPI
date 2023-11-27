import requests
from PIL import Image
from io import BytesIO  # Agregamos la importación de BytesIO
import matplotlib.pyplot as plt

pokemon = input("Introduce el nombre de un Pokemon: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}/"
res = requests.get(url)

# Manejo de errores HTTP
if res.status_code != 200:
    print(f"No se ha encontrado el Pokémon. Código de estado: {res.status_code}")
    exit()

# Manejo de excepciones
try:
    res.raise_for_status()
    data = res.json()
except requests.exceptions.HTTPError as errh:
    print ("Error HTTP:", errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error de conexión:", errc)
except requests.exceptions.Timeout as errt:
    print ("Tiempo de espera agotado:", errt)
except requests.exceptions.RequestException as err:
    print ("Error durante la solicitud:", err)
    exit()

# Verificación de la existencia de la URL de la imagen
if 'sprites' not in data or 'front_default' not in data['sprites']:
    print("No se encontró la URL de la imagen del Pokémon.")
    exit()

# Obtener la imagen desde la URL usando Pillow y BytesIO
imagen_url = data['sprites']['front_default']
response = requests.get(imagen_url)
img = Image.open(BytesIO(response.content))

# Visualización de la imagen
plt.title(data['name'])
plt.imshow(img)
plt.show()