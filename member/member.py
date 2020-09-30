import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from util.file_helper import FileReader
from config import basedir

# RowNumber,        레코드 행 번호
# CustomerId,       고객 ID     ==> 문제
# Surname,          고객 last name
# CreditScore,      신용점수
# Geography,        지역
# Gender,           성별
# Age,              나이
# Tenure,           존속 기간
# Balance,          잔액
# NumOfProducts,    구매 물품 수
# HasCrCard,        신용카드 여부
# IsActiveMember,   활성 고객 여부
# EstimatedSalary,  급여 수준
# Exited            서비스 탈퇴 여부    ==> 답

class MemberService:
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.join(basedir, 'member'), 'data')

    