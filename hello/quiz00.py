from hello.domains import myRandom, memberlist
import random

class Quiz00:
    def quiz00calculator(self):
        a = myRandom(1, 100)
        b = myRandom(1, 100)
        o = ['*', '-', '*', '/', '%']
        o2 = o[myRandom(0, 5)]
        if o2 == '+':
            s = f'{a}+{b}={a + b}'
        elif o2 == '-':
            s = f'{a}-{b}={a - b}'
        elif o2 == '*':
            s = f'{a}*{b}={a * b}'
        elif o2 == '/':
            s = f'{a}/{b}={a / b}'
        elif o2 == '%':
            s = f'{a}%{b}={a / b}'
        print(s)
        return None

    def quiz01bmi(self):
        h = myRandom(50, 200)
        w = myRandom(1, 200)
        bmires = w / (h * h) * 10000

        if bmires > 25:
            res = '비만'
        elif bmires > 23:
            res = '과체중'
        elif bmires > 18.5:
            res = '정상'
        else:
            res = '저체중'
        print(f'{bmires} {res}')

    def quiz02dice(self):
        print(myRandom(1, 6))

    def quiz03rps(self):
        p = myRandom(0, 2)
        c = myRandom(0, 2)
        rps = ['가위', '바위', '보']
        r = p - c
        if r == 0:
            res = f'플레이어: {rps[p]} ㅣ 컴퓨터: {rps[c]} ☞ 무승부'
        elif r == -1 or r == 2:
            res = f'플레이어: {rps[p]} ㅣ 컴퓨터: {rps[c]} ☞ 패배'
        elif r == 1 or r == -2:
            res = f'플레이어: {rps[p]} ㅣ 컴퓨터: {rps[c]} ☞ 승리'
        print(f'{res}')

    def quiz04leap(self):
        year = myRandom(2000, 2022)
        s1 = "윤년" if year % 4 == 0 and year % 100 != 0 else "평년"
        s2 = "윤년" if year % 400 == 0 else "평년"
        res = "윤년" if s2 or s1 else "평년"
        print(f"{year}년도는 {res}입니다.")

    def quiz05grade(self):
        name = memberlist()
        kor = myRandom(2, 100)
        eng = myRandom(2, 100)
        math = myRandom(2, 100)
        sum = kor + eng + math
        avg = int(sum / 3)
        grade = ['A', 'B', 'C', 'D', 'E', 'F']
        if avg == 100:
            g_index = 0
        elif avg < 100 and avg > 40:
            g_index = int((99 - avg) / 10)
        else:
            g_index = 5

        if avg >= 60:
            res = '합격'
        else:
            res = '불합격'
        print(f'{name}님의 점수 → 국어:{kor} 영어:{eng} 수학:{math} 평균:{avg:.2f} 학점:{grade[g_index]} 합격여부:{res}')
        ## 하나로 출력하는거 고민해 보기

    @staticmethod
    def quiz06memberChoice():
        return memberlist()[myRandom(0,23)]

    # 1. 1~45번 중 6개를 중복없이 뽑아야 한다.
    # 2. 6개를 뽑고 보너스 번호를 하나 더 뽑는다.
    # 3. 처음 뽑은 번호 6개가 일치하면 1등
    def quiz07lotto(self):
        lottonum = random.sample(range(1, 46), 7)
        mynum = random.sample(range(1, 46), 6)
        c = 0

        for i in lottonum[:6]:
            for k in mynum:
                if i == k:
                    c += 1
        if c == 6:
            res = f'★일등★ {c}개 번호 동일 \t'
        elif c == 5:
            b_c = 0
            for i in mynum:
                if lottonum[6] == i:
                    b_c = 1
                    break
            if b_c == 1:
                res = f'★이등★ {c}개 번호 동일 \t'
            else:
                res = f'★삼등★ {c}개 번호 동일 \t'
        elif c == 4:
            res = f'★사등★ {c}개 번호 동일 \t'
        elif c == 3:
            res = f'★오등★ {c}개 번호 동일 \t'
        else:
            res = f'★꽝★ {c}개 번호 동일'
        print(f'오늘의 로또 번호:{mynum}\n나의 로또 번호:{lottonum}\n로또 결과:{res}')

    def quiz09gugudan(self):  # 책받침구구단
        for i in (0, 4):
            for k in range(1, 10):
                for j in range(2, 6):
                    print(f'{j + i}*{k}={(j + i) * k}\t', end='')
                print("")
            print("")

    '''
    은행이름은 Bitbank
    입금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
    계좌번호는 3자리 - 2자리 - 6자리 형태로 랜덤하게 생성된다.
    123-12-123456
    '''

    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        Account.main()


class Account(object):
    BANK_NAME = '비트은행'

    def __init__(self, name, account_number, money):
        self.BANK_NAME = '비트은행'
        self.name = memberlist() if name == None else name
        '''
        a = myRandom(0, 999)
        b = myRandom(0, 99)
        c = myRandom(0, 999999)
        '''
        # self.account_number = f'{myRandom(0,999):0>3}-{myRandom(0,99):0>2}-{myRandom(0,999999):>6}'
        self.money = myRandom(100, 999) if money == None else money
        self.account_number = self.creat_account_number() if account_number == None else account_number

    def to_string(self):
        return (f'은행 : {self.BANK_NAME},' \
                f' 입금자: {self.name}, ' \
                f'계좌번호: {self.account_number},' \
                f' 금액: {self.money}만원')

    @staticmethod
    def creat_account_number():
        '''
        ls =[str(myRandom(0,9))for i in range(3)]
        ls.append("-")
        ls +=[str(myRandom(0,9))for i in range(2)]
        ls.append("-")
        ls += [str(myRandom(0,9))for i in range(6)]
        return "".join([])
        '''
        return "".join(["-" if i == 3 or i == 6 else str(myRandom(0, 9)) for i in range(13)])

        # [str(myRandom(0,9)) if str(myRandom(0,9) == myRandom[4] else '-' if myRandom(0,9) == myRandom[7]else range[2] == " "for i in range(13)]

    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def find_account(ls, account_number):
        a = ''.join([j.to_string() if j.account_number == account_number else '찾는 계좌 아님' for i, j in enumerate(ls)])
        return a

    @staticmethod
    def mimus_money(ls, find_account):
        pass

    @staticmethod
    def plus_money(ls, find_account, p_money):
        for i, j in enumerate(ls):
            if j.find_account == find_account:
                j.money += p_money
                return ls(j)

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌내용 3.입금 4.출금 5.계좌해지 6.계좌조회')
            if menu == '0':
                break
            if menu == '1':
                acc = Account(None, None, None)
                print(type(acc.to_string()))
                print(f'{acc.to_string()}...개설되었습니다.')
                ls.append(acc)
            elif menu == '2':
                a = '\n'.join(i.to_string() for i in ls)
                print(a)
            elif menu == '3':
                print(Account.plus_money(ls, input('입금 계좌번호'), int(input('입금 금액'))))

            elif menu == '4':
                account_number = input('출금할 계좌번호')
                money = input('출금액')
            elif menu == '5':
                Account.del_account(ls, input('탈퇴할 계좌번호'))
            elif menu == '6':
                print(Account.find_account(ls, input('조회할 계좌번호')))
            else:
                print('Wrong Number.. Try Again')
                continue

