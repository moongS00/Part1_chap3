# 중간고사 클래스와 기말고사 클래스를 상속관계로 만들고
# 각각의 점수를 초기화하자.
# 또한 총점 및 평균을 반환하는 기능도 만들어보자

class Mid:

    def __init__(self, s1, s2, s3):
        print('[Mid] __init__()')

        self.mid_kor_score = s1
        self.mid_eng_score = s2
        self.mid_mat_score = s3

    def printScore(self):
        print(f'mid_kor_score : {self.mid_kor_score}')
        print(f'mid_eng_score : {self.mid_eng_score}')
        print(f'mid_mat_score : {self.mid_mat_score}')


class Final(Mid):

    def __init__(self, s1, s2, s3, s4, s5, s6):
        print('[Final] __init__()')

        super().__init__(s1, s2, s3,)

        self.fianl_kor_score = s4
        self.final_eng_score = s5
        self.final_mat_score = s6

    def printScore(self):
        super().printScore()   #상속받은 기능
        print(f'fianl_kor_score : {self.fianl_kor_score}')
        print(f'final_eng_score : {self.final_eng_score}')
        print(f'final_mat_score : {self.final_mat_score}')

    def total(self):
        total = self.mid_kor_score + self.mid_eng_score + self.mid_mat_score
        total += self.fianl_kor_score + self.final_eng_score + self.final_mat_score

        return total

    def average(self):
        return self.total() / 6



my = Final(85,90,88,75,85,95)
my.printScore()
print(f'총점 : {my.total()}')
print(f'평균 : {round(my.average(),2)}')