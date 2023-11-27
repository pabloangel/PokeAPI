import requests
from PIL import Image
from io import BytesIO  # Agregamos la importación de BytesIO
import matplotlib.pyplot as plt

pokemon_name = input("Introduce el nombre de un Pokémon: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
response = requests.get(url)

if response.status_code == 200:
    pokemon_data = response.json()

    print(f"Nombre: {pokemon_data['name']}")
    print(f"Altura: {pokemon_data['height']}")
    print(f"Peso: {pokemon_data['weight']}")
    print("Habilidades:")
    for ability in pokemon_data['abilities']:
        print(f" - {ability['ability']['name']}")

else:
    print(f"No se encontró el Pokémon. Código de estado: {response.status_code}")

print("Movimientos:")
for move in pokemon_data['moves']:
    print(f" - {move['move']['name']}")

# Manejo de excepciones
try:
    response.raise_for_status()
    data = response.json()
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
