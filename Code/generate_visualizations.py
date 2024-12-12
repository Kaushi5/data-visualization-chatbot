import os
import pandas as pd
import matplotlib.pyplot as plt

# Path for saving visualizations
VISUALIZATION_PATH = "visualizations"
os.makedirs(VISUALIZATION_PATH, exist_ok=True)


def generate_visualization(file_path, request):
    """
    Generates visualizations based on user requests.

    Args:
        file_path (str): Path to the uploaded dataset.
        request (str): Visualization request (e.g., "Bar Chart: X=index, Y=Sku").

    Returns:
        str: Path to the generated visualization image.
        str: High-level insight explaining the visualization.
    """
    try:
        # Read the dataset
        dataset = pd.read_excel(file_path, engine="openpyxl")

        # Parse visualization request
        request_lower = request.lower()
        if "bar chart" in request_lower:
            viz_type = "Bar"
        elif "line chart" in request_lower:
            viz_type = "Line"
        elif "scatter plot" in request_lower:
            viz_type = "Scatter"
        else:
            raise ValueError("Unsupported visualization type. Use Bar, Line, or Scatter.")

        # Extract X and Y columns
        x_col = request.split("X=")[1].split(",")[0].strip()
        y_col = request.split("Y=")[1].strip()

        # Generate the visualization
        plt.figure(figsize=(8, 6))
        if viz_type == "Bar":
            dataset.groupby(x_col)[y_col].sum().plot(kind="bar")
            plt.title(f"Bar Chart of {y_col} by {x_col}")
            insight = f"This bar chart shows how {y_col} is distributed across different {x_col} values."
        elif viz_type == "Line":
            dataset.plot(x=x_col, y=y_col, kind="line")
            plt.title(f"Line Chart of {y_col} over {x_col}")
            insight = f"This line chart displays the trend of {y_col} over {x_col}."
        elif viz_type == "Scatter":
            dataset.plot.scatter(x=x_col, y=y_col)
            plt.title(f"Scatter Plot of {y_col} vs {x_col}")
            insight = f"This scatter plot shows the relationship between {x_col} and {y_col}."

        # Save the visualization
        visualization_file = f"{viz_type}_{x_col}_vs_{y_col}.png"
        visualization_path = os.path.join(VISUALIZATION_PATH, visualization_file)
        plt.savefig(visualization_path)
        plt.close()

        return visualization_path, insight

    except KeyError as e:
        raise ValueError(f"Invalid column name in request: {e}")
    except Exception as e:
        raise Exception(f"Error generating visualization: {str(e)}")
