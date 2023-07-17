# Evaluador de Propiedades

Este script de Python se utiliza para evaluar y clasificar propiedades en función de varios criterios. Carga un archivo Excel que contiene información detallada sobre diferentes propiedades, incluyendo características tales como "Parrilla", "Hogar a Leña", "Agua Potable", "Dormitorios separados", "Sauna", "Jacuzzi", "Pool", "Costo por persona" y "Distancia a BCN". Cada una de estas características contribuye a una puntuación final que se utiliza para clasificar las propiedades.

## Criterios y su Importancia

Los criterios son ponderados según su importancia para la evaluación de la propiedad. Aquí está el detalle de los criterios y su peso en la puntuación final:

- "Dormitorios separados": 4
    - Esta característica tiene la mayor ponderación. Se da preferencia a las propiedades que tienen dormitorios separados.
- "Costo por persona": -1
    - Este criterio tiene una ponderación negativa porque un costo menor es preferible. Por lo tanto, las propiedades con un costo por persona más bajo recibirán una puntuación más alta.
- "Distancia a BCN": -1
    - Similar al "Costo por persona", un valor más bajo es mejor para este criterio. Las propiedades más cercanas a BCN tendrán una puntuación más alta.
- "Parrilla", "Hogar a Leña", "Agua Potable", "Pool": 3
    - Estas características son bastante deseables y reciben una ponderación alta.
- "Sauna": 2
    - La disponibilidad de una sauna es deseable, pero tiene una ponderación ligeramente menor en comparación con las características anteriores.
- "Jacuzzi": 1
    - Esta característica tiene la ponderación más baja, indicando que es la menos importante de las características enumeradas.

## Cómo Ejecutar el Script en PyCharm

1. Abra PyCharm.
2. Navegue a `File > Open` y seleccione el directorio que contiene el script de Python.
3. Asegúrese de que tiene instalada la biblioteca `pandas` en su entorno de Python. Si no es así, puede instalarla a través de la terminal de PyCharm utilizando el comando `pip install pandas`.
4. Si el archivo de datos Excel no se encuentra en la ruta especificada en el script (`~/Downloads/casas/2024_here_we_come.xlsx`), actualice la ruta a la ubicación correcta del archivo.
5. Ejecute el script presionando `Shift + F10` o haciendo clic derecho en el archivo del script y seleccionando `Run`.

El script calculará las puntuaciones para cada propiedad basándose en los criterios y sus pesos, ordenará las propiedades en orden ascendente de puntuación, e imprimirá los nombres y las puntuaciones de las 10 propiedades principales.
