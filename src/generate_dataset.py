import os
import pandas as pd

def generate_benchmark_dataset(output_path="data/dataset_opiniones.csv"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    records = [
        {
            "id": 1,
            "fecha": "2026-10-01",
            "comentario": "El servicio fue excelente y la comida llegó rapidísimo. Muy recomendado.",
            "aspecto": "servicio",
            "sentimiento_real": "POS",
            "calificacion": 5
        },
        {
            "id": 2,
            "fecha": "2026-10-01",
            "comentario": "La comida tardó más de 45 minutos y llegó fría. Deplorable atención.",
            "aspecto": "tiempo",
            "sentimiento_real": "NEG",
            "calificacion": 1
        },
        {
            "id": 3,
            "fecha": "2026-10-02",
            "comentario": "El lugar es agradable, pero los precios son algo elevados para la porción.",
            "aspecto": "precio",
            "sentimiento_real": "NEU",
            "calificacion": 3
        },
        {
            "id": 4,
            "fecha": "2026-10-02",
            "comentario": "Pésimo trato del mesero, nos ignoró durante media hora.",
            "aspecto": "servicio",
            "sentimiento_real": "NEG",
            "calificacion": 1
        },
        {
            "id": 5,
            "fecha": "2026-10-03",
            "comentario": "Las hamburguesas tienen muy buen sabor, volvería sin duda alguna.",
            "aspecto": "comida",
            "sentimiento_real": "POS",
            "calificacion": 5
        },
        {
            "id": 6,
            "fecha": "2026-10-03",
            "comentario": "Atención regular, nada fuera de lo común. La limonada estaba tibia.",
            "aspecto": "comida",
            "sentimiento_real": "NEU",
            "calificacion": 3
        },
        {
            "id": 7,
            "fecha": "2026-10-04",
            "comentario": "Me encantó el postre de chocolate, excelente presentación.",
            "aspecto": "comida",
            "sentimiento_real": "POS",
            "calificacion": 5
        },
        {
            "id": 8,
            "fecha": "2026-10-04",
            "comentario": "La mesa estaba sucia al llegar y tardaron en limpiarla.",
            "aspecto": "limpieza",
            "sentimiento_real": "NEG",
            "calificacion": 2
        },
        {
            "id": 9,
            "fecha": "2026-10-05",
            "comentario": "Buena relación calidad-precio en el menú del día.",
            "aspecto": "precio",
            "sentimiento_real": "POS",
            "calificacion": 4
        },
        {
            "id": 10,
            "fecha": "2026-10-05",
            "comentario": "No me gustó la salsa, estaba demasiado salada y el aire acondicionado no servía.",
            "aspecto": "ambiente",
            "sentimiento_real": "NEG",
            "calificacion": 2
        }
    ]
    
    df = pd.DataFrame(records)
    df.to_csv(output_path, index=False, encoding="utf-8")
    print(f"Dataset generado exitosamente en: {output_path}")

if __name__ == "__main__":
    generate_benchmark_dataset()