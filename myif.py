# 아스키 코드 그림 출력하기
def print_cat_ascii_art():
    cat_art = r"""
 /\\_/\\  
( o.o ) 
 > ^ <
"""
    print(cat_art)

if __name__ == "__main__":
    print_cat_ascii_art()


def print_dog_ascii_art():
    dog_art = r"""
  / \\__
 (    @\\___
 /         O
/   (_____/
/_____/  U
"""
    print(dog_art)

if __name__ == "__main__":
    print_dog_ascii_art()



def print_rabbit_ascii_art():
    rabbit_art = r"""
 (\\(\\ 
 ( -.-)
 o_(")(")
"""
    print(rabbit_art)

if __name__ == "__main__":
    print_rabbit_ascii_art()


print("그림 출력 프로그램")
print("============================")
print("1. 고양이")
print("2. 강아지")
print("3. 토끼")
print("============================")
n = int(input("선택: "))
# 만약에 1을 입력하면 1번 캐릭터 출력
if n == 1:
    print("고양이")
    print_cat_ascii_art()
# 만약에 2를 입력하면 2번 캐릭터 출력
elif n == 2:
    print("강아지")
    print_dog_ascii_art()
# 만약에 3을 입력하면 3번 캐릭터 출력
elif n == 3:
    print("토끼")
    print_rabbit_ascii_art
# 잘못 입력하면 잘못 입력했다고 출력
else :
    print("잘못입력")