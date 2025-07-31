# 📊 Assignment 1: Extracting Feature Matrix from Weather Data

This assignment guides you through the process of extracting a numerical feature matrix from raw weather data in CSV format. The resulting matrix is suitable for downstream machine learning tasks such as classification or regression.

---

## 🧩 Objective

Implement a Python function that loads and processes weather observation data from a CSV file and returns a NumPy array containing:

- **Year**
- **Month**
- **Day**
- **Hour**
- **Minute**
- **Minimum temperature (°C)**
- **Maximum temperature (°C)**

Missing values (represented as `-` in the CSV file) should be replaced with `0.0` in the final matrix.

---

## 📂 File Structure

```
assignment-1/
├── data/
│   └── assignment_1.csv          # Raw input data
├── src/
│   └── data_gathering.py         # Your implementation goes here
├── tests/
│   └── test_train_model.py       # Test script for verifying correctness
└── README.md                     # This file
```

---

## 🧠 Your Task

Implement the function `load_feature_matrix(filepath: str) -> np.ndarray` in `src/data_gathering.py`.

### Example Signature

```python
import numpy as np
import pandas as pd

def load_feature_matrix(filepath: str) -> np.ndarray:
    ...
```

This function should:
- Load the CSV file using `pandas.read_csv`, treating `"-"` as missing values.
- Parse the date and time fields into structured components.
- Replace any missing values with `0.0`.
- Return a NumPy array with shape `(n_samples, 7)`.

---

## 📎 Sample CSV Format

```csv
"Year","Month","Day","Time [Local time]","Minimum temperature [°C]","Maximum temperature [°C]"
2025,2,23,02:00,-0.6,2
2025,2,24,08:00,-,-
```

---

## ▶️ Example Usage

You can run the script manually:

```bash
$ python src/data_gathering.py
```

This will load the data from `data/assignment_1.csv`, process it, and print the resulting feature matrix.

---

## ✅ Expected Output

```python
[[2025.     2.    23.     2.     0.    -0.6     2. ]
 [2025.     2.    24.     8.     0.     0.      0. ]]
```

---

## 🧪 Running the Tests

To verify your implementation, run the provided unit test:

```bash
PYTHONPATH=. pytest
```

The test checks:
- The correct number of rows and columns
- That missing values were replaced
- That the date and time were parsed correctly

---

## 🔐 Notes

- Do **not** hardcode the file path in your function. It should work with any valid CSV passed via the `filepath` argument.
- Make sure to commit only `.py` files and **not** any large datasets.

---

## 🙋‍♂️ Questions?

Contact your instructor or teaching assistant via the course Slack channel or email.

Good luck!
