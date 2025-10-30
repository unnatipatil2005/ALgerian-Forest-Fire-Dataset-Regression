🌲 Algerian Forest Fire Dataset — Regression Project
📌 Overview

This project predicts the Fire Weather Index (FWI) using multiple environmental features such as temperature, humidity, wind speed, and more.
It uses Ridge Regression for predictive modeling and a Flask web app for interactive user input and result visualization.

🧠 Problem Statement

Wildfires can cause massive environmental and economic damage.
The goal of this project is to predict the FWI — a metric representing the potential for forest fire — based on meteorological data from the Algerian Forest Fire dataset.

⚙️ Tech Stack

Python 3

Flask (for web framework)

Scikit-learn (for regression and scaling)

HTML/CSS (for frontend interface)

Pickle (for model serialization)

NumPy & Pandas (for data processing)

🧩 Project Structure
📁 Algerian-Forest-Fire-Dataset-Regression
│
├── app.py                     # Flask application
├── models/
│   ├── ridge.pkl              # Trained Ridge Regression model
│   └── scaler.pkl             # StandardScaler object
│
├── templates/
│   ├── home.html              # Web form for user input
│   └── index.html             # Landing page
│
├── static/                    # (optional) CSS/JS files
│
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies

🚀 How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/unnatipatil2005/ALgerian-Forest-Fire-Dataset-Regression.git
cd ALgerian-Forest-Fire-Dataset-Regression

2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate     # (Windows)
# or
source venv/bin/activate  # (Mac/Linux)

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the Flask app
python app.py


Then open your browser and go to:
👉 http://127.0.0.1:5000

🧪 Model Details

Algorithm: Ridge Regression

Evaluation Metrics: R² Score, MAE, MSE

Preprocessing: Standard Scaling applied to all numeric features

🖼️ Web App Interface

The app provides a simple and clean interface to input the following features:

Feature	Description
Temperature	Ambient temperature (°C)
RH	Relative Humidity (%)
WS	Wind Speed (km/h)
Rain	Rainfall (mm/m²)
FFMC	Fine Fuel Moisture Code
DMC	Duff Moisture Code
ISI	Initial Spread Index
Classes	Fire or No Fire indicator
Region	Region code (Bejaia or Sidi-Bel-Abbes)

After entering these values and clicking Predict, the model displays the predicted FWI value.

📊 Example Output

Input:

Temperature = 25°C
RH = 45%
WS = 15 km/h
Rain = 0.0 mm/m²
FFMC = 85
DMC = 75
ISI = 10
Classes = 1
Region = 1


Predicted Output:

Predicted Fire Weather Index (FWI): 23.48

👩‍💻 Author

Unnati Patil
📧 [your-email@example.com
]
🌐 GitHub Profile

⭐ Acknowledgements

Dataset sourced from the UCI Machine Learning Repository
.
Special thanks to the open-source community for enabling accessible AI research and tools.