import os
from datetime import datetime
import pandas as pd


def log(number, status, name):
    
    
    """
    number , status , name 값을 월에 맞는 텍스트 파일에 기록합니다

    Args:
        number (int) : pc번호
        status (str) : 행동
        name (str) : 이름
        

    Returns:
        nothing XD
    """
    
    #log 파일이 없다면 생성합니다
    if not os.path.exists('log'):
        os.makedirs('log')


    # 현재 날짜를 YYYY-MM-DD 형식의 문자열로 얻기
    date_str = datetime.now().strftime('%y-%m-%d-%H-%M-%S')
    
    #년-월만 따로 추출
    date_year = datetime.now().strftime('%y-%m')
    
    #월에 맞는 텍스트 파일 생성
    filename = os.path.join('log', f'log_{date_year}.txt')
    
    # 텍스트 파일에 값을 기록하는 함수
    with open(filename, 'a') as file: #'a'는 추가
        #파일에 작성
        file.write(f"날짜: {date_str}, 상태: {status}, 사용자: {name}, 태블릿: {number}\n")       
    


