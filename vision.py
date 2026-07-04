# importar librerias
import streamlit as st
from openai import OpenAI
from openai import RateLimitError
from PIL import Image
import base64
from io import BytesIO
import json

# librerías locales
import clasificador

# declarar si o si
response = None

# guardar estados

if "continuar" not in st.session_state:
    st.session_state.continuar = False

if "respuesta" not in st.session_state:
    st.session_state.respuesta = None

if "paquete_texto" not in st.session_state:
    st.session_state.paquete_texto = None

if "paquete_json" not in st.session_state:
    st.session_state.paquete_json = None

if "imagen" not in st.session_state:
    st.session_state.imagen = None



# incluye clave API_KEY desde entorno
client = OpenAI(
    api_key = st.secrets["OPENAI_API_KEY"]
)

#---------
#funciones
#---------

# función para clasificar texto detectado
def clasificar_texto(respuesta):
    # almacena texto en variable para clasificar
    texto = respuesta.output_text

    # clasifica el texto detectado
    
    clasificacion = clasificador.clasificar_documento(texto)
    st.write("Clasificación del documento:")
    st.subheader(clasificacion)

    return clasificacion

def prompt_para_extraer_texto(img_base64, client):
    
    # llama a modelo AI + inputs
    
    respuesta = client.responses.create(
        model="gpt-4.1-mini",
        input=[{
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Extrae todo el texto de esta imagen. No agregues explicaciones."
                },
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{img_base64}"
                }
            ]
        }]
    )

    return respuesta

def promt_para_convertir_texto_a_json(texto, client):
    # llama a modelo AI + inputs
    
    prompt_system = """
    Eres un experto en extracción de datos desde boletas electrónicas chilenas.

    Tu tarea es convertir el texto OCR en un JSON válido.

    Reglas:
    - Devuelve únicamente un JSON.
    - No agregues explicaciones.
    - No uses markdown.
    - No escribas ```json.
    - Si un dato no existe usa null.
    - Los montos deben ser números enteros.
    - Las fechas deben tener formato YYYY-MM-DD.
    - Los productos deben ir en un arreglo llamado "items".
    - Si una descripción ocupa varias líneas, únelas.
    - No inventes información.
    """

    paquete_json = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": prompt_system},
            {"role": "user", "content": texto}
        ]
    )

    return paquete_json.output_text

def decodificar_imagen_a_base64(imagen):
    # almacena imagen en la RAM temporalmente
    buffer = BytesIO()
    imagen.save(buffer, format="JPEG")
    
    # transforma de binario a texto imprimible
    img_base64 = base64.b64encode(
        buffer.getvalue()
    ).decode()

    return img_base64

def enviar_paquetes(paquete_texto, paquete_json, tipo):
    # prepara datos para enviar a la API

    import requests

  # URL de la API
    url = "http://www.androbit.cl/api/"
    # url = "http://localhost/dashboard/androbit.cl/api/"

    # API Key
    headers = {
        "X-API-Key": "58e5159435a817494e4275c82a60ac153bf7826df52b393a36e9bec1133e0949",
        "Content-Type": "application/json"
    }

    # Datos
    datos = {
        "paquete_texto": paquete_texto,
        "paquete_json": paquete_json,
        "clasificacion": tipo
    }

    # Envío
    respuesta_servidor = requests.post(
        url,
        json=datos,
        headers=headers
    )

    # respuesta del servidor al enviar datos a la API
    # respuesta_servidor = requests.post(url, json=datos)

    st.write(respuesta_servidor.status_code)
    st.write(respuesta_servidor.text)
    # st.write(respuesta_servidor.json())


    st.write("Enviado a la API...")

#----------------
# presenta título
#----------------

st.title("Visionticks 1.0")
st.write("Clasifica tickets de peajes, boletas y facturas usando IA")

#---------------------------
#tipo de carga de imagen
#---------------------------

opcion = st.toggle("como ingresar tu imagen")

#opciones de carga de imagen
if opcion and st.session_state.respuesta is None: # Ejecutar OCR solo una vez
    st.write("foto")
else:
    st.write("disco duro")

st.write("elijiste una opción")

if "continuar" not in st.session_state:
    st.session_state.continuar = False

# el usuario presiona el botón para continuar
if st.button("Continuar"):
    st.session_state.continuar = True

# state para no perder la opción elegida al recargar la página
if st.session_state.continuar:

    # si el usuario elige tomar foto
    if opcion and st.session_state.respuesta is None: # Ejecutar OCR solo una vez
        st.write("elegiste tomar foto")

        # abrir camara para tomar foto
        foto = st.camera_input("Toma una foto")

        # si cámara tiene algún valor
        if foto and st.session_state.respuesta is None: # Ejecutar OCR solo una vez
            # i/o
            imagen = Image.open(foto)
            st.image(imagen, caption="Imagen cargada")
            
            # llama a la función para decodificar la imagen a base64
            img_base64 = decodificar_imagen_a_base64(imagen)

            # prompt para extraer texto de la imagen usando el modelo AI
            try:
                respuesta = prompt_para_extraer_texto(img_base64, client)

            except AttributeError:
                st.error("Error: No se pudo obtener la respuesta del modelo. Verifica la conexión y la cuota de OpenAI.")

            try:
                # muestra respuesta en texto plano
                paquete_texto = respuesta.output_text
                st.text_area(
                "Texto detectado",
                paquete_texto,
                height=300
            )

                # llama a la función para clasificar el texto detectado
                tipo = clasificar_texto(respuesta)

                #boton para convertir texto a JSON y mostrarlo en pantalla
                if st.button("Convertir a JSON") and st.session_state.paquete_json is None:
                    try:
                        paquete_json = promt_para_convertir_texto_a_json(respuesta.output_text, client)

                        # muestra JSON
                        st.text_area(
                            "JSON generado",
                            paquete_json,
                            height=300
                        )

                    except AttributeError:
                        st.error("Error: No se pudo obtener la respuesta del modelo. Verifica la conexión y la cuota de OpenAI.")

                    if st.button("Envíar datos a la API"):
                        enviar_paquetes(paquete_texto, paquete_json, tipo)

            except AttributeError:
                st.error("Error: No se pudo obtener la respuesta del modelo. Verifica la conexión y la cuota de OpenAI.")

    #----------------------------------------------------------------------------  

    # si el usuario elige cargar imagen desde disco duro
    else:
        st.write("elegiste discoduro")

        # cargar archivo de imagen desde discoduro
        foto = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg", "webp", "tiff", "gif"])

        # si cámara tiene algún valor
        if foto and st.session_state.respuesta is None: # Ejecutar OCR solo una vez
    
            # i/o
            imagen = Image.open(foto)
            st.image(imagen, caption="Imagen cargada")

            # llama a la función para decodificar la imagen a base64
            img_base64 = decodificar_imagen_a_base64(imagen)

            # prompt para extraer texto de la imagen usando el modelo AI
            try:
                respuesta = prompt_para_extraer_texto(img_base64, client)

            except AttributeError:
                st.error("Error: No se pudo obtener la respuesta del modelo. Verifica la conexión y la cuota de OpenAI.")

            # muestra respuesta en texto plano
            paquete_texto = respuesta.output_text
            st.text_area(
                "Texto detectado",
                paquete_texto,
                height=300
            )

            # llama a la función para clasificar el texto detectado
            tipo = clasificar_texto(respuesta)

            #boton para convertir texto a JSON y mostrarlo en pantalla
            if st.button("Convertir a JSON") and st.session_state.paquete_json is None:  # Ejecutar conversión a JSON solo una vez
                try:
                    paquete_json = promt_para_convertir_texto_a_json(respuesta.output_text, client)

                    # muestra JSON
                    st.text_area(
                        "JSON generado",
                        paquete_json,
                        height=300
                    )

                    # enviar datos a la API
                    enviar_paquetes(paquete_texto, paquete_json, tipo)

                except AttributeError:
                    st.error("Error: No se pudo obtener la respuesta del modelo. Verifica la conexión y la cuota de OpenAI.")

