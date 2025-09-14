import pandas as pd
from src.data_processing import load_data, split_data, scale_data, handle_imbalance
from src.models import get_classification_models
from src.evaluation import classification_metrics, plot_confusion_matrix
import joblib

def main():
    # Load data
    df = load_data("data/raw/your_data.csv")
    X = df.drop("target", axis=1)
    y = df["target"]

    # Train test split
    X_train, X_test, y_train, y_test = split_data(X, y)

    # Scale data
    X_train_scaled, X_test_scaled, scaler = scale_data(X_train, X_test)

    # Handle imbalance
    X_train_res, y_train_res = handle_imbalance(X_train_scaled, y_train, method="SMOTE")

    # Get models
    models = get_classification_models()

    results = []
    for name, model in models.items():
        model.fit(X_train_res, y_train_res)
        preds = model.predict(X_test_scaled)
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(X_test_scaled)
        else:
            proba = None
        metrics = classification_metrics(y_test, preds, proba)
        results.append((name, metrics))
        print(f"\n{name} Metrics:\n{metrics}")
        plot_confusion_matrix(y_test, preds)

    # Save scalers & models as needed
    joblib.dump(scaler, "models/scaler.joblib")
    # Example: joblib.dump(models["Random Forest"], "models/rf_model.joblib")

if __name__ == "__main__":
    main()
