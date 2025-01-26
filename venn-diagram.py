import plotly.graph_objects as go
"""
This script creates an interactive Venn diagram using Plotly to visualize the relationships between 
Deterministic, Probabilistic, and Non-Probabilistic AI/ML models. The diagram includes labeled sections 
for individual and overlapping categories, with hover text providing additional information.

Modules:
    plotly.graph_objects: Used to create the Venn diagram and add interactive elements.

Variables:
    x_positions (list): X-coordinates for the centers of the circles.
    y_positions (list): Y-coordinates for the centers of the circles.
    sizes (list): Sizes of the circles.
    labels (list): Labels for the individual and overlapping sections.
    hover_texts (list): Text to display when hovering over each section.
    hover_positions (list): Positions for the hover text.
    hover_colors (list): Background colors for the hover text.

Functions:
    None

Usage:
    Run the script to display the interactive Venn diagram in a web browser. The diagram can also be saved 
    as an HTML file by uncommenting the relevant lines at the end of the script.
"""

# Define updated positions and sizes based on the static image
x_positions = [0.3, 0.7, 0.5]  # Positions for the centers of the circles
y_positions = [0.7, 0.7, 0.4]
sizes = [400, 400, 400]         # Circle sizes

# Define labels for the individual and overlapping sections
labels = [
    "Deterministic\n(e.g., Sorting Algorithms, Rule-based Systems)",
    "Probabilistic\n(e.g., Bayesian Networks, GANs)",
    "Non-Probabilistic\n(e.g., SVMs, K-means Clustering)",
    "Deterministic & Probabilistic\n(e.g., Ensemble Models)",
    "Deterministic & Non-Probabilistic\n(e.g., Decision Trees)",
    "Probabilistic & Non-Probabilistic\n(Hybrid Approaches)",
    "All Three\n(Theoretical/Niche Systems)"
]

# Create the figure
fig = go.Figure()

# Add circles using go.Shape with reduced horizontal overlap
fig.update_layout(
    shapes=[
        # Deterministic
        dict(
            type="circle",
            xref="x",
            yref="y",
            x0=0.3,  # Shifted right by 0.05
            y0=0.4,
            x1=0.6,  # Shifted right by 0.05
            y1=0.7,
            fillcolor='rgba(255, 99, 132, 0.5)',
            line=dict(color='black')
        ),
        # Probabilistic
        dict(
            type="circle",
            xref="x",
            yref="y",
            x0=0.5,  # Shifted right by 0.05
            y0=0.4,
            x1=0.8,  # Shifted right by 0.05
            y1=0.7,
            fillcolor='rgba(54, 162, 235, 0.5)',
            line=dict(color='black')
        ),
        # Non-Probabilistic
        dict(
            type="circle",
            xref="x",
            yref="y",
            x0=0.4,  # Shifted right by 0.05
            y0=0.2,
            x1=0.7,  # Shifted right by 0.05
            y1=0.5,
            fillcolor='rgba(153, 102, 255, 0.5)',
            line=dict(color='black')
        ),
        # Colored Boxes for Legend
        dict(
            type="rect",
            xref="x",
            yref="y",
            x0=0.85,  # Repositioned to the right
            y0=0.7,
            x1=0.875,
            y1=0.725,
            fillcolor='rgba(255, 99, 132, 0.8)',  # Deterministic Color
            line=dict(width=0)
        ),
        dict(
            type="rect",
            xref="x",
            yref="y",
            x0=0.85,
            y0=0.65,
            x1=0.875,
            y1=0.675,
            fillcolor='rgba(54, 162, 235, 0.8)',  # Probabilistic Color
            line=dict(width=0)
        ),
        dict(
            type="rect",
            xref="x",
            yref="y",
            x0=0.85,
            y0=0.6,
            x1=0.875,
            y1=0.625,
            fillcolor='rgba(153, 102, 255, 0.8)',  # Non-Probabilistic Color
            line=dict(width=0)
        )
    ],
    annotations=[
        # Text Labels for Legend
        dict(
            xref="x",
            yref="y",
            x=0.88,  # Repositioned to align with legend boxes
            y=0.715,
            xanchor="left",
            yanchor="middle",
            text="Deterministic",
            showarrow=False,
            font=dict(color="black", size=12)
        ),
        dict(
            xref="x",
            yref="y",
            x=0.88,  # Repositioned to align with legend boxes
            y=0.665,
            xanchor="left",
            yanchor="middle",
            text="Probabilistic",
            showarrow=False,
            font=dict(color="black", size=12)
        ),
        dict(
            xref="x",
            yref="y",
            x=0.88,  # Repositioned to align with legend boxes
            y=0.615,
            xanchor="left",
            yanchor="middle",
            text="Non-Probabilistic",
            showarrow=False,
            font=dict(color="black", size=12)
        )
    ]
)

# Update hover texts without HTML styling
hover_texts = [
    # Non-Overlapping Labels
    "Deterministic<br>Sorting Algorithms, Rule-based Systems",
    "Probabilistic<br>Bayesian Networks, GANs",
    "Non-Probabilistic<br>SVMs, K-means Clustering",
    # Overlapping Labels
    "Deterministic & Probabilistic<br>Ensemble Models",
    "Deterministic & Non-Probabilistic<br>Decision Trees",
    "Probabilistic & Non-Probabilistic<br>Hybrid Approaches",
    "All Three<br>Theoretical/Niche Systems"
]

# Update hover positions to correctly align with overlapping sections
hover_positions = [
    # Non-Overlapping Positions
    (0.35, 0.55),   # Deterministic Non-Overlapping
    (0.7, 0.55),    # Probabilistic Non-Overlapping
    (0.55, 0.35),   # Non-Probabilistic Non-Overlapping
    # Overlapping Positions
    (0.55, 0.55),   # Deterministic & Probabilistic Overlap
    (0.45, 0.45),   # Deterministic & Non-Probabilistic Overlap
    (0.65, 0.45),   # Probabilistic & Non-Probabilistic Overlap
    (0.55, 0.45)    # All Three Overlap
]

# Define hover background colors corresponding to each label with darker overlaps
hover_colors = [
    # Non-Overlapping Labels
    'rgba(255, 99, 132, 0.8)',    # Deterministic
    'rgba(54, 162, 235, 0.8)',    # Probabilistic
    'rgba(153, 102, 255, 0.8)',   # Non-Probabilistic
    # Overlapping Labels
    'rgba(50, 50, 50, 0.8)',      # Deterministic & Probabilistic Overlap
    'rgba(50, 50, 50, 0.8)',      # Deterministic & Non-Probabilistic Overlap
    'rgba(50, 50, 50, 0.8)',      # Probabilistic & Non-Probabilistic Overlap
    'rgba(30, 30, 30, 0.8)'       # All Three Overlap
]

# Add interactive hover text using Scatter with updated positions and hover colors
for (x, y), text, color in zip(hover_positions, hover_texts, hover_colors):
    fig.add_trace(go.Scatter(
        x=[x],
        y=[y],
        mode="markers",
        marker=dict(size=30, opacity=0.01),  # Slightly visible for better interactivity
        hoverinfo="text",
        text=[text],
        hoverlabel=dict(
            bgcolor=color,               # Set darker background color for overlaps
            font=dict(color='white')    # Set contrasting text color for readability
        ),
        showlegend=False
    ))

# Update layout for a clean and interactive look
fig.update_layout(
    title="Interactive Venn Diagram: Deterministic, Probabilistic, and Non-Probabilistic AI/ML Models",
    xaxis=dict(showgrid=False, zeroline=False, visible=False, range=[0, 1.2], scaleanchor="y", scaleratio=1),
    yaxis=dict(showgrid=False, zeroline=False, visible=False, range=[0, 1], scaleanchor="x", scaleratio=1),
    hovermode="closest",
    showlegend=False,
    width=1000,    # Increased width to accommodate legend
    height=900,    # Maintained height for consistency
    margin=dict(l=100, r=200, t=100, b=100)  # Increased right margin for legend
)

fig.show()
# Save the interactive Venn diagram as an HTML file
#interactive_venn_path = "/mnt/data/interactive_venn_ai_ml.html"
#fig.write_html(interactive_venn_path)

#print(f"Saved interactive Venn diagram to: {interactive_venn_path}")

