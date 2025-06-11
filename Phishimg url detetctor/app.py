from flask import Flask, request, render_template, jsonify, session, redirect, url_for
import joblib
from extract_features import extract_features

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

# Mock user database (in a real app, use a proper database)
users = {
    'admin': {'password': 'admin123', 'name': 'Admin User'}
}

model = joblib.load("phishing_model.pkl")

@app.route("/")
def home():
    if 'username' in session:
        return render_template("index.html", username=session['username'])
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('home'))
        return render_template("login.html")
    
    # Handle POST request
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    # Check credentials (in a real app, use proper password hashing)
    if username in users and users[username]['password'] == password:
        session['username'] = username
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'Invalid username or password'}), 401

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route("/predict", methods=["POST"])
def predict():
    if 'username' not in session:
        return jsonify({"error": "Unauthorized"}), 401
        
    url = request.form.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    features = extract_features(url)
    input_data = [list(features.values())]
    prediction = model.predict(input_data)[0]
    result = "Phishing" if prediction == 1 else "Legitimate"
    
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)