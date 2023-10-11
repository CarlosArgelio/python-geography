import geopandas as gpd
import matplotlib.pyplot as plt

# Cargar la capa temática
natalidad = "data/spain/natalidad.geojson"
map_data = gpd.read_file(natalidad)
map_data.head()

# Control del tamaño de la figura del mapa
fig, ax = plt.subplots(figsize=(10, 10))
 
# Control del título y los ejes
ax.set_title('Natalidad por Provincias en España, 2018', 
             pad = 20, 
             fontdict={'fontsize':20, 'color': '#4873ab'})
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
 
# Mostrar el mapa finalizado
map_data.plot(column='NAT2018', cmap='plasma', ax=ax, zorder=5)
