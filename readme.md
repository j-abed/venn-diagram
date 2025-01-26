 Interactive Venn Diagram

This project creates an interactive Venn diagram using Plotly to visualize the relationships between Deterministic, Probabilistic, and Non-Probabilistic AI/ML models. The diagram includes labeled sections for individual and overlapping categories, with hover text providing additional information.

## Modules

- `plotly.graph_objects`: Used to create the Venn diagram and add interactive elements.

## Variables

- `x_positions` (list): X-coordinates for the centers of the circles.
- `y_positions` (list): Y-coordinates for the centers of the circles.
- `sizes` (list): Sizes of the circles.
- `labels` (list): Labels for the individual and overlapping sections.
- `hover_texts` (list): Text to display when hovering over each section.
- `hover_positions` (list): Positions for the hover text.
- `hover_colors` (list): Background colors for the hover text.

## Usage

Run the script to display the interactive Venn diagram in a web browser. The diagram can also be saved as an HTML file by uncommenting the relevant lines at the end of the script.

```bash
python venn-diagram.py
```

## Instructions

Interact with the Venn diagram by hovering over the sections. The legend on the upper right corner indicates which of the three main circles represent which model type.

## License

This project is licensed under the MIT License.