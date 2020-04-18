# from random import *
# print(random())
# print(random()*10)
# print(int(random()*10))
# print(randrange(1,46))

# sentence = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence)

# python = "Python is amazing"
# print(python.replace("Python", "Java"))
# print(python.index("P"))
# print(python.find("a"))
# print(python.find("Java"))
# print((2 / 29.1) *  0.393701) 
# print("나는 %s%d를 좋아해요." % ("파이썬", 3))
# print("나는 {0}{1}을 가지고 있어요.".format("갤럭시S", 20))
# print("나는 {age}살이고 {color}색을 좋아해요.".format(age=28, color="주황"))

# age=28
# color="주황"
# print(f"나는 {age}살이고 {color}색을 좋아해요.(ver.2)")
# print("문장 안에서 큰따옴표를 표시하는 방법은 \"이것\" 입니다.")
# print("문장 안에서 역슬래시를 쓰는 방법은 \\ 처럼 두 번 쓰면 됩니다.")
# print("백스페이스로 문자를 삭제하려면 Redd\bApple 처럼 쓰면 됩니다.") 


""" --------- 문자열 처리 예제 --------- """
# url = "http://naver.com"
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# # 남은 문자열 중 처음 세자리 + 글자개수 + 글자 내 'e' 개수 + "!" 로 구성
# ans = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0} 의 비밀번호는 {1} 입니다.".format(url, ans))


""" --------- 리스트 --------- """
# subway = ["유재석", "박명수", "정준하"]
# subway.append("하하")
# subway.insert(1, "노홍철") 
# print(subway)
# subway.pop()
# print(subway)

# num_list = [1,3,5,2,4] 
# num_list.sort()
# print(num_list)
# num_list.reverse()
# print(num_list)
# num_list.clear()
# print(num_list)
# num_list.extend(subway)
# print(num_list) 


""" --------- 사전 --------- """
# cabinet = {3:"유재석", 100:"김태호"} #키는 문자열도 가능
# print(cabinet.get(3), cabinet[100])
# print(cabinet.get(5, "저장된 키가 없으니 이것을 출력"))
# print(3 in cabinet, 5 in cabinet)
# del cabinet[3]
# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())


""" --------- 튜플 --------- """
#리스트처럼 내용 변경은 불가능하나 리스트보다 속도가 빠르다.

# menu = ("돈까스", "김밥")
# print(menu[0], menu[1])
# (name, age, hobby) = ("종국", 30, "운동")
# print(name, age, hobby)


""" --------- 세트 --------- """
#집합(set). 중복 안되고 순서가 없음

# python = {"유재석", "박명수", "정준하"}
# java = set(["유재석", "하하"])
# print(python & java) #교집합
# print(python.intersection(java))
# print(python | java) #합집합
# print(python.union(java))
# print(python - java) #차집합
# print(python.difference(java))

# python.add("노홍철")
# python.remove("유재석")
# print(python)

#자료구조를 변경할 수도 있다.
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))
# menu = list(menu)
# print(menu, type(menu))
# menu = tuple(menu)
# print(menu, type(menu))
# menu = set(menu)
# print(menu, type(menu))


""" --------- 자료구조 예제 ---------
1명은 치킨, 3명은 커피 쿠폰 당첨 이벤트.
- 조건1: 20명이고 id는 1~20
- 조건2: 무작위로 추첨하되 중복 불가
- 조건3: random 모듈의 shuffle, sample 활용

(ex) 다음과 같이 출력,
치킨 당첨자: 1
커피 당첨자: [2, 3, 4]
"""

# from random import *
# id = list(range(1, 21))
# print(id, type(id))
# shuffle(id)
# winners = sample(id, 4)
# print("치킨 당첨자: {0}".format(winners[0]))
# print("커피 당첨자: {0}".format(winners[1:])) 
#막판에 어려웠다


""" --------- 제어문 --------- """
# for waiting_no in [0, 1, 2, 3, 4]: #혹은 range(0, 5)
#     print("대기번호: {0}".format(waiting_no))

# student = ["Iron man", "Thor", "I am groot"]
# length = [len(i) for i in student]
# print(length)
# Upper = [i.upper() for i in student]
# print(Upper)


""" --------- 제어문 예제 ---------
택시기사가 50명의 손님과 매칭할 수 있을때 총 탑승객 수는?
- 조건1: 승객별 탑승 시간은 5~50분 사이 난수
- 조건2: 5~15분 탑승 시간의 손님만 매칭 가능

(ex.출력문)
[O] 1번째 손님 (소요시간: 15분)
[ ] 2번째 손님 (소요시간: 25분)
...
[ ] 50번째 손님 (소요시간: 16분)
총 탑승객 수: 2 명 """

# from random import *
# count = 0
# for customers in range(1, 51):
#     time = randint(5, 50)
#     if time >= 5 and time <= 15:
#         print("[O] {0}번째 손님 (소요시간: {1}분)".format(customers, time))
#         count += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간: {1}분)".format(customers, time))
# print("총 탑승객 수: ", count, "명")
#내가 짰다 ㅎㅎ


""" --------- 함수 --------- """
# def deposit(balance, money): #입금
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# balance = 0
# balance = deposit(balance, 1000)

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance - money

# balance = withdraw(balance, 1000)

# def withdraw_night(balance, money):
#     commission = 100
#     if balance >= (money + commission):
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money - commission))
#         return commission, balance - money - commission

# balance = deposit(balance, 1100)
# commission, balance = withdraw_night(balance, 1000)
# print("수수료: {0}원, 잔액: {1}원".format(commission, balance))

# def profile(name, age, *language): #인자에 *을 쓸 경우 가변인자.
#     print("이름: {0}\t 나이: {1}\t".format(name, age), end =" ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", "38", "Python", "Java", "C#")
# profile("조세호", "32", "Ruby")

# gun = 10
# def checkpoint(soldiers):
#     global gun #전역변수 gun을 사용
#     gun = gun - soldiers
#     print("남은 총: {0}".format(gun))
#     return gun

# print("전체 총: {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("남은 총: {0}".format(gun))

# checkpoint_ret(checkpoint(2), 2) 
# #첫번째 인자에서 checkpoint 함수를 실행 후 리턴값을 받고 checkpoint_ret 실행.
# print("전체 총: {0}".format(gun))
# #checkpoint_ret 실행할 때 전역변수 gun 은 바뀌지 않으며 지역변수 gun 을 출력


""" --------- 함수 예제 ---------
표준체중을 구하는 프로그램 작성.
*표준체중: 각 개인의 키에 적당한 체중.

(성별에 따른 공식)
남 = 키(m) x 키(m) x 22
여 = 키(m) x 키(m) x 21

- 조건1: 표준체중은 별도의 함수 내에서 계산
    *함수명: std_weight
    *전달값: 키(height), 성별(gender)
- 조건2: 값은 소수점 둘째자리까지 표기

(출력 예제)
키 175cm 남자의 표준체중은 67.38kg 입니다. """

# def std_weight(height, gender):
#     hei = height / 100
#     if gender == "남자":
#         print("키 {0}cm 남자의 표준체중은 {1}kg 입니다.".format(height, round(hei * hei * 22, 2)))
#     elif gender == "여자":
#         print("키 {0}cm 여자의 표준체중은 {1}kg 입니다.".format(height, round(hei * hei * 21, 2)))

# std_weight(175, "남자")
# std_weight(163, "여자")


""" --------- 입출력 --------- """
# print("Python", "Java", sep=",", end='?') 

# scores = {"영어": 0, "수학": 50, "코딩": 100} 
# for subject, score in scores.items():
#     print(subject.ljust(1), str(score).rjust(4), sep = ":")

# for num in range(1, 11):
#     print("대기번호:", str(num).zfill(3))

# "앞에 빈 공간 10자리 확보하고 오른쪽 정렬하되 +/- 값 출력"
# print("{0:>+10}".format(500))
# print("{0:>10}".format(-500))

# "왼쪽 정렬하되 빈칸은 '_' 로, 값 출력"
# print("{0:_<10}".format(500))

# #세자리수마다 ',' 찍고 +/- 값 출력
# print("{0:+,}".format(100000000000))
# print("{0:,}".format(-100000000000))

# #소수로 출력하되 3번째 자리에서 반올림하여 출력
# print("{0:.2f}".format(5/3))

# score_file = open("scores.txt", "w", encoding="utf8")
# print("영어: 50", file=score_file)
# print("수학: 100", file=score_file)
# score_file.close()

# score_file = open("scores.txt", "a", encoding="utf8")
# score_file.write("과학: 80")
# score_file.write("\n코딩: 70")
# score_file.close()

# score_file = open("scores.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("scores.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for List in lines:
#     print(List, end="")
# score_file.close()


""" --------- pickle 모듈 --------- """
# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이": 40, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile 정보를 profile_file 에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) #profile_file 의 정보를 profile 에 로드
# print(profile)
# profile_file.close()


""" --------- with  --------- """
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬 공부")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


""" --------- 입출력 예제 ---------
다음과 같이 매주 1건 보고서 작성해야함. 으 극혐.

- ( )주차 주간보고서 -
부서 : 
이름 :
업무 요약 : 

1주차부터 10주차까지 보고서 만드는 프로그램?
- 조건: 파일명은 '1주차.txt', '2주차.txt', ...
"""

# # for문에서 in 뒤에 들어가는 인자는 iterable 해야하며, int형은 not iterable!
# def writeReport(toWeek):
#     for week in range(1, toWeek + 1):
#         report = open("{0}주차.txt".format(week), "w", encoding="utf8")
#         report.write("- {0}주차 주간보고서 -".format(week))
#         report.write("\n부서 : ")
#         report.write("\n이름 : ")
#         report.write("\n업무 요약 : ")

# writeReport(10)


""" --------- 클래스 --------- """
# from random import *
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name #self.( )로 멤버변수 선언.
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(self.name))

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} -> {1} 방향으로 이동합니다. [속도: {2}]"\
#             .format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} -> {1} 만큼 피해를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0}의 남은 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} 유닛이 파괴되었습니다.".format(self.name))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed) #Unit 클래스를 상속받음
#         self.damage = damage
    
#     #함수 내에서 'self'를 쓰려면 인자로 'self'를 받아야함.
#     def attack(self, location):
#         print("{0} -> {1} 방향으로 공격합니다. [공격력: {2}]"\
#             .format(self.name, location, self.damage))
    
# # marine1 = AttackUnit("마린1", 40, 5)
# # print("유닛이름: {0},  공격력: {1}".format(marine1.name, marine1.damage))
# # wraith1 = AttackUnit("레이스1", 80, 8)
# # wraith1.attack("5시")
# # wraith1.damaged(40)

# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 5, 6)
    
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} -> 스팀팩을 사용합니다. [현재 체력: {1}]"\
#                 .format(self.name, self.hp))
#         else:
#             print("{0} -> 체력이 부족합니다.".format(self.name))

# class Tank(AttackUnit):
#     seizeMode_developed = False
#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 5, 30)
#         self.seizeMode = False

#     def set_seizeMode(self):
#         if Tank.seizeMode_developed == False:
#             return
#         if self.seizeMode == False:
#             self.seizeMode == True
#             print("{0} -> 시즈모드로 전환".format(self.name))
#             self.damage *= 2
#         else:
#             self.seizeMode == False
#             print("{0} -> 시즈모드를 해제".format(self.name))
#             self.damage /= 2

# class Flyable: 
#     def __init__(self, flyingSpeed):
#         self.flyingSpeed = flyingSpeed
    
#     def fly(self, name, location):
#         print("{0} -> {1} 방향으로 날아갑니다. [속도: {2}]"\
#             .format(name, location, self.flyingSpeed))

# class AttackUnit_Flyable(AttackUnit, Flyable): #다중 상속 클래스
#     def __init__(self, name, hp, damage, flyingSpeed):
#         #AttackUnit 을 상속받고 공중유닛의 지상속도(speed)는 0
#         AttackUnit.__init__(self, name, hp, 0, damage) 
#         Flyable.__init__(self, flyingSpeed) #Flyable 를 상속받음
    
#     def move(self, location): #메소드 오버라이딩
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location) 

# class Wraith(AttackUnit_Flyable):
#     def __init__(self):
#         AttackUnit_Flyable.__init__(self, "레이스", 80, 8, 10)
#         self.clockingMode = False
        
#     def set_clockingMode(self):
#         if self.clockingMode == False:
#             self.clockingMode == True
#             print("{0} -> 클로킹모드로 전환".format(self.name))
#         else:
#             self.clockingMode == False
#             print("{0} -> 클로킹모드를 해제".format(self.name))

# # valkyrie = AttackUnit_Flyable("발키리", 150, 6, 5)
# # valkyrie.fly(valkyrie.name, "7시")

# # vulture = AttackUnit("벌쳐", 80, 10, 20)
# # battlecruiser = AttackUnit_Flyable("배틀크루져", 500, 25, 4)
# # vulture.move("6시")
# # battlecruiser.fly(battlecruiser.name, "4시")
# # battlecruiser.move("11시")

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # pass
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) #super 를 쓸땐 'self' 안씀.
#         # 다중상속일 땐 super 안 쓴다.
#         self.locaiton = location

# supplyDepot = BuildingUnit("서플라이디폿", 500, "3시")

# def game_start():
#     print("[알림] 게임을 시작합니다.")
# def game_over():
#     print("Player: gg\n" + "[Player] 가 게임에서 나갔습니다!")

# #게임 시작!
# game_start()
# m1, m2, m3, t1, t2, w1 = Marine(), Marine(), Marine(),\
#     Tank(), Tank(), Wraith()

# attack_unit = []
# attack_unit.append(m1), attack_unit.append(m2), attack_unit.append(m3),\
#     attack_unit.append(t1), attack_unit.append(t2), attack_unit.append(w1)

# for unit in attack_unit:
#     unit.move("1시")

# Tank.seizeMode_developed = True
# print("[알림] 시즈모드가 개발되었습니다.")

# for unit in attack_unit:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seizeMode()
#     elif isinstance(unit, Wraith):
#         unit.set_clockingMode()

# for unit in attack_unit:
#     unit.attack("2시")
#     unit.damaged(randint(5, 41))

# game_over() #게임 종료!

""" --------- 클래스 예제 ---------
아래 코드를 활용해 부동산 프로그램 작성.

class House:
    #매물 초기화
    def __init__(self, location, house_type, deal_type,
        price, completion_year):
        pass

    #매물 정보 표시
    def show_detail(self):
        pass

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년 """

# class House:
#     def __init__(self, location, house_type, deal_type,\
#         price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type,\
#             self.price, self.completion_year)

# deal1 = House("강남", "아파트", "매매", "10억", "2010년")
# deal2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# deal_list = []
# deal_list.append(deal1)
# deal_list.append(deal2)

# print("총 {0}대의 매물이 있습니다.".format(len(deal_list)))
# for num in deal_list:
#     num.show_detail()
# # 함수만으로 출력을 구현하고 싶었다..


""" --------- 예외 처리 --------- """
# class BigNumErr(Exception): #사용자 정의 예외 처리
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요: ")))
#     nums.append(int(input("두번째 숫자를 입력하세요: ")))
#     if nums[0] >= 10 or nums[1] >= 10:
#         raise BigNumErr("초과 입력값: {0}, {1}".format(nums[0], nums[1]))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 10 미만의 정수를 입력하세요.")
# except BigNumErr as err:
#     print("입력값이 초과되었습니다.\n", err)
#     # print(err)
# except ZeroDivisionError as err:
#     print(err) #실제 발생 에러를 그대로 출력
# except Exception as err:
#     print("알수 없는 에러가 발생하였습니다.") #위의 경우 외 에러를 출력
#     print(err) #실제 발생 에러를 그대로 출력
# finally:
#     print("게산기를 이용해 주셔서 감사합니다.")

""" --------- 예외 처리 예제 --------- 
치킨 주문 시간 절약을 위해 주문 자동 시스템을 만드려할때
시스템 코드를 확인하고 적절한 예외 처리 구문을 활용해 코드 수정.

chicken = 10
waiting = 1 #대기번호 1부터 시작
while(True):
    print("[남은치킨: {0}]".format(chicken))
    order = int(print("치킨 몇 마리 주문하세요?))
    if order > chicken:
        print("재료가 부족합니다.")
    else:
        print("[대기번호: {0}] 치킨 {1}마리 주문 완료되었습니다."\
            .format(waiting, order))
        waiting += 1
        chicken -= order 
        
- 조건1: 1보다 작거나 숫자가 아니면 ValueError
- 조건2: 주문 가능 총량은 치킨 10마리, 치킨 소진 시 예외처리: [SoldoutError] """

# class SoldoutError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# chicken = 10
# waiting = 1 #대기번호 1부터 시작
# while(True):
#     try:
#         print("[남은치킨: {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하세요?: "))
#         if order > chicken:
#             print("재료가 부족합니다.")
#         elif order < 1:
#             raise ValueError
#         else:
#             print("[대기번호: {0}] 치킨 {1}마리 주문 완료되었습니다."\
#                 .format(waiting, order))
#             waiting += 1
#             chicken -= order
#             if chicken == 0:
#                 raise SoldoutError("재고가 소진되었습니다.")

#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldoutError as err:
#         print(err)
#         break


""" --------- 모듈과 패키지 --------- """
# import theater_module as tm
# tm.price(3)
# tm.price_morning(2)

# from theater_module import *
# price_soldier(4)

# # import 단독구문은 모듈이나 패키지만 작성 가능.
# import travel.thailand 
# trip_to1 = travel.thailand.ThailandPackage()
# trip_to1.detail()

# # 그러나 form - import 구문은 import 뒤에 클래스도 작성 가능.
# from travel.vietnam import VietnamPackage 
# trip_to2 = VietnamPackage()
# trip_to2.detail()

# # __init__.py 에서 __all__ 을 작성하였기 때문에 import * 불러오기 가능.
# # 원래는 개발자가 import 다음에 직접 명시해주어야 함.
# from travel import *
# trip_to3 = thailand.ThailandPackage()
# trip_to3.detail()


""" --------- 모듈 직접 실행 --------- """
# # thailland.py 파일을 보면 모듈 내에서 실행하느냐, 외부에서 실행하느냐에 따라 출력값이 다름
# from travel import thailand
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# import inspect, random 
# print(inspect.getfile(random)) #모듈의 path를 출력
# print(inspect.getfile(thailand))


""" --------- 내장/외장 함수 --------- """
# import random #random은 외장함수
# #dir: 받는 객체가 가지는 변수, 함수들을 모두 표시
# print(dir(random))

# import glob
# #glob: 경로 내의 폴더, 파일의 목록 조회(윈도우에서는 dir)
# print(glob.glob("*.py"))

# import os
# #os: 운영체제에서 제공하는 기본 기능
# print(os.getcwd())
# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더가 생성되었습니다.")
# print(os.listdir())

# import time, datetime
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
# today = datetime.date.today()
# print("오늘 날짜는", today)
# td = datetime.timedelta(days=100) #td 객체에 100일 저장
# print("앞으로 100일 후는", today + td)


""" --------- 모듈과 패키지 예제 --------- 
프로젝트 내에 나만의 시그니쳐를 남기는 모듈 작성.
- 조건: 모듈 파일명은 byme.py 로 작성

(모듈 사용 예)
import byme
byme.sign()

(출력 예)
이 프로그램은 나도코딩에 의해 만들어졌어요.
유튜브: http://youtube.com
이메일: nadocoding@gmail.com """
#너무 쉬워서 패쓰








# smarthome-51c4f-mymatrix-crau8q

# scp ~/Downloads/client_secret_*.json pi@192.168.0.215:/home/pi