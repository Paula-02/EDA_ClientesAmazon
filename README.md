<table>
<tr>
<td>

# Exploratory Data Analysis – Clientes Amazon

Análisis exploratorio del comportamiento de los clientes de Amazon a partir de un conjunto de datos de consumo online.

</td>
<td align="right">
<img src="src/img/logo.png" alt="Logo" width="80">
</td>
</tr>
</table>

## Versión en español

### Descripción e hipótesis

Este proyecto desarrolla un análisis exploratorio del comportamiento de compra online en Amazon, con el objetivo de identificar qué factores influyen en la finalización de una compra. En un contexto en el que el comercio electrónico tiene un peso cada vez mayor en el consumo global, comprender estos patrones resulta clave para mejorar la experiencia del usuario, detectar perfiles de comportamiento y optimizar las estrategias de venta.

Las hipótesis principales de este EDA son:

- A mayor edad, los usuarios dependen más de las reseñas para realizar una compra.  
- Los usuarios que navegan con mayor frecuencia en Amazon tienen una mayor probabilidad de completar una compra.  
- Los productos con un mayor número de reseñas se compran más que aquellos con menos reseñas.  
- Los usuarios tienden a dejar reseñas con mayor frecuencia cuando la experiencia con el producto ha sido negativa.  

A partir de estas hipótesis, el análisis busca responder a preguntas como:

- ¿Por qué los usuarios abandonan el carrito de compra?  
- ¿Existen distintos tipos de compradores según su comportamiento?  
- ¿Qué características presentan los usuarios que navegan con frecuencia pero compran poco o no compran?  
- ¿Qué factor tiene mayor peso en la decisión de compra: la frecuencia de uso, la edad o la confianza en las reseñas?  

### Fuente de datos

Dataset utilizado:  
[Amazon Consumer Behaviour Dataset](https://www.kaggle.com/datasets/swathiunnikrishnan/amazon-consumer-behaviour-dataset)

### Tecnologías utilizadas

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  
- VS Code  

### Estructura del repositorio

```text
EDA_ClientesAmazon/
├── src/
│   ├── data/         # Datos brutos y/o procesados
│   ├── img/          # Gráficos e imágenes generadas
│   ├── notebooks/    # Notebooks de análisis exploratorio
│   └── utils/        # Funciones auxiliares y utilidades
├── .gitattributes
├── Memoria.pdf
├── Presentacion.pdf
├── README.md
└── main.ipynb
```

### Instrucciones de reproducción

1. Clonar el repositorio.  
2. Crear y activar un entorno virtual.  
3. Instalar las dependencias necesarias.  
4. Descargar el dataset desde Kaggle y guardarlo en `src/data/`.  
5. Abrir y ejecutar `main.ipynb` desde la raíz del repositorio.  
6. Ejecutar las celdas en orden para reproducir el análisis.  

### Principales conclusiones

## H1: Edad y Reseñas
**Refutada.** La edad no influye significativamente en la importancia que los usuarios dan a las reseñas.

## H2: Navegación y Compra
**Parcialmente confirmada.** Una mayor frecuencia de navegación se asocia con un mayor número de compras, aunque la relación no es perfecta.

## H3: Impacto de las Reseñas
**Confirmación limitada.** Las reseñas afectan a la satisfacción y la confianza de los usuarios, pero no actúan como el único factor que impulsa la compra.

## H4: Reseñas Negativas
**Refutada.** Dejar reseñas es un hábito característico de usuarios activos y no una respuesta exclusiva a experiencias negativas. 

El análisis concluye que la **interacción del usuario en la plataforma**, como la navegación y la gestión del carrito, es el principal motor de compra, superando la relevancia de los factores demográficos.

Para optimizar la conversión, Amazon debe centrarse en la **competitividad de precios** y en reforzar la **credibilidad de su sistema de reseñas**.

### Autores

- Paula Comas – [GitHub](https://github.com/Paula-02) 
- Ana Corrochano Fraile – [GitHub](https://github.com/AnaCoFra) · [LinkedIn](https://www.linkedin.com/in/ana-corrochano-fraile-6bb551163/)  

---

## English version

### Project overview and hypotheses

This project presents an exploratory data analysis of online shopping behaviour on Amazon, with the aim of identifying the factors that influence the completion of an online purchase. In a context where e‑commerce plays an increasingly important role in global consumption, understanding these patterns is essential for improving user experience, identifying behavioural profiles, and optimizing sales strategies.

The main hypotheses of this EDA are:

- Older users rely more on reviews when making a purchase.  
- Users who browse Amazon more frequently are more likely to complete a purchase.  
- Products with a higher number of reviews are purchased more often than those with fewer reviews.  
- Users tend to leave reviews more frequently when the product has led to a negative experience.  

Based on these hypotheses, the analysis seeks to answer questions such as:

- Why do users abandon their shopping carts?  
- Are there different types of buyers according to their behaviour?  
- What characteristics define users who browse frequently but buy little or do not buy at all?  
- Which factor has the greatest influence on purchase decisions: usage frequency, age, or trust in reviews?  

### Data source

Dataset used:  
[Amazon Consumer Behaviour Dataset](https://www.kaggle.com/datasets/swathiunnikrishnan/amazon-consumer-behaviour-dataset)

### Technologies used

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  
- VS Code  

### Repository structure

```text
EDA_ClientesAmazon/
├── src/
│   ├── data/         # Raw and/or processed data
│   ├── img/          # Generated plots and images
│   ├── notebooks/    # Exploratory analysis notebooks
│   └── utils/        # Helper functions and utilities
├── .gitattributes
├── Memoria.pdf
├── Presentacion.pdf
├── README.md
└── main.ipynb
```

### Reproducibility instructions

1. Clone the repository.  
2. Create and activate a virtual environment.  
3. Install the required dependencies.  
4. Download the dataset from Kaggle and place it in `src/data/`.  
5. Open and run `main.ipynb` from the root directory of the repository.  
6. Execute the notebook cells in order to reproduce the analysis.  

### Main findings

## H1: Age and Reviews
**Refuted.** Age does not significantly influence the importance users place on reviews.

## H2: Browsing and Purchase
**Partially confirmed.** Higher browsing frequency is associated with a greater number of purchases, although the relationship is not perfect.

## H3: Review Impact
**Limited confirmation.** Reviews affect user satisfaction and trust, but they do not act as the sole driver of purchasing decisions.

## H4: Negative Reviews
**Refuted.** Leaving reviews is a habit of active users rather than an exclusive response to negative experiences.

The analysis concludes that **user interaction on the platform**, such as browsing and cart management, is the primary driver of purchases, outweighing the relevance of demographic factors.

To optimize conversion, Amazon should focus on **price competitiveness** and reinforcing the **credibility of its review system**.

### Authors

- Paula Comas – [GitHub](https://github.com/Paula-02)
- Ana Corrochano Fraile – [GitHub](https://github.com/AnaCoFra) · [LinkedIn](https://www.linkedin.com/in/ana-corrochano-fraile-6bb551163/)  
