# ❤️ Heart Disease Prediction

This project predicts the likelihood of heart disease based on patient health data using **Machine Learning**.  
It provides a user-friendly interface where users can input various health parameters and get a prediction result instantly.

---

## 🚀 Features
- Machine Learning-based heart disease prediction  
- Frontend built with HTML/CSS  
- Backend powered by Python (Flask/Django — specify which one you used)  
- Database managed using **XAMPP (MySQL)**  
- Interactive web interface  
- Easy to deploy and customize  

---

## 🧠 Tech Stack
- **Frontend:** HTML, CSS  
- **Backend:** Python (Flask/Django)  
- **Database:** MySQL (via XAMPP)  
- **Libraries Used:**
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `joblib`
  - `flask` (if used)
  - `mysql.connector` (if used)

---

## ⚙️ Installation and Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/rayamgari-supriya/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
2️⃣ Set up your environment
Make sure you have Python installed. Then install the required libraries:

bash
Copy code
pip install -r requirements.txt
(If you don’t have a requirements.txt file, install manually:)

bash
Copy code
pip install pandas numpy scikit-learn flask mysql-connector-python joblib
3️⃣ Start XAMPP
Open XAMPP Control Panel

Start Apache and MySQL

Create a database (e.g., heart_disease_db) in phpMyAdmin

Import your SQL file if available

4️⃣ Run the application
In your project folder:

bash
Copy code
python app.py
or (if using Django):

bash
Copy code
python manage.py runserver
Then open your browser and go to:

cpp
Copy code
http://localhost:5000/     (for Flask)
or
http://127.0.0.1:8000/     (for Django)
📊 Machine Learning Model
The model was trained using the Heart Disease UCI dataset

Algorithm used: Logistic Regression / Random Forest / Naive Bayes (whichever you used)

Data was preprocessed and scaled before training

Model saved using joblib

👩‍💻 Author
Rayamgari Supriya
B.Tech Student | Aspiring Data Scientist & Developer
📧 rayamgarisupriya@gmail.com