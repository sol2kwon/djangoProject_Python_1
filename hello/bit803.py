from hello.domains import myRandom, memberlist, bit803
import random
class Bit803:
    light = 0
    temp = 0

    def __init__(self):
        self.name = bit803()
        self.attendance = myRandom(0,1)
        self.age = myRandom(20,30)

    def attend(self):
        for i in range(1):
            return f'이름:{self.name} 나이:{self.age} 출석:{self.attendance}'

    def ctrl_temp(self):
        pass

    def ctrl_light(self):
        pass

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.출석여부 2.전등 3.내용 4.출금 5.계좌해지 ')
            if menu == '0':
                break
            if menu == '1':
                print(Bit803().attend())




