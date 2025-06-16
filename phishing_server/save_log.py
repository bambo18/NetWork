# phishing_server/save_log.py

import csv
import os
from datetime import datetime

def save_user_data(name, email, real_mbti, fake_mbti):
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'log.csv')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            name,
            email,
            real_mbti,
            fake_mbti
        ])
