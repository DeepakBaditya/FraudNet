FraudNet is a machine learning-powered job fraud detection system designed to identify fraudulent job postings with high accuracy. The tool leverages NLP (Natural Language Processing) techniques to analyze job descriptions, requirements, and benefits, and flags suspicious listings in real-time.

## 🚀 How to Run

### 🧠 Option 1: Run in GitHub Codespaces

1. Click **`Code`** → **`Codespaces`** → **`New codespace`**
2. Once it's ready, run this in the terminal:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

### 💻 Option 2: Run Locally

#### 1. Clone the repository

```bash
git clone https://github.com/DeepakBaditya/FraudNet.git
cd FraudNet
```

#### 2. Install the dependencies

```bash
pip install -r requirements.txt
```

#### 3. Launch the Streamlit app

```bash
streamlit run app.py
```

---

## 📂 requirements.txt

```txt
streamlit
pandas
scikit-learn
xgboost
joblib
```

---

## 🧪 Example Output

You’ll get predictions like:

- ✅ Genuine  
- ❌ Fraudulent

### 📝 What It Does
- Upload a .csv file with job data

- The model detects whether each job post is Fraudulent or Genuine

- Simple and easy-to-use interface