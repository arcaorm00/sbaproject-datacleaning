import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import basedir
from util.file_helper import FileReader
import pandas as pd
import numpy as np
import uuid

# RowNumber,        레코드 행 번호
# CustomerId,       고객 ID
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
# Exited            서비스 탈퇴 여부

class MemberService:
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.join(basedir, 'member'), 'data')

    def new_model(self, payload) -> object:
        this = self.fileReader
        this.data = self.data
        this.fname = payload
        print(f'*****{this.context + this.fname}')
        return pd.read_csv(os.path.join(self.data, this.fname))

    @staticmethod
    def create_train(this):
        return this.train.drop('Exited', axis=1)

    @staticmethod
    def create_label(this):
        return this.train['Exited']

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis=1)
        return this

    @staticmethod
    def surname_nominal(this):
        return this

    @staticmethod
    def creditScore_ordinal(this):
        return this

    @staticmethod
    def geography_nominal(this):
        return this

    @staticmethod
    def gender_nominal(this):
        gender_mapping = {'Male': 0, 'Female': 1}
        this.train['Gender'] = this.train['Gender'].map(gender_mapping)
        this.train = this.train
        return this

    @staticmethod
    def age_ordinal(this):
        train = this.train
        train['Age'] = train['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] # 범위
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'YoungAdult', 'Adult', 'Senior']
        train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        age_title_mapping = {
            0: 'Unknown',
            1: 'Baby', 
            2: 'Child',
            3: 'Teenager',
            4: 'Student',
            5: 'YoungAdult',
            6: 'Adult',
            7: 'Senior'
        }

        for x in range(len(train['AgeGroup'])):
            if train['AgeGroup'][x] == 'Unknown':
                train['AgeGroup'][x] = age_title_mapping[train['Title'][x]]
        
        age_mapping = {
            'Unknown': 0,
            'Baby': 1, 
            'Child': 2,
            'Teenager': 3,
            'Student': 4,
            'YoungAdult': 5,
            'Adult': 6,
            'Senior': 7
        }
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        this.train = train
        return this

    @staticmethod
    def tenure_ordinal(this):
        return this

    @staticmethod
    def balance_ordinal(this):
        return this

    @staticmethod
    def numOfProducts_ordinal(this):
        return this

    @staticmethod
    def hasCrCard_numeric(this):
        return this

    @staticmethod
    def isActiveMember_numeric(this):
        return this

    @staticmethod
    def estimatedSalary_ordinal(this):
        this.train['EstimatedSalary'] = pd.qcut(this.train['EstimatedSalary'], 4, labels={1, 2, 3, 4})
        return this

    # 비밀번호 추가 (임시 1234 통일)
    @staticmethod
    def password_nominal(this):
        this.train['Password'] = '1234'
        return this

    # 이메일 추가 (임시 uuid_CustomerId@gmail.com)
    @staticmethod
    def email_nominal(this):
        this.train['Email'] = ''
        for idx in range(len(this.train)):
            this.train.loc[idx,'Email'] = str(uuid.uuid1()).split('-')[3] + '_' + str(this.train.loc[idx,'CustomerId']) + '@gmail.com'
        return this