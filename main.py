from src.preprocessing import load_and_clean_data
from src.visualization import plot_coordinates
from src.heatmap_generator import create_heatmap
from src.model_training import train_models

import pandas as pd

if __name__ == "__main__":
    df = load_and_clean_data("data/sample_data.json")
    plot_coordinates(df)

    # Example features (adjust based on actual dataset)
    X = df[["latitude", "longitude", "hour"]]
    y = df["health_status"]  # assumed column
    
    results = train_models(X, y)
    for model, report in results.items():
        print(f"\n=== {model} ===")
        print(f"Accuracy: {report['accuracy']:.2f}")

    m = create_heatmap(df)
    m.save("contact_tracing_heatmap.html")
