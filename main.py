import turtle

import random

# 색상 리스트
COLOR_LIST = ['light blue', 'royal blue', 
              'light steel blue', 'steel blue',
              'light cyan', 'light sky blue', 
              'violet', 'salmon', 'tomato',
              'sandy brown', 'purple', 'deep pink', 
              'medium sea green', 'khaki']

screen = turtle.Screen()
screen.title("벽돌깨기")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0) #스크핀 업데이트를 수동으로 제어

paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5) #패들 크기 조정
paddle.penup()
paddle.goto(0, -250)

#공
ball = turtle.Turtle()
ball.shape('circle')
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25 #공 x축 이동속도
ball.dy = -0.25 #공 y축 이동속도

#패들 이동 함수
def paddle_right():
    x = paddle.xcor()
    if x < 350:  # 경계 처리
        x += 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -350:  # 경계 처리
        x -= 20
    paddle.setx(x)

# 키보드 입력 설정
screen.listen()
screen.onkey(paddle_right, "Right")
screen.onkey(paddle_left, "Left")


# 벽돌 생성 함수
bricks = []

for i in range(5):  # 행
    for j in range(8):  # 열
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(random.choice(COLOR_LIST))  # 벽돌의 초기 색상 무작위 선택
        brick.shapesize(stretch_wid=1.3, stretch_len=4.8)
        brick.penup()
        brick.goto(-350 + (j * 100), 250 - (i * 30))
        bricks.append(brick)

# 벽돌 색상 변경 함수
def change_bricks_color():
    for brick in bricks:
        brick.color(random.choice(COLOR_LIST))



while True:
    screen.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # 경계 처리
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1



        # 패들과 충돌 처리
    if ball.ycor() > -240 and ball.ycor() < -230 and ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50:
        ball.sety(-230)
        ball.dy *= -1

     # 벽돌과의 충돌 감지
    for brick in bricks:
        if ball.distance(brick) < 30:
            change_bricks_color()  # 모든 벽돌의 색상 변경
            brick.goto(1000, 1000)  # 벽돌을 화면에서 제거
            bricks.remove(brick)
            ball.dy *= -1
            break  # 충돌 후 다음 충돌까지 루프를 진행

    if ball.ycor() < -290:
        # ball.goto(0, 0)
        # ball.dy *= -1  # 바닥에 닿으면 초기화 (게임 종료 조건으로 확장 가능)
        print("Game Over")
        break #공이 바닥에 닿으면 게임 종료

    # 승리 조건
    if not bricks:  # 벽돌 리스트가 비었을 때
        print("You Win!")
        break