import unittest
from unittest.mock import patch
from io import StringIO
import sys
import random

user_di = {'홍길동': 1234, '성춘향': 5678}  # 사용자 데이터 미리 추가

def register_user():
    while True:
        print("학번 이름> ", end="")
        user_input = input()
        student_info = user_input.split(" ")
        if len(student_info) == 2 and student_info[0].isdigit():
            user_di[student_info[1]] = int(student_info[0])
            print("등록 완료")
            break
        else:
            print("올바른 형식의 학번과 이름을 입력하세요.")

def find_user_by_name():
    print("사용자 이름> ", end="")
    user_name = input().strip()
    user = user_di.get(user_name)
    if user is not None:
        print(f"{user} {user_name}")
    else:
        print("존재하지 않습니다")

def show_all_users():
    for user, value in user_di.items():
        print(f"{value} {user}", end=' ')
    print()

def update_user():
    print("사용자 이름> ", end="")
    user_name = input().strip()
    print("학번 이름> ", end="")
    user_input = input()
    user_di[user_name] = int(user_input.split(" ")[0])
    print("수정 완료")

def delete_user():
    print("사용자 이름> ", end="")
    user_name = input().strip()
    if user_name in user_di:
        del user_di[user_name]
        print("삭제 완료")
    else:
        print("사용자가 존재하지 않습니다.")

def select_menu(choice):
    if choice == 1:
        register_user()
    elif choice == 2:
        find_user_by_name()
    elif choice == 3:
        show_all_users()
    elif choice == 4:
        update_user()
    elif choice == 5:
        delete_user()
    elif choice == 6:
        return True
    else:
        print("잘못된 선택입니다. 다시 선택해주세요.")
    return False

class TestUserManagement(unittest.TestCase):

    def test_register_user(self):
        register_user()
        self.assertIn('홍길동', user_di)

    def test_find_user_by_name_existing(self):
        with patch('builtins.input', return_value='홍길동'):
            captured_output = StringIO()
            sys.stdout = captured_output
            find_user_by_name()
            sys.stdout = sys.__stdout__
            self.assertIn('1234 홍길동', captured_output.getvalue().strip())

    def test_find_user_by_name_nonexisting(self):
        with patch('builtins.input', return_value='Nonexistent'):
            captured_output = StringIO()
            sys.stdout = captured_output
            find_user_by_name()
            sys.stdout = sys.__stdout__
            self.assertEqual('존재하지 않습니다', captured_output.getvalue().strip())

    def test_show_all_users(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        show_all_users()
        sys.stdout = sys.__stdout__
        self.assertEqual('1234 홍길동 5678 성춘향', captured_output.getvalue().strip())

    def test_update_user(self):
        with patch('builtins.input', side_effect=['성춘향', '5678 Lily']):
            update_user()
            self.assertIn('Lily', user_di)

    def test_delete_user(self):
        with patch('builtins.input', return_value='홍길동'):
            delete_user()
            self.assertNotIn('홍길동', user_di)

if __name__ == '__main__':
    while True:
        menu = """
        1. 사용자 등록
        2. 사용자 이름으로 조회
        3. 사용자 전체 조회
        4. 사용자 수정
        5. 사용자 삭제
        6. 종료
        """
        print(menu)
        choice = int(input("> "))  # 번호 고르기
        if select_menu(choice):
            break
