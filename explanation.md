# Creating an Interactive Venn Diagram with Plotly

This document provides a detailed, step-by-step explanation of how to create an interactive Venn diagram using Plotly. The Venn diagram visualizes the relationships between Deterministic, Probabilistic, and Non-Probabilistic AI/ML models.

## Key Concepts

### Plotly

Plotly is a graphing library that makes interactive, publication-quality graphs online. It supports a wide range of chart types and is highly customizable.

### Venn Diagram

A Venn diagram is a diagram that shows all possible logical relations between a finite collection of different sets. In this project, we use a Venn diagram to represent the relationships between different types of AI/ML models.

## Step-by-Step Guide

### 1. Importing Plotly

First, we import the necessary module from Plotly:

```python
import plotly.graph_objects as go
```

### 2. Defining Variables

We define the positions, sizes, labels, hover texts, and colors for the circles and their sections:

```python
x_positions = [0.3, 0.7, 0.5]
y_positions = [0.7, 0.7, 0.4]
sizes = [400, 400, 400]
labels = [
    "Deterministic\n(e.g., Sorting Algorithms, Rule-based Systems)",
    "Probabilistic\n(e.g., Bayesian Networks, GANs)",
    "Non-Probabilistic\n(e.g., SVMs, K-means Clustering)",
    "Deterministic & Probabilistic\n(e.g., Ensemble Models)",
    "Deterministic & Non-Probabilistic\n(e.g., Decision Trees)",
    "Probabilistic & Non-Probabilistic\n(Hybrid Approaches)",
    "All Three\n(Theoretical/Niche Systems)"
]
hover_texts = [
    "Deterministic<br>Sorting Algorithms, Rule-based Systems",
    "Probabilistic<br>Bayesian Networks, GANs",
    "Non-Probabilistic<br>SVMs, K-means Clustering",
    "Deterministic & Probabilistic<br>Ensemble Models",
    "Deterministic & Non-Probabilistic<br>Decision Trees",
    "Probabilistic & Non-Probabilistic<br>Hybrid Approaches",
    "All Three<br>Theoretical/Niche Systems"
]
hover_positions = [
    (0.4, 0.5),
    (0.65, 0.5),
    (0.5, 0.3),
    (0.55, 0.5),
    (0.45, 0.4),
    (0.6, 0.4),
    (0.55, 0.4)
]
hover_colors = [
    'rgba(255, 99, 132, 0.8)',
    'rgba(54, 162, 235, 0.8)',
    'rgba(153, 102, 255, 0.8)',
    'rgba(50, 50, 50, 0.8)',
    'rgba(50, 50, 50, 0.8)',
    'rgba(50, 50, 50, 0.8)',
    'rgba(30, 30, 30, 0.8)'
]
```

### 3. Creating the Figure

We create a figure using `go.Figure()`:

```python
fig = go.Figure()
```

### 4. Adding Circles

We add circles to the figure using `go.Shape`:

```python
fig.update_layout(
    shapes=[
        dict(
            type="circle",
            xref="x",
            yref="y",
            x0=0.25,
            y0=0.35,
            x1=0.55,
            y1=0.65,
            fillcolor='rgba(255, 99, 132, 0.5)',
            line=dict(color='black')
        ),
        dict(
            type="circle",
            xref="x",
            yref="y",
            x0=0.45,
            y0=0.35,
            x1=0.75,
            y1=0.65,
            fillcolor='rgba(54, 162, 235, 0.5)',
            line=dict(color='black')
        ),
        dict(
            type="circle",
            xref="x",
            yref="y",
            x0=0.35,
            y0=0.15,
            x1=0.65,
            y1=0.45,
            fillcolor='rgba(153, 102, 255, 0.5)',
            line=dict(color='black')
        )
    ]
)
```

### 5. Adding Hover Text

We add interactive hover text using `go.Scatter`:

```python
for (x, y), text, color in zip(hover_positions, hover_texts, hover_colors):
    fig.add_trace(go.Scatter(
        x=[x],
        y=[y],
        mode="markers",
        marker=dict(size=30, opacity=0.01),
        hoverinfo="text",
        text=[text],
        hoverlabel=dict(
            bgcolor=color,
            font=dict(color='white')
        ),
        showlegend=False
    ))
```

### 6. Adding a Legend

We add a legend to the upper right corner:

```python
fig.update_layout(
    shapes=[
        dict(
            type="rect",
            xref="x",
            yref="y",
            x0=0.9,
            y0=0.9,
            x1=0.925,
            y1=0.925,
            fillcolor='rgba(255, 99, 132, 0.8)',
            line=dict(width=0)
        ),
        dict(
            type="rect",
            xref="x",
            yref="y",
            x0=0.9,
            y0=0.85,
            x1=0.925,
            y1=0.875,
            fillcolor='rgba(54, 162, 235, 0.8)',
            line=dict(width=0)
        ),
        dict(
            type="rect",
            xref="x",
            yref="y",
            x0=0.9,
            y0=0.8,
            x1=0.925,
            y1=0.825,
            fillcolor='rgba(153, 102, 255, 0.8)',
            line=dict(width=0)
        ),
        dict(
            type="rect",
            xref="x",
            yref="y",
            x0=0.88,
            y0=0.78,
            x1=1.15,
            y1=0.93,
            fillcolor='rgba(0,0,0,0)',
            line=dict(color='black', width=1)
        )
    ],
    annotations=[
        dict(
            xref="x",
            yref="y",
            x=0.93,
            y=0.9125,
            xanchor="left",
            yanchor="middle",
            text="Deterministic",
            showarrow=False,
            font=dict(color="black", size=12)
        ),
        dict(
            xref="x",
            yref="y",
            x=0.93,
            y=0.8625,
            xanchor="left",
            yanchor="middle",
            text="Probabilistic",
            showarrow=False,
            font=dict(color="black", size=12)
        ),
        dict(
            xref="x",
            yref="y",
            x=0.93,
            y=0.8125,
            xanchor="left",
            yanchor="middle",
            text="Non-Probabilistic",
            showarrow=False,
            font=dict(color="black", size=12)
        )
    ]
)
```

### 7. Adding Instructions

We add instructions on how to interact with the Venn diagram:

```python
fig.update_layout(
    annotations=[
        dict(
            xref="paper",
            yref="paper",
            x=0.5,
            y=-0.1,
            xanchor="center",
            yanchor="top",
            text="Interact with the Venn diagram by hovering over the sections.",
            showarrow=False,
            font=dict(color="black", size=12)
        )
    ],
    margin=dict(l=100, r=100, t=100, b=150)
)
```

### 8. Displaying the Figure

Finally, we display the figure:

```python
fig.show()
```

## Helpful Pointers on Working with Plotly

- **Customization**: Plotly provides extensive customization options for creating interactive and visually appealing charts.
- **Interactivity**: Use hover texts and interactive elements to enhance the user experience.
- **Annotations**: Add annotations to provide additional information and instructions.
- **Layout**: Adjust the layout to ensure that all elements are properly positioned and visible.

By following these steps, you can create an interactive Venn diagram using Plotly to visualize complex relationships between different sets.