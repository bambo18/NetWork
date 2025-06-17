# normal_server/app.py

import os
import sys

# 🔧 상위 폴더(mbti_phishing_project)를 모듈 경로에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request
from analysis.mbti import analyze_mbti

# shared_templates 경로 지정
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../shared_templates'))

app = Flask(__name__, template_folder=template_dir)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    name = request.form.get("name")
    email = request.form.get("email")

    # 설문 응답 수집 (q1 ~ q12)
    responses = {}
    for i in range(1, 13):
        q_key = f"q{i}"
        responses[q_key] = int(request.form.get(q_key, 3))  # 응답 없으면 중간값 3

    # MBTI 분석
    mbti_result = analyze_mbti(responses)

    return render_template("result.html", name=name, mbti=mbti_result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)