import random
import json


def encriptar(codigo, mensaje):
    """Encripta un mensaje reemplazando caracteres según el diccionario código."""
    mensaje_encriptado = ""  # .join(codigo.get(char, char) for char in mensaje)
    for palabra in mensaje:
        if palabra in codigo.keys():
            mensaje_encriptado += codigo[palabra]
        else:
            mensaje_encriptado += palabra
    return mensaje_encriptado


def descifrar(codigo, mensaje):
    """Descifra un mensaje invirtiendo el código de sustitución."""
    codigo_inverso = {v: k for k, v in codigo.items()}  # Invertimos clave-valor
    mensaje_descifrado = ""  # .join(codigo_inverso.get(char, char) for char in mensaje)
    for palabra in mensaje:
        if palabra in codigo_inverso.keys():
            mensaje_descifrado += codigo_inverso[palabra]
        else:
            mensaje_descifrado += palabra
    return mensaje_descifrado


def crear_codigo_aleatorio(guardar=True, ruta="codigo.json"):
    """Genera un diccionario de sustitución aleatorio para encriptación."""
    caracteres = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    caracteres_cifrados = caracteres.copy()
    random.shuffle(caracteres_cifrados)  # Mezclamos los caracteres

    codigo = {}  # Diccionario de sustitución
    for caracter, caracter_cifrado in zip(caracteres, caracteres_cifrados):
        codigo[caracter] = caracter_cifrado

    if guardar:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(codigo, archivo)  # Guardamos el diccionario en JSON

    return codigo


def leer_mensaje(ruta="mensaje.txt"):
    """Lee un mensaje desde un archivo."""
    with open(ruta, encoding="utf-8") as archivo:
        mensaje = archivo.read()
    return mensaje


def leer_codigo(ruta="codigo.json"):
    """Lee el código desde un archivo y lo carga como un diccionario."""
    with open(ruta, encoding="utf-8") as archivo:
        codigo = json.load(archivo)  # Cargamos el diccionario desde JSON
    return codigo


if __name__ == "__main__":

    # Ejemplo de uso
    codigo = crear_codigo_aleatorio()
    mensaje_original = "Hola, Python!"
    mensaje_encriptado = encriptar(codigo, mensaje_original)
    mensaje_descifrado = descifrar(codigo, mensaje_encriptado)

    print(f"Mensaje original: {mensaje_original}")
    print(f"Mensaje encriptado: {mensaje_encriptado}")
    print(f"Mensaje descifrado: {mensaje_descifrado}")
