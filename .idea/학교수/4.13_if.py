#단순 if

# a =10
# if a>0:
#     print("양수")
# print('종료')

#if /elif/else
# a=-1
# if a>0:
#     print("양수")
# elif a<0:
#     pass
# else:
#     print('제로')
# print('종료')


#비교 연산자
# a =10
# if a==0:
#     print('양수')
# elif a<0:
#     print('음수')
# else:
#     print('양수') ##
# print('종료')

#논리 연산자
# a=95
# if a>=90 and a<=100:
#     print("A")
# else:
#     print("B")
# print("종료")

#조건 분기문 예제
#점수를 입력받아 ABC등등 등급을 출력합니다
# score =int(input('점수를 입력하세요: '))
# if score>=90:
#     print("A")
# elif score>=80:
#     print("B")
# elif score>=70:
#     print("C")
# elif score>=60:
#     print("D")
# else:
#     print("F")

#조건 분기문 예제
#터틀 그래픽을 이용하여 다음 조건에 따른 프로그램을 작
# 성하세요.
# – 원점을 중심으로 가로, 세로 200 크기의 사각형을 그린다.
# – 마우스 이벤트를 이용하여 사각형 내부를 클릭하면 클릭한 지
# 점에 파랑색 원, 외부를 클릭하면 빨강색 원을 그린다.
# – 원의 크기는 반지름 5
import turtle as t
t.shape('turtle')

#사각형 그리기
t.penup()
t.goto(-100,-100)
t.pendown()
for i in range(4):
    t.forward(200)
    t.left(90)

def decision(x,y):
    if 100>=x>=-100 and 100>=y>=-100:
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.pencolor('Blue')
        t.circle(15)
    else:
        t.penup()
        t.goto(x,y)
        t.pendown()
        t.pencolor('Red')
        t.circle(15)
t.onscreenclick(decision)
t.done()







