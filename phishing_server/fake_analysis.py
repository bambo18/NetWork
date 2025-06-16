# phishing_server/fake_analysis.py

import random

def generate_similar_mbti(real_mbti):
    """
    real_mbti: 문자열 (예: 'INTP')
    returns: 비슷해 보이지만 조작된 MBTI
    """
    mbti_options = {
        0: ['E', 'I'],
        1: ['S', 'N'],
        2: ['T', 'F'],
        3: ['J', 'P'],
    }

    # 1~2자리 무작위로 바꿈
    real_list = list(real_mbti)
    positions_to_change = random.sample([0, 1, 2, 3], k=random.choice([1, 2]))
    
    for pos in positions_to_change:
        original = real_list[pos]
        options = [c for c in mbti_options[pos] if c != original]
        real_list[pos] = random.choice(options)

    return ''.join(real_list)
