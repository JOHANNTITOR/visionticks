
# 🚗 Clasificador Inteligente de Tickets de Peajes

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Estado](https://img.shields.io/badge/Estado-En%20desarrollo-green)
![Licencia](https://img.shields.io/badge/Licencia-Académica-lightgrey)

> Sistema de clasificación automática de tickets de peajes mediante técnicas de **Machine Learning**, utilizando modelos supervisados y etiquetado de documentos para identificar automáticamente el concesionario de origen.

---

# 📖 Descripción

Este proyecto implementa un sistema de Inteligencia Artificial capaz de **clasificar automáticamente tickets de peajes** pertenecientes a distintas concesionarias.

El sistema aprende a partir de un conjunto de tickets previamente etiquetados, extrayendo patrones presentes en el texto mediante técnicas de Procesamiento de Lenguaje Natural (NLP) y utilizando algoritmos de clasificación supervisada.

Una vez entrenado, el modelo puede identificar automáticamente el concesionario correspondiente incluso cuando existen diferencias de formato, tipografía o estructura entre los comprobantes.

El proyecto está diseñado para crecer continuamente, permitiendo incorporar nuevos tickets etiquetados y reentrenar el modelo para mejorar su precisión.

---

# ✨ Características

- 🎫 Clasificación automática de tickets de peajes.
- 🧠 Aprendizaje supervisado mediante etiquetas.
- 🏷️ Entrenamiento basado en documentos previamente clasificados.
- 📄 Procesamiento automático del texto OCR.
- 🔍 Identificación del concesionario.
- 📈 Entrenamiento incremental con nuevos ejemplos.
- ⚡ Predicción en tiempo real.
- 📊 Comparación entre múltiples algoritmos de clasificación.
- 💾 Persistencia del modelo entrenado.
- 📱 Interfaz desarrollada con Streamlit.

---

# 🛠 Tecnologías

| Tecnología | Función |
|------------|---------|
| Python | Lenguaje principal |
| Scikit-learn | Modelos de Machine Learning |
| Streamlit | Interfaz gráfica |
| Pandas | Manejo de datos |
| NumPy | Operaciones numéricas |
| Joblib | Serialización del modelo |
| Regex | Limpieza del texto |
| TF-IDF | Vectorización del texto |
| OCR | Extracción de texto desde imágenes |

---

# 📂 Estructura del proyecto

```text
ClasificadorPeajes
│
├── app.py
├── entrenamiento.py
├── clasificador.py
├── modelo.pkl
├── vectorizador.pkl
├── dataset.csv
├── requirements.txt
└── README.md
```

---

# 📈 Flujo del sistema

```text
              Imagen Ticket
                    │
                    ▼
              OCR / Texto
                    │
                    ▼
        Limpieza del documento
                    │
                    ▼
      Tokenización del texto
                    │
                    ▼
      Vectorización TF-IDF
                    │
                    ▼
     Modelo de Clasificación
                    │
          ┌─────────┴──────────┐
          ▼                    ▼
     Entrenamiento        Predicción
          │                    │
          └─────────┬──────────┘
                    ▼
        Concesionaria detectada
```

---

# 📋 Variables utilizadas

| Variable | Tipo |
|----------|------|
| Texto OCR | Texto |
| Fecha | Texto |
| Hora | Texto |
| Plaza de Peaje | Texto |
| Nombre Concesionaria | Etiqueta |
| Categoría Vehículo | Texto |
| Monto | Numérica |
| Forma de Pago | Texto |

---

# 🏷️ Etiquetas de clasificación

Cada ticket pertenece a una clase previamente definida.

Ejemplo:

| Texto OCR | Etiqueta |
|------------|-----------|
| Ruta del Maipo Plaza Angostura... | Ruta del Maipo |
| Costanera Norte Pórtico 15... | Costanera Norte |
| Autopista Central Troncal... | Autopista Central |
| Vespucio Norte Express... | Vespucio Norte |
| Ruta 68 Lo Prado... | Ruta 68 |
| Túnel El Melón... | Túnel El Melón |

---

# 📊 Conjunto de entrenamiento

El sistema aprende desde un archivo CSV con una estructura similar a:

| texto | etiqueta |
|--------|-----------|
| RUTA DEL MAIPO PLAZA ANGOSTURA... | Ruta del Maipo |
| AUTOPISTA CENTRAL TRONCAL SUR... | Autopista Central |
| COSTANERA NORTE PEAJE... | Costanera Norte |

Cada registro corresponde a un ticket previamente identificado.

---

# 🧹 Preprocesamiento

Antes del entrenamiento el sistema realiza automáticamente:

- Conversión a mayúsculas.
- Eliminación de caracteres especiales.
- Eliminación de puntuación.
- Eliminación de espacios repetidos.
- Eliminación de palabras irrelevantes (Stop Words).
- Normalización del texto.
- Vectorización mediante TF-IDF.

---

# 🤖 Algoritmos de clasificación implementados

El proyecto permite evaluar distintos modelos supervisados para determinar cuál ofrece la mejor precisión.

| Algoritmo | Tipo |
|-----------|------|
| ✅ Regresión Logística | Clasificación lineal |
| ✅ Naive Bayes Multinomial | Probabilístico |
| ✅ Support Vector Machine (SVM) | Margen máximo |
| ✅ Random Forest | Ensemble |
| ✅ Decision Tree | Árbol de decisión |
| ✅ K-Nearest Neighbors (KNN) | Basado en vecinos |
| ✅ Gradient Boosting | Ensemble |
| ✅ AdaBoost | Ensemble |
| ✅ Extra Trees | Ensemble |
| ✅ Linear SVC | Clasificación lineal |
| ✅ SGD Classifier | Descenso de Gradiente |
| ✅ Passive Aggressive | Clasificación online |
| ✅ Ridge Classifier | Clasificación lineal regularizada |

---

# ⭐ Modelo recomendado

Para clasificación de tickets OCR, el modelo recomendado es:

**Regresión Logística + TF-IDF**

Ventajas:

- Alta precisión.
- Muy rápido.
- Excelente desempeño en clasificación de texto.
- Fácil de entrenar.
- Poco consumo de memoria.
- Muy robusto frente a errores de OCR.

---

# 🎯 Entrenamiento del modelo

Durante el entrenamiento se ejecutan automáticamente las siguientes etapas:

- Lectura del dataset.
- Limpieza del texto.
- Tokenización.
- Vectorización TF-IDF.
- División entrenamiento/prueba.
- Entrenamiento del modelo.
- Validación.
- Cálculo de Accuracy.
- Precision Score.
- Recall.
- F1 Score.
- Matriz de confusión.
- Guardado del modelo.

---

# 📊 Métricas de evaluación

El sistema calcula automáticamente:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC AUC (clasificación binaria)
- Confusion Matrix
- Classification Report

---

# 🔍 Predicción

El usuario puede ingresar:

- Texto OCR obtenido desde un ticket.
- Texto copiado manualmente.
- Documento procesado desde una imagen.

El sistema identifica automáticamente:

- 🏷️ Concesionaria
- 📊 Probabilidad de pertenencia
- 📈 Nivel de confianza del modelo

---

# ➕

## Agregar nuevos tickets

La aplicación permite incorporar nuevos documentos etiquetados.

Cada nuevo ticket queda almacenado dentro del conjunto de entrenamiento para futuras versiones del modelo.

---

# 🔄 Reentrenamiento

El modelo puede reentrenarse cada vez que se agregan nuevos tickets.

Esto permite aumentar progresivamente la precisión y adaptarse a nuevos formatos de impresión.

---

# 💡 Futuras mejoras

- 📷 Clasificación directa desde imágenes.
- 🤖 Integración con modelos Vision.
- ☁️ Entrenamiento automático en la nube.
- 🧠 Redes neuronales profundas.
- 🔎 Detección automática de anomalías.
- 📈 Aprendizaje incremental.
- 🌎 Clasificación de peajes internacionales.
- 🗂️ Clasificación por tipo de documento.
- ⚡ API REST para clasificación en tiempo real.
- 📱 Aplicación móvil.

---

# ▶️ Ejecución

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar la aplicación:

```bash
streamlit run app.py
```

---

# 📦 Dependencias

```text
streamlit
pandas
numpy
scikit-learn
joblib
nltk
regex
matplotlib
scipy
```

---

# 📚 Fundamentos de Machine Learning utilizados

El proyecto aplica conceptos fundamentales de aprendizaje supervisado:

- Aprendizaje Supervisado (Supervised Learning)
- Clasificación Multiclase
- Ingeniería de Características (Feature Engineering)
- Procesamiento de Lenguaje Natural (NLP)
- TF-IDF
- Tokenización
- Vectorización
- Validación Cruzada
- Entrenamiento y Test
- Selección de Modelos
- Optimización de Hiperparámetros
- Evaluación mediante métricas estadísticas

---

# 👨‍💻 Autor

**Juan Andrés Sánchez Dodero**

Proyecto de Inteligencia Artificial Aplicada al Reconocimiento Automático de Tickets de Peajes mediante Machine Learning y Procesamiento de Lenguaje Natural.

---

# 📄 Licencia

Este proyecto ha sido desarrollado con fines académicos, de investigación y experimentación en Machine Learning.

El procesamiento de documentos debe cumplir con la legislación vigente sobre protección de datos personales y privacidad aplicable en cada país.
