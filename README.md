# 🌊 Flood Prediction Using Machine Learning

## 📌 Project Overview

The Flood Prediction System is a Machine Learning-based web application that predicts the likelihood of flood occurrence using environmental and rainfall-related parameters.

The project follows a structured Machine Learning workflow, starting from data collection and preprocessing to model training, evaluation, deployment, and web application development using Flask.

The application allows users to enter weather and rainfall information through a web interface and instantly predicts whether flooding is likely to occur.

---

# 🎯 Objective

The objective of this project is to develop an intelligent flood prediction system that can assist in identifying flood-prone conditions based on historical environmental data.

---

# 🛠 Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle
- Flask
- HTML
- CSS

---

# 📂 Project Structure

```
Flood_Prediction_Project/
│
├── Dataset/
│   └── flood.xlsx
│
├── models/
│   ├── flood_prediction.pkl
│   └── scaler.pkl
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── Flood_Prediction.ipynb
├── app.py
├── requirements.txt
└── README.md
```

---

# 🚀 Workflow

The project is developed through multiple epics covering the complete Machine Learning lifecycle.

---

# Epic 1: Environment Setup and Package Installation

### Story 1

Installed all required Python libraries including:

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Pickle
- Flask
- OpenPyXL

### Story 2

Created the project folder structure including:

- Dataset
- Models
- Templates
- Static
- Notebook
- Flask Application

---

# Epic 2: Importing Required Libraries

### Story 1

Imported all required libraries for:

- Data Analysis
- Data Visualization
- Machine Learning
- Model Serialization
- Flask Web Application

---

# Epic 3: Dataset Download and Understanding

### Story 1

Downloaded the Flood Prediction dataset.

### Story 2

Loaded the dataset into Pandas DataFrame.

### Story 3

Explored:

- Dataset Shape
- Data Types
- Feature Names
- Missing Values
- Statistical Summary

### Story 4

Visualized data using:

- Heatmap
- Histogram
- Correlation Matrix
- Distribution Plots

---

# Epic 4: Data Preprocessing

### Story 1

Selected Independent Variables (Features)

- Temperature
- Humidity
- Cloud Cover
- Annual Rainfall
- Jan-Feb Rainfall
- Mar-May Rainfall
- Jun-Sep Rainfall
- Oct-Dec Rainfall
- Average June Rainfall
- Subdivision

### Story 2

Selected Dependent Variable

- Flood

### Story 3

Handled Missing Values

### Story 4

Performed Label Encoding for categorical columns.

### Story 5

Scaled numerical data using StandardScaler.

---

# Epic 5: Train-Test Split

### Story 1

Split the dataset into:

- Training Data (80%)
- Testing Data (20%)

using train_test_split().

---

# Epic 6: Model Development

### Story 1

Trained multiple Machine Learning models:

- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost

### Story 2

Generated predictions using each model.

### Story 3

Compared model performance using Accuracy Score.

### Story 4

Selected the best-performing model for deployment.

---

# Epic 7: Saving the Model

### Story 1

Serialized the trained model using Pickle.

### Story 2

Saved:

- flood_prediction.pkl
- scaler.pkl

inside the models folder.

---

# Epic 8: Flask Web Application

### Story 1

Developed Flask backend.

### Story 2

Created HTML pages:

- Home Page
- Prediction Result Page

### Story 3

Integrated trained model with Flask.

### Story 4

Accepted user inputs.

### Story 5

Preprocessed inputs using the saved scaler.

### Story 6

Generated prediction using the trained model.

### Story 7

Displayed prediction result on the webpage.

---

# 📊 Machine Learning Models Used

- Decision Tree Classifier
- Random Forest Classifier
- K-Nearest Neighbors
- XGBoost Classifier

---

# 📈 Model Performance

The trained models were evaluated using Accuracy Score.

Example Results:

| Model | Accuracy |
|--------|----------|
| Decision Tree | 100% |
| Random Forest | 100% |
| KNN | 91.3% |
| XGBoost | 100% |

The best-performing model was selected and deployed.

---

# 🌐 Web Application Features

- User-friendly interface
- Input flood-related environmental parameters
- Predict flood occurrence instantly
- Fast prediction using the trained model
- Responsive design

---

# ▶️ How to Run the Project

## Step 1

Install required libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn flask openpyxl xgboost
```

## Step 2

Run the Flask application

```bash
python app.py
```

## Step 3

Open your browser

```
http://127.0.0.1:5000
```

---

# 📷 Project Output

- Home Page
- User Input Form
- Flood Prediction Result
- No Flood Prediction Result

---

# 📚 Future Enhancements

- Real-time weather API integration
- Interactive dashboard
- GIS map visualization
- SMS/Email flood alerts
- Cloud deployment
- Mobile application

---

# 👨‍💻 Author

**Karthik**

Machine Learning Project developed using Python, Scikit-learn, and Flask.