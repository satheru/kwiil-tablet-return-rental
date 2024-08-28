#pip install xlrd
#pip install openpyxl
#pip install pandas
#설치하고 진행함.

import pandas as pd

def namefind(value):
    """
    엑셀(명부.xlsx)에서 value를 찾기

    Args:
        value (str) : 찾을값

    Returns:
        True or False
    """
    
    
    
    # 엑셀 파일 경로 설정
    excel_file_path = '명부.xlsx'
    
    # '목록'만 불러오기
    df = pd.read_excel(excel_file_path, sheet_name='목록')
    
    # '목록'에서 값을 찾았는지 여부를 확인
    found = (df == value).any().any()

    return found




def laptopsfind(name):
    """
    이름에 귀속된 모든 노트북 번호를 추출

    Args:
        name (str) : 이름

    Returns:
        이름에 귀속된 모든 노트북 번호를 문자열 형식으로 반환
    """
    
    
    
    # 엑셀 파일 경로 설정
    excel_file_path = '현황.xlsx'
    
    # '현황' 시트만 읽기
    df = pd.read_excel(excel_file_path, sheet_name='현황')
    
    # '대여자' 열에서 특정 대여자(name)만 필터링
    filtered_df = df[df['대여자'] == name]
    
    # 조건에 맞는 태블릿 번호를 추출
    laptop_numbers = filtered_df['태블릿'].tolist()
    
    return laptop_numbers



def barcodefind(username,barcode,todo):
    """
    바코드를 받아서 노트북 번호로 추출

    아무도 대출하지 않았는지 = 대출
    내가 대출한 것인지 = 반납
    에서 확인 ( todo )
    
    Args:
        username (str) : 이름
        barcode (str) : 바코드
        todo (str) : b or r (대출 or 반납)

    Returns:
        바코드 번호에 맞는 노트북 번호를 반환
    """

    excel_file_path = '현황.xlsx'
    
    # '현황' 시트만 읽기
    df = pd.read_excel(excel_file_path, sheet_name='현황')
    
    filtered_df = df[df['바코드'] == barcode]
    
    # 태블릿번호 정보 추출
    
    if todo == "b":
        if not filtered_df.empty:
            # 사용자 값이 "none"인지 확인
            if filtered_df['대여자'].values[0] == "none":
                renter = filtered_df['태블릿'].values[0]
                renter = int(renter)
                return renter
            
            else:
                return False

        else:
            return "error1"
        
    elif todo == "r":
        if not filtered_df.empty:
            # 사용자 값이 맞는지 확인
            if filtered_df['대여자'].values[0] == username:
                renter = filtered_df['태블릿'].values[0]
                renter = int(renter)
                return renter
            
            else:
                return False

        else:
            return "error2"
        
        
def adminbarcode(barcode):
    """
    바코드에 맞는 노트북 번호를 출력
    (관리자용 , 누구에게 귀속되든 확인할수 있음)

    Args:
        barcode (str) : 바코드

    Returns:
        바코드에 맞는 노트북 번호를 반환
    """

    excel_file_path = '현황.xlsx'
    
    # '현황' 시트만 읽기
    df = pd.read_excel(excel_file_path, sheet_name='현황')
    
    filtered_df = df[df['바코드'] == barcode]
    
    if not filtered_df.empty:
        renter = filtered_df['태블릿'].values[0]
        renter = int(renter)
        return renter
            
    else:
        return False




    