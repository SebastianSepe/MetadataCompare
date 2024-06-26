import json
import os
import re

def compare_jsons(old_json, new_json, path="", differences=None, ignored_keys=None):
    if differences is None:
        differences = []
    if ignored_keys is None:
        ignored_keys = set()  # Claves que deseas ignorar

    if isinstance(old_json, dict) and isinstance(new_json, dict):
        for key in old_json:
            if key in ignored_keys:
                continue  # Ignora esta clave completamente
            if key not in new_json:
                differences.append(f"Clave '{key}' encontrada en el JSON antiguo pero no en el nuevo JSON. Ruta: {path}")
            else:
                compare_jsons(old_json[key], new_json[key], path=f"{path}.{key}" if path else key,
                              differences=differences, ignored_keys=ignored_keys)
        for key in new_json:
            if key in ignored_keys:
                continue  # Ignora esta clave completamente
            if key not in old_json:
                differences.append(f"Clave '{key}' encontrada en el nuevo JSON pero no en el antiguo. Ruta: {path}")
    elif isinstance(old_json, list) and isinstance(new_json, list):
        if len(old_json) != len(new_json):
            differences.append(f"Las listas en '{path}' tienen diferentes longitudes.")
        else:
            for index, (o, n) in enumerate(zip(old_json, new_json)):
                compare_jsons(o, n, path=f"{path}[{index}]", differences=differences, ignored_keys=ignored_keys)
    else:
        if old_json != new_json:
            if type(old_json) != type(new_json):
                differences.append(
                    f"Tipos diferentes en '{path}'. Esperado {type(old_json).__name__}, encontrado {type(new_json).__name__}")
            else:
                differences.append(f"Valor diferente en '{path}'. Esperado '{old_json}', encontrado '{new_json}'")

    return differences

def load_json_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error al decodificar JSON en el archivo {filename}: {e}")
        return None
    except Exception as e:
        print(f"Error al cargar el archivo {filename}: {e}")
        return None

def get_file_size(filename):
    if os.path.exists(filename):
        return os.path.getsize(filename)

def main(source_dir, target_dir, output_file, platform, ignored_keys=None):
    with open(output_file, 'w', encoding='utf-8') as file:
        # pattern = re.compile(f".+\\.{re.escape(platform)}\\.json$")
        pattern = re.compile(f".+.json$")
        for filename in os.listdir(source_dir):
            if pattern.match(filename) and get_file_size(os.path.join(source_dir, filename)) > 0:
                file.write(f"\nArchivo: {filename}, Tamaño: {get_file_size(os.path.join(source_dir, filename))} bytes\n")
                source_file = os.path.join(source_dir, filename)
                target_file = os.path.join(target_dir, filename)
                if os.path.exists(target_file):
                    old_json = load_json_file(source_file)
                    new_json = load_json_file(target_file)
                    if old_json is None or new_json is None:
                        file.write(f"No se pudo comparar {filename} debido a un error al cargar los archivos.\n")
                    else:
                        differences = compare_jsons(old_json, new_json, ignored_keys=ignored_keys)
                        if differences:
                            file.write(f"Resultado para {filename}:\n")
                            for diff in differences:
                                file.write(f" - {diff}\n")
                        else:
                            file.write(f"{filename}: Los JSON son compatibles.\n")
                else:
                    file.write(f"No se encontró el archivo correspondiente para {filename} en la carpeta destino.\n")
        if ignored_keys:
            file.write(f"\n\nClaves ignoradas pero con diferencias: {ignored_keys}\n")

# Configura tus directorios y el archivo de salida aquí
expected = '../gxMetadata/gxmetadataPlantCareBuild182098v18u9'
obtained = '../gxMetadata/gxmetadataPlantCareBuild182150Trunk'
platform = 'TODO'
outputFile = f'Diferencias_en_Metadata_{platform}.txt'
ignored_keys = {"@accessibleVisible"}
ignored_keys1 = set()

main(expected, obtained, outputFile, platform, ignored_keys)
