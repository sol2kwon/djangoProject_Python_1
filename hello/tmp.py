class Tmp:
    def __init__(self):
        self.name = 'sonata'
        self.speed = 0
        self.oil = 110

    def ctrl_speed(self, speed):
        print(f'경고') if self.spend_oil(50) < 20 else print('기름 많음')
        self.speed += speed

    def spend_oil(self, oil):
        self.oil -= oil
        return self.oil


if __name__ == '__main__':
    car = Tmp()

    print('변경 전 스피드')
    print(car.speed)

    car.ctrl_speed(20)  # 인자(argument)의 값만큼 스피드 증가
    print('변경 후 스피드1')
    print(car.speed)

    print(f'오일 잔량:{car.oil}')

    car.ctrl_speed(10)  # 인자(argument)의 값만큼 스피드 증가
    print('변경 후 스피드2')
    print(car.speed)

    print(f'오일 잔량:{car.oil}')

    print(f'오일 잔량:{car.spend_oil(-100)}')
