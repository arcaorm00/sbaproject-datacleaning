import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from config import basedir
from util.file_helper import FileReader
from memberService import MemberService

class MemberController:
    def __init__(self):
        self.fileReader = FileReader()
        self.data = os.path.join(os.path.join(basedir, 'member'), 'data')
        self.service = MemberService()

    def modeling(self, data):
        service = self.service
        this = self.preprocessing(data)
        label = service.create_label(this)
        train = service.create_train(this)
        return this

    def preprocessing(self, data):
        service = self.service
        this = self.fileReader
        this.context = '/Users/saltQ/sbaproject-api/member/data/'
        this.train = service.new_model(data)
        print(f'feature 드롭 전 변수: \n{this.train.columns}')
        this = service.gender_nominal(this)
        print(f'성별 정제 후: \n{this.train.head()}')
        this = service.age_ordinal(this)
        print(f'나이 정제 후: \n{this.train.head()}')
        this = service.estimatedSalary_ordinal(this)
        print(f'수입 정제 후: \n{this.train.head()}')
        this = service.password_nominal(this)
        print(f'비밀번호 정제 후: \n{this.train["Password"]}')
        this = service.email_nominal(this)
        print(f'이메일 정제 후: \n{this.train["Email"]}')
        return this

    def learning(self):
        pass

    def submit(self):
        pass


if __name__ == '__main__':
    print(f'********** {basedir} **********')
    ctrl = MemberController()
    ctrl.modeling('member.csv')
    