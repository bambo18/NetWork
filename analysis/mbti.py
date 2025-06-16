# analysis/mbti.py

def analyze_mbti(responses):
    """
    responses: dict 형태
    예시: {'q1': 4, 'q2': 2, ..., 'q12': 5}
    """

    # 각 MBTI 지표에 해당하는 질문 번호
    ei_questions = ['q1', 'q5', 'q9']    # 외향 vs 내향
    sn_questions = ['q2', 'q6', 'q10']   # 감각 vs 직관
    tf_questions = ['q3', 'q7', 'q11']   # 사고 vs 감정
    jp_questions = ['q4', 'q8', 'q12']   # 판단 vs 인식

    def trait_score(question_list):
        return sum([int(responses.get(q, 3)) for q in question_list])  # 기본값 3 (중간)

    mbti = ""
    mbti += "E" if trait_score(ei_questions) >= 9 else "I"
    mbti += "S" if trait_score(sn_questions) >= 9 else "N"
    mbti += "T" if trait_score(tf_questions) >= 9 else "F"
    mbti += "J" if trait_score(jp_questions) >= 9 else "P"

    return mbti
