
### 🧩 **src/preprocessing.py**
```python
import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_json(file_path)
    df = df.drop_duplicates()
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')
    df['hour'] = df['timestamp'].dt.hour + 1
    return df
