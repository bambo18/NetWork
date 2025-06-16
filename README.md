# MBTI Phishing Simulation Project - 13조

Flask 기반 정상/피싱 서버 구현을 통해 사용자의 개인정보 입력 및 결과 조작 흐름을 시뮬레이션하는 프로젝트입니다.

---

## 팀원

| 이름     | 역할                                                        |
|----------|-------------------------------------------------------------|
| 설재우   | Flask 서버 구현, 결과 반환 처리                            |
| 최선호   | 설문/개인정보 입력 UI 설계, MBTI 분석 알고리즘 구현       |
| 표형돈   | Wireshark 패킷 캡처 및 분석, 보고서 및 발표자료 작성      |

---

## 시나리오 요약

1. 사용자는 MBTI 검사 페이지에 접속한다 (`normal_server` 또는 `phishing_server`)
2. 이름, 이메일, 설문 항목을 입력한다
3. `phishing_server`는 조작된 MBTI 결과를 반환하고, 사용자의 정보를 `log.csv`에 저장한다
4. 정상 서버와의 결과 차이를 통해 피싱 위협을 인식하는 교육적 효과를 기대한다

---

## 실행 방법

### 정상 서버 실행

```bash
cd normal_server
python app.py
# 접속: http://localhost:5000
### 피싱 서버 실행
cd phishing_server
python app.py
# 접속: http://localhost:5001
