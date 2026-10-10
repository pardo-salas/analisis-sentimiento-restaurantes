# Prototipado Rápido para Análisis de Sentimientos en Reseñas de Restaurantes

## Descripción del Proyecto
Este repositorio contiene el prototipo funcional de evaluación e implementación comparativa de modelos preentrenados del ecosistema **Hugging Face** para la clasificación automática de opiniones en el sector restaurantero. El proyecto utiliza **Google Colab** acelerado por GPU como entorno de prototipado rápido para contrastar la precisión, latencia y eficiencia de diferentes arquitecturas Transformer en idioma español.

## Entorno de Ejecución
* **Plataforma de Prototipado:** Google Colab
* **Acelerador por Hardware:** GPU NVIDIA T4 (CUDA activado)
* **Lenguaje de Programación:** Python 3.10+
* **Frameworks Principales:** PyTorch, Hugging Face `transformers`, `evaluate`, `scikit-learn` y `pandas`

## Estructura del Repositorio
```text
.
├── data/
│   └── dataset_opiniones.csv        # Dataset de prueba estandarizado
├── notebooks/
│   └── prototipo_colab_huggingface.ipynb # Notebook interactivo con celdas de inferencia
├── results/
│   └── metricas_comparativas.json   # Resultados de evaluación en formato JSON
├── src/
│   ├── generate_dataset.py          # Script de generación del dataset
│   └── evaluate_models.py           # Pipeline ejecutable de evaluación
├── .gitignore
├── README.md                        # Documentación principal del proyecto
└── requirements.txt                 # Dependencias del proyecto

## Resumen de Resultados Reales

| Modelo Evaluado | Accuracy | Precision | Recall | F1-Score | Latencia Promedio |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **BETO Sentiment (Español)** | **1.0000** | **1.0000** | **1.0000** | **1.0000** | **55.54 ms** |
| `pysentimiento/robertuito-sentiment-analysis` | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 194.86 ms |
| `cardiffnlp/twitter-xlm-roberta-base-sentiment` | 0.8000 | 0.6667 | 0.8000 | 0.7200 | 22.17 ms |

### Conclusión Técnica
* **Modelo Elegido:** `finiteautomata/beto-sentiment-analysis` debido a su puntuación perfecta (F1-Score: 1.0) y su baja latencia (55.54 ms por reseña).
* **Observación de Rendimiento:** XLM-RoBERTa demostró menor latencia (22.17 ms), pero con una degradación notable en precisión (F1-Score de 0.72), confirmando que los modelos especializados en español superan a las opciones multilingües generales para este dominio.