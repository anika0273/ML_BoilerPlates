import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE  # install imblearn package if needed

def load_data(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)

def split_data(X, y, test_size=0.2, random_state=42):
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=random_state)

def scale_data(X_train, X_test, scaler=None):
    if scaler is None:
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
    else:
        X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler

def handle_imbalance(X_train, y_train, method="SMOTE"):
    if method == "SMOTE":
        sm = SMOTE(random_state=42)
        X_res, y_res = sm.fit_resample(X_train, y_train)
        return X_res, y_res
    # Can add class weights or other methods here
    return X_train, y_train
