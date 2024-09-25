from flask import Flask, request, jsonify, render_template
from model.recommendation import RecommendationSystem

app = Flask(__name__)
model = RecommendationSystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = request.form.get('user_id')
    recommendations = model.get_recommendations(user_id)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
