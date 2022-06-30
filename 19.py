# 객체의 속성 변경
class NewPC:

    def __init__(self, name, cpu, memory, ssd):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd

    def doExcel(self):
        print('EXCEL RUN!')

    def dophoto(self):
        print('PHOTO RUN!')

    def printinfo(self):
        print(f'name   : {self.name}')
        print(f'cpu    : {self.cpu}')
        print(f'memory : {self.memory}')
        print(f'ssd    : {self.ssd}')


myPC = NewPC('myPC', 'i5', '16G', '256G')
myPC.printinfo()

# 속성 변경하기
myPC.cpu = 'i7'
myPC.memory = '32G'
myPC.ssd = '512G'
myPC.printinfo()