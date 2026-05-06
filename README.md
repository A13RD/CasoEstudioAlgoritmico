# 🚚 Trabajo Final — Sistema de Logística y Entregas

## Análisis y Diseño de Algoritmos — 2026-1

---

## 📌 Descripción del Proyecto

Este proyecto aborda el problema de optimización en un **sistema de logística y entregas**, donde una empresa de paquetería debe distribuir eficientemente paquetes utilizando una flota de camiones.

El objetivo es implementar y comparar diferentes técnicas algorítmicas para resolver el problema, analizando su eficiencia, complejidad y calidad de solución.

---

## 🎯 Problema

Se tienen:

* `n` paquetes, cada uno con:

  * Destino
  * Peso
  * Ventana de entrega (tiempo)
* `m` camiones, cada uno con:

  * Capacidad máxima de carga

### 🔍 Objetivos

* Asignar paquetes a camiones sin exceder su capacidad
* Determinar el orden óptimo de entregas
* Cumplir con restricciones de tiempo

---

## 🧠 Enfoques Algorítmicos

Se implementan y comparan las siguientes técnicas:

### 1. Fuerza Bruta

* Explora todas las combinaciones posibles
* Garantiza solución óptima
* Muy costosa computacionalmente

### 2. Recursividad

* Reformulación del problema de manera recursiva
* Permite entender la estructura del problema

### 3. Greedy (Voraz)

* Selección local óptima (ej: asignar paquetes más livianos primero)
* Rápido pero no siempre óptimo

### 4. Backtracking

* Explora soluciones posibles con poda
* Reduce el espacio de búsqueda

### 5. Divide y Vencerás

* Divide el problema en subconjuntos de paquetes
* Combina soluciones parciales

---

## 📊 Comparación de Técnicas

Se evaluarán según:

* Complejidad temporal (Big O)
* Complejidad espacial
* Calidad de solución (óptima o no)
* Tiempo de ejecución real

---

## 📁 Estructura del Proyecto

```
trabajo-final/
├── README.md
├── datos/
│   ├── caso_pequeno.txt
│   ├── caso_mediano.txt
│   └── caso_grande.txt
├── src/
│   ├── fuerza_bruta.py
│   ├── recursivo.py
│   ├── greedy.py
│   ├── backtracking.py
│   ├── divide_y_venceras.py
│   └── comparativa.py
├── docs/
│   ├── entrega1.pdf
│   ├── entrega2.pdf
│   └── entrega3_final.pdf
└── presentacion/
    └── presentacion_final.pdf
```

---

## 🧪 Datos de Prueba

Se utilizan tres conjuntos de datos:

* **Pequeño:** Validación básica
* **Mediano:** Evaluación intermedia
* **Grande:** Análisis de rendimiento

Cada dataset incluye paquetes con diferentes pesos, destinos y horarios.

---

## ⚙️ Ejecución

1. Clonar repositorio:

```bash
git clone <repo-url>
cd trabajo-final
```

2. Ejecutar comparativa:

```bash
python src/comparativa.py
```

---

## 📈 Resultados Esperados

* Identificar qué algoritmo es más eficiente
* Analizar trade-offs entre tiempo y optimalidad
* Determinar el mejor enfoque para sistemas reales de logística

---

## 🧾 Conclusiones (Esperadas)

* La fuerza bruta garantiza optimalidad pero no escala
* Greedy es eficiente pero puede fallar
* Backtracking ofrece buen balance
* Divide y vencerás depende de cómo se divida el problema

---

## 👥 Integrantes

* Alejandro Ruiz Diaz
* Sebastian Rendon Grisales

---

## ⚠️ Consideraciones

* Todo el código debe ser ejecutable
* Se deben incluir pruebas propias
* Se evaluará el uso correcto de Git (commits)

---

## 🚀 Objetivo Académico

Aplicar múltiples paradigmas algorítmicos sobre un mismo problema real para desarrollar criterio en la selección de técnicas de optimización.

---
