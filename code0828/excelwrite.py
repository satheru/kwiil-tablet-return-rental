import pandas as pd
import excelfind as ex
import log 



def bwrite( pcnumber , username):
    
    
    """
    대출한 것을 엑셀에 기록합니다

    Args:
        pcnumber (int) : pc번호
        username (str) : 이름
    Returns:
        아무것도 반환하지 않습니다.
    """
    
    
    #pcnumber 값이 옳지 않음
    if pcnumber == False:
        print("false")
              
    else:
        
        pcnumber = int(pcnumber)
        file_name = '현황.xlsx'
        # Daraframe형식으로 엑셀 파일 읽기
        df = pd.read_excel(file_name, sheet_name='현황')
        target_row = df.loc[df['태블릿'] == pcnumber]

        # 해당 행이 존재하는지 확인
        if not target_row.empty:
            # 선택된 태블릿 번호에 대해 대여자가 'none'인 경우 업데이트
            current_borrower = target_row['대여자'].values[0]

            if current_borrower == 'none':
                df.loc[df['태블릿'] == pcnumber, '대여자'] = username

                # 변경된 데이터프레임을 엑셀 파일에 저장
                with pd.ExcelWriter(file_name) as w:
                    df.to_excel(w, sheet_name='현황', index=False)
                
                log.log(pcnumber,"대출", username)
                    
            else:
                print(current_borrower + "님이 이미 excelwrite")
        else:
            print("해당 태블릿 번호를 찾을 수 없습니다.")
                
                

                
def rwrite( pcnumber , username):
    
    
    """
    반납한 것을 엑셀에 기록합니다

    Args:
        pcnumber (int) : pc번호
        username (str) : 이름
    Returns:
        아무것도 반환하지 않습니다.
    """
    
              
    if pcnumber == False:
        print("false")
        
    else:
        pcnumber = int(pcnumber)
        file_name = '현황.xlsx'
        # Daraframe형식으로 엑셀 파일 읽기
        df = pd.read_excel(file_name, sheet_name='현황')
        
        target_row = df.loc[df['태블릿'] == pcnumber]

        # 해당 행이 존재하는지 확인
        if not target_row.empty:
            # 선택된 태블릿 번호에 대해 대여자가 'none'이 아닌경우 경우 업데이트
            current_borrower = target_row['대여자'].values[0]

            if current_borrower == username:
                df.loc[df['태블릿'] == pcnumber, '대여자'] = 'none'

                # 변경된 데이터프레임을 엑셀 파일에 저장
                with pd.ExcelWriter(file_name) as w:
                    df.to_excel(w, sheet_name='현황', index=False)
                    
                log.log(pcnumber,"반납", username)
                    
            elif current_borrower == 'none':
                return False
                
            else:
                return False
                
        else:
            return False
                
                
def adminwrite( pcnumber , username):
    """
    엑셀의 pcnumber 항에 있는 이름을 username 으로 변경합니다
    (관리자용)
    
    Args:
        pcnumber (int) : pc번호
        username (str) : 이름
    Returns:
        아무것도 반환하지 않습니다.
    """

    pcnumber = int(pcnumber)
    file_name = '현황.xlsx'
    # Daraframe형식으로 엑셀 파일 읽기
    df = pd.read_excel(file_name, sheet_name='현황')
    target_row = df.loc[df['태블릿'] == pcnumber]

    # 해당 행이 존재하는지 확인
    if not target_row.empty:

        df.loc[df['태블릿'] == pcnumber, '대여자'] = username

        # 변경된 데이터프레임을 엑셀 파일에 저장
        with pd.ExcelWriter(file_name) as w:
            df.to_excel(w, sheet_name='현황', index=False)
        
        if username == "none":
            log.log(pcnumber,"관리자가 반납", username)
        else:
            log.log(pcnumber,"관리자가 대출", username)