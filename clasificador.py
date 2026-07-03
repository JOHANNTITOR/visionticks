import json
import unicodedata

def clasificar_documento(texto):

    # normaliza texto a minúsculas y elimina acentos
    texto = texto.lower()
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

    # abre archivo JSON con palabras clave, transforma a diccionario
    with open("formatos.json", "r", encoding="utf-8") as f:
        config = json.load(f)

    # carga palabras clave desde archivo JSON
    peaje = config["peaje"]
    boleta = config["boleta"]
    factura = config["factura"]
    estacionamiento = config["estacionamiento"]
    tarjeta_credito = config["tarjeta de credito"]
    tarjeta_debito = config["tarjeta de debito"]
    mall_chino = config["mall chino"]
    disco_duro = config["disco duro"]
    comprobante_giro = config["comprobante de giro"]
    comprobante_deposito = config["comprobante de deposito"]
    cupon = config["cupon"]
    revision_tecnica = config["revision tecnica"]
    seguro_automotriz = config["seguro automotriz"]
    permiso_circulacion = config["permiso de circulacion"]
    registro_vehiculo = config["padron del vehiculo"]
    registro_propiedad = config["registro de propiedad"]
    pago_servicios = config["internet"]
    multa = config["multa"]
    

    # indica puntajes si son boletas o tickets de peaje 

    puntaje_peaje = sum(peso for palabra, peso in peaje.items() if palabra in texto)
    puntaje_boleta = sum(peso for palabra, peso in boleta.items() if palabra in texto)
    puntaje_factura = sum(peso for palabra, peso in factura.items() if palabra in texto)
    puntaje_estacionamiento = sum(peso for palabra, peso in estacionamiento.items() if palabra in texto)
    puntaje_tarjeta_credito = sum(peso for palabra, peso in tarjeta_credito.items() if palabra in texto)
    puntaje_tarjeta_debito = sum(peso for palabra, peso in tarjeta_debito.items() if palabra in texto)
    puntaje_mall_chino = sum(peso for palabra, peso in mall_chino.items() if palabra in texto)
    puntaje_disco_duro = sum(peso for palabra, peso in disco_duro.items() if palabra in texto)
    puntaje_comprobante_giro = sum(peso for palabra, peso in comprobante_giro.items() if palabra in texto)
    puntaje_comprobante_deposito = sum(peso for palabra, peso in comprobante_deposito.items() if palabra in texto)
    puntaje_cupon = sum(peso for palabra, peso in cupon.items() if palabra in texto)
    puntaje_revision_tecnica = sum(peso for palabra, peso in revision_tecnica.items() if palabra in texto)
    puntaje_seguro_automotriz = sum(peso for palabra, peso in seguro_automotriz.items() if palabra in texto)
    puntaje_permiso_circulacion = sum(peso for palabra, peso in permiso_circulacion.items() if palabra in texto)
    puntaje_registro_vehiculo = sum(peso for palabra, peso in registro_vehiculo.items() if palabra in texto)
    puntaje_registro_propiedad = sum(peso for palabra, peso in registro_propiedad.items() if palabra in texto)
    puntaje_pago_servicios = sum(peso for palabra, peso in pago_servicios.items() if palabra in texto)
    puntaje_multa = sum(peso for palabra, peso in multa.items() if palabra in texto)


    # crea diccionario con puntajes
    puntajes = {
        "peaje": puntaje_peaje,
        "boleta": puntaje_boleta,
        "factura": puntaje_factura,
        "estacionamiento": puntaje_estacionamiento,
        "tarjeta de credito": puntaje_tarjeta_credito,
        "tarjeta de debito": puntaje_tarjeta_debito,
        "mall chino": puntaje_mall_chino,
        "disco duro": puntaje_disco_duro,
        "comprobante de giro": puntaje_comprobante_giro,
        "comprobante de depósito": puntaje_comprobante_deposito,
        "cupon": puntaje_cupon,
        "revision tecnica": puntaje_revision_tecnica,
        "seguro automotriz": puntaje_seguro_automotriz,
        "permiso de circulacion": puntaje_permiso_circulacion,
        "padron del vehiculo": puntaje_registro_vehiculo,
        "registro de propiedad": puntaje_registro_propiedad,
        "internet": puntaje_pago_servicios,
        "multa": puntaje_multa
    }

    resultado = max(puntajes, key=puntajes.get)

    return resultado