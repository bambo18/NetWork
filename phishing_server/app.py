# phishing_server/app.py

import os
import sys
import random
from flask import Flask, render_template, request

# 경로 설정
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analysis.mbti import analyze_mbti
from fake_analysis import generate_similar_mbti
from save_log import save_user_data  # 👉 아래에서 만들 예정

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../shared_templates'))
app = Flask(__name__, template_folder=template_dir)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    name = request.form.get("name")
    email = request.form.get("email")

    # 설문 응답 수집
    responses = {}
    for i in range(1, 13):
        q_key = f"q{i}"
        responses[q_key] = int(request.form.get(q_key, 3))

    real_mbti = analyze_mbti(responses)
    fake_mbti = generate_similar_mbti(real_mbti)

    # 👉 CSV 저장
    save_user_data(name, email, real_mbti, fake_mbti)

    return render_template("result.html", name=name, mbti=fake_mbti)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
