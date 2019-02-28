#-*-coding:utf-8

# for 문 사용하기
# 기존 언어의 for 문과 다른 for ~ in 문의 형태를 하고 있음
# Java 에서는 for ~ in 문과 같고 C#에서는 foreach 문과 같은 형태의 반복문
# for 문의 조건절에 in 연산자를 사용하여 해당하는 리스트 및 튜플, 딕셔너리의 모든 요소를 카운트 변수 없이 출력할 수 있음
# for 문 사용시 괄호를 사용하지 않음

test_list = ["one", "two", "three"]

for i in test_list:
    print(i)

# for (int i = 0; i < test_list.length; i++) {
    # System.out.println(i)
# }
print()

# 리스트 a의 요소가 튜플로 구성되어 있어 in 연산자에서 리스트의 값을 받는 부분을 튜플로 지정해야함
# 튜플로 변수 선언 및 초기화 하는 방식인 (a, b) = (값1, 값2)을 사용하여 리스트 a의 요소 데이터를 대입받음
a = [(1,2), (3,4), (5,6)]
for (asd, qwe) in a:
    print(asd + qwe)

# 문제 1) 1 ~ 10까지의 합을 구하는 프로그램을 for문을 사용하여 만드세요

listNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumNum = 0

for value in listNum:
    sumNum += value

print("1 ~ 10까지의 합은 : {0}".format(sumNum))

print()

marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks:
    number += 1

    if mark >= 60:
        print("{0}번 학생은 합격입니다".format(number))
    else:
        print("{0}번 학생은 불합격입니다.".format(number))

# for문에서 continue 사용
# while문에서의 continue 사용법과 동일함

print()

marks = [90, 25, 67, 45, 80]
number = 0

for mark in marks:
    number += 1

    if mark < 60:
        continue
    print("{0}번 학생 축하합니다.".format(number))

print()
number = 0

for mark in marks:
    number += 1

    if mark < 60:
        break
    print("{0}번 학생 축하합니다.".format(number))

# for 문과 range() 함수 사용하기
# range() 함수는 지정한 범위의 숫자의 리스트를 자동 생성
# range(시작숫자, 끝숫자), 시작 숫자를 제외하면 0에서 지정한 끝 숫자까지 자동 생성
print()

print(range(10))
print(range(1, 11))

sum = 0
for i in range(1, 11):
    sum += i

print(sum)

print()

for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print()

# 문제 2) 사용자 입력을 받아 해당하는 단수의 구구단을 출력하세요
# dan = input("출력할 구구단을 입력하세요 : ")
# dan = int(dan)
dan = 5

for val in range(1, 10):
    # print() 함수의 끝은 \n이 붙어있음
    # end를 사용하게 되면 끝나는 부분에 다른 문자를 입력할 수 있음
    print(dan * val, end=" ")
print("")

# 리스트 내포 사용하기
# 리스트에 for ~ in 문을 사용하여 리스트의 요소를 자동 생성하는 방식

# 기존 방식
a = [1, 2, 3, 4]
result = []

for num in a:
    result.append(num * 3)

print(result)

# 리스트 내포 방식
a = [1, 2, 3, 4]
result = [num * 3 for num in a]
print("리스트 내포 방식으로 result 출력 : {0}".format(result))

print()

result = [num * 3 for num in a if num % 2 == 0]
print("리스트 내포 방식으로 for문과 if 문 사용 : {0}".format(result))

# 문제 3) listNum 이라는 리스트에 숫자가 1부터 10까지 들어있다. 이 리스트를 리스트 내포 방식을 사용하여 복사하세요
# 복사 받을 리스트의 이름 : listCopy

listNum = range(1, 11)
listCopy = [num for num in listNum]
print("원본 리스트 listNum : {0}".format(listNum))
print("사본 리스트 listCopy : {0}".format(listCopy))

print()

result = [x * y for x in range(2, 10)
    for y in range(1, 10)]

print(result)

# 연습문제 1
# if 문에서 and, or 연산을 통해서 논리적 값을 얻기 위해서 연산을 실행할 경우 True인지 False인지 확인하는 순서가 존재함
# 순서는 앞에서부터 순차적으로 진행이 되고 만약 앞쪽에서 원하는 결과가 나온다면 뒤 쪽의 논리적 연산을 하지 않는다.
a = "Life is too short, you need python"
if "wife" in a: # 없어서 False
    print("wife")
elif "python" in a or "you" not in a: # and 연산이므로 2개의 조건이 모두 True이어야하는데 뒤의 조건에서 False 임
    print("python")
elif "shirt" not in a: # 조건에 맞아서 True
    print("shirt")
elif "need" in a: # 조건에 맞긴하지만 위에서 먼저 조건에 부합하기 때문에 아래에 있는 elif문은 실행을 안함
    print("need")
else:
    print("none")

# 연습 2번
i = 0
while True:
    i += 1
    if i > 5: break
    print("*" * i)

# 연습3
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for value in A:
    total += value
average = total / len(A)
print(average)