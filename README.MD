Comparador de JSONs para Metadatos
Este script está diseñado para comparar dos directorios que contienen archivos JSON, identificando diferencias entre las versiones de archivos que corresponden entre sí. Es útil para validar cambios en los metadatos entre diferentes versiones de software o durante el desarrollo.

Características
Detección de Diferencias: Identifica y reporta diferencias clave por clave entre dos archivos JSON.
Compatibilidad con Listas y Tipos: Gestiona listas y valida que los tipos de datos sean consistentes entre los archivos comparados.
Informes Detallados: Genera un archivo de texto que resume las diferencias encontradas, indicando las rutas específicas de las discrepancias en la estructura JSON.
Filtrado por Plataforma: Permite especificar una plataforma (por ejemplo, iOS o Android) para filtrar los archivos que serán comparados, basándose en la extensión del archivo.
Estructura del Código
El código está dividido en varias funciones principales:

load_json_file(filename): Carga un archivo JSON y retorna su contenido.
write_differences(file, filename, differences): Escribe las diferencias encontradas en un archivo de salida.
compare_jsons(old_json, new_json, path="", differences=None): Compara recursivamente dos estructuras JSON y acumula las diferencias.
main(source_dir, target_dir, output_file, platform): Función principal que organiza el flujo del programa, desde la lectura de los directorios hasta la escritura del archivo de resultados.
Uso
Para usar este script, necesitas configurar los siguientes parámetros al final del archivo:

expected_dir: Directorio que contiene los archivos JSON de la versión anterior.
obtained_dir: Directorio que contiene los archivos JSON de la nueva versión.
platform: Plataforma específica para la que se compararán los archivos (e.g., 'ios').
output_file: Nombre del archivo donde se escribirán los resultados.

