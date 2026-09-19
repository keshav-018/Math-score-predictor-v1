# 📊 Math Score Predictor

An end-to-end machine learning project that predicts a student's **math score** based on demographic and academic factors — gender, ethnicity, parental level of education, lunch/food type, test preparation course, and reading & writing scores.

The project isn't just a single model — it runs multiple regression algorithms through **GridSearchCV**, compares them on **R² score**, and automatically selects and saves the best-performing model for inference.

---

## 🔗 Live Project

- **GitHub Repo:** [Math-score-predictor-v1](https://github.com/keshav-018/Math-score-predictor-v1)
- **Docker Image:** *(coming soon)*

---

## 🚀 Features

- **End-to-end ML pipeline** — from raw data to a deployed prediction web app
- **Modular pipeline design** — separate, reusable `Training Pipeline` and `Predict Pipeline`
- **Automated model selection** — trains several regression models, tunes them with `GridSearchCV`, and picks the one with the best R² score
- **Custom exception handling & logging** for easier debugging
- **Preprocessing pipeline** (encoding, scaling) saved as an artifact and reused at inference time
- **Flask web front end** to input student details and get an instant score prediction
- **Installable as a package** via `setup.py`
- **Dockerized** for consistent deployment across environments
- Deployment-ready config for **AWS Elastic Beanstalk** (`.ebextensions`)

---

## 🧠 How It Works

1. **Data Ingestion** — Reads the raw student dataset and splits it into train/test sets.
2. **Data Transformation** — Applies preprocessing (imputation, scaling, one-hot encoding) via a `ColumnTransformer` and saves the fitted preprocessor as an artifact (`preprocessor.pkl`).
3. **Model Training** — Trains multiple regression models (e.g. Linear Regression, Ridge, Lasso, Decision Tree, Random Forest, Gradient Boosting, AdaBoost, XGBoost, CatBoost), tunes hyperparameters with `GridSearchCV`, evaluates each on R² score, and saves the **best model** as `model.pkl`.
4. **Prediction Pipeline** — Loads the saved preprocessor + model and transforms new input data to return a math score prediction.
5. **Web App** — A Flask front end collects the input features and displays the predicted score.

---

## 🗂️ Project Structure

```
Math-score-predictor-v1/
│
├── .ebextensions/          # AWS Elastic Beanstalk deployment config
├── artifacts/               # Saved model, preprocessor, and processed datasets
├── catboost_info/           # Auto-generated CatBoost training logs
├── notebook/
│   └── data/                 # Raw dataset & EDA / model-experimentation notebooks
├── src/
│   ├── components/           # Data ingestion, transformation & model trainer
│   ├── pipeline/              # train_pipeline.py & predict_pipeline.py
│   ├── exception.py           # Custom exception handling
│   ├── logger.py              # Logging configuration
│   └── utils.py                # Shared utility functions (save/load objects, model evaluation)
├── templates/                # HTML templates for the Flask front end
├── app.py                     # Flask application entry point
├── application.py             # WSGI entry point (used for AWS Elastic Beanstalk)
├── Dockerfile                 # Docker build configuration
├── requirements.txt           # Python dependencies
├── setup.py                    # Makes the project pip-installable
└── README.md
```

> Note: adjust the tree above if your actual folder/file names differ slightly.

---

## 🎯 Input Features

| Feature | Description |
|---|---|
| Gender | Student's gender |
| Race/Ethnicity | Group category |
| Parental Level of Education | Highest education level of parent(s) |
| Lunch | Standard or free/reduced lunch (food type) |
| Test Preparation Course | Completed or not |
| Reading Score | Score out of 100 |
| Writing Score | Score out of 100 |

**Target variable:** Math Score

---

## 🛠️ Tech Stack

- **Language:** Python
- **ML/Data:** scikit-learn, pandas, numpy, CatBoost, XGBoost
- **Model Selection:** GridSearchCV
- **Web Framework:** Flask
- **Deployment:** Docker, AWS Elastic Beanstalk
- **Packaging:** setup.py

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/keshav-018/Math-score-predictor-v1.git
cd Math-score-predictor-v1
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the training pipeline (optional — a trained model is already included in `artifacts/`)
```bash
python src/pipeline/train_pipeline.py
```

### 5. Run the web app
```bash
python app.py
```
Then open `http://127.0.0.1:5000` in your browser.

---

## 🐳 Running with Docker

Build the image:
```bash
docker build -t math-score-predictor .
```

Run the container:
```bash
docker run -p 5000:5000 math-score-predictor
```

Then visit `http://localhost:5000`.

---

## 📈 Model Evaluation

Multiple regression models are trained and tuned using `GridSearchCV`. Each model's **R² score** on the test set is compared, and the model with the highest score is automatically selected and persisted as the final prediction model.

| Step | Description |
|---|---|
| Models trained | Linear Regression, Ridge, Lasso, Decision Tree, Random Forest, Gradient Boosting, AdaBoost, XGBoost, CatBoost *(update to match your actual list)* |
| Selection metric | R² Score |
| Output | Best model saved to `artifacts/model.pkl` |

---

## 📌 Future Improvements

- Add CI/CD pipeline for automated retraining and deployment
- Add unit tests for pipeline components
- Log experiments with MLflow
- Add more granular feature engineering

---

## 🙌 Acknowledgements

This was built as a learning project to strengthen end-to-end ML engineering skills — covering data pipelines, model experimentation, packaging, and deployment.

---

## 📬 Contact

**Keshav** — [GitHub: keshav-018](https://github.com/keshav-018)

If you find this project useful, consider giving it a ⭐ on GitHub!