def print_animal(number):
    if number == 1:
        # 고양이
        cat = """
        /\\_/\\
       ( o.o )
        > ^ <
        """
        print("고양이")
        print(cat)
    elif number == 2:
        # 강아지
        dog = """
         / \\__
        (    @\\___
        /         O
       /   (_____/
       /_____/   U
        """
        print("강아지")
        print(dog)
    elif number == 3:
        # 토끼
        rabbit = """
        (\\(\\
       (='.')
       (")_(")
        """
        print("토끼")
        print(rabbit)
    elif number == 4:
        # 코끼리
        elephant = """
        _____
       /     \\
      | ^   ^ |
      (  (O)  )
       \\_____/
        /   \\
       /     \\
        """
        print("코끼리")
        print(elephant)
    elif number == 5:
        # 펭귄
        penguin = """
         _____
        /     \\
       | (o)_(o) |
       |  (_)   |
       |       |
       \\      /
        \\____/
        """
        print("펭귄")
        print(penguin)

def main():
    print("숫자를 입력하세요.")
    
    while True:
        try:
            number = int(input("\n숫자를 입력하세요 (0-5): "))
            
            if number == 0:
                print("프로그램을 종료합니다.")
                break
            elif 1 <= number <= 5:
                print_animal(number)
            else:
                print("1부터 5 사이의 숫자를 입력해주세요.")
        except ValueError:
            print("잘못입력.")

if __name__ == "__main__":
    main()
