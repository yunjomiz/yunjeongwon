import os

user_di = {}

def user_register(user):
  user_di[user.split(" ")[1]]=int(user.split(" ")[0]) # user_di에 key value로 학번 이름 따로 저장

def user_find(user):
  if user in user_di == True:
    print("존재하지 않습니다")
  else:
    print(f"{user_di.get(user)} {user}")

def user_view():
  for i in user_di.items():
    print(i)

def user_modify(user):
  user_di[user.split(" ")[1]]=int(user.split(" ")[0]) # user_di에 key value로 학번 이름 따로 저장

def user_del(user):
  del user_di[user]

while True:
  menu = """
  1. 사용자 등록
  2. 사용자 이름으로 조회
  3. 사용자 전체 조회
  4. 사용자 수정 및 수정내용 조회
  5. 사용자 삭제 및 확인
  """
  print(menu)
  choice = int(input("> ")) # 번호 고르기
  if choice == 1: # 1이면
    print("학번 이름> ", end = "")
    user = input() # 입력받기
    user_register(user)
    print("등록 완료")
  elif choice == 2:
    print("사용자 이름> ", end = "")
    user = input()
    user_find(user)
  elif choice == 3:
      user_view()
  elif choice == 4:
    print("사용자 이름> ", end = "")
    user = input()
    print("학번 이름> ", end = "")
    user = input()
    user.user_modify(user)
    print("수정 완료")
  elif choice == 5:
    print("사용자 이름> ", end = "")
    user = input()
    user_del(user)
    print("삭제 완료")