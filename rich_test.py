# Rich를 사용한 동물 아스키 아트 프로그램 (화려한 테두리와 이모지)
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import print
from rich import box
import random

# Rich 콘솔 객체 생성
console = Console()

# 화려한 테두리 스타일 세트
BORDER_STYLES = ["red", "green", "blue", "magenta", "cyan", "yellow", "bright_red", "bright_green", 
                 "bright_blue", "bright_magenta", "bright_cyan", "bright_yellow", "purple", "orange3"]

# 다양한 테두리 타입
BOX_TYPES = [box.ROUNDED, box.DOUBLE, box.HEAVY, box.SQUARE, box.SIMPLE]

# 동물별 이모지 세트
CAT_EMOJIS = ["🐱", "😺", "😸", "😻", "🐈", "😽"]
FOX_EMOJIS = ["🦊", "🔥", "🍂", "🦝", "🍁"]
TURTLE_EMOJIS = ["🐢", "🐿️", "🌿", "🌱", "🍃"]
GENERAL_EMOJIS = ["✨", "🌟", "💫", "⭐", "🎮", "💡", "🎯", "🎨"]

# 랜덤 이모지 선택
def get_random_emojis(emoji_set, count=2):
    return " ".join(random.sample(emoji_set, min(count, len(emoji_set))))

# 예쁜 출력 함수 - 모든 출력을 이 함수로 통일
def pretty_print(message, style="bold", border_style=None, title=None, box_type=None, emojis=None):
    """예쁜 패널로 메시지 출력 (이모지 추가)"""
    if border_style is None:
        border_style = random.choice(BORDER_STYLES)
    
    if box_type is None:
        box_type = random.choice(BOX_TYPES)
    
    if emojis and title:
        title = f"{emojis} {title} {emojis}"
    elif title and not emojis:
        gen_emojis = get_random_emojis(GENERAL_EMOJIS)
        title = f"{gen_emojis} {title} {gen_emojis}"
    
    if title:
        console.print(Panel(message, title=title, style=style, border_style=border_style, box=box_type))
    else:
        console.print(Panel(message, style=style, border_style=border_style, box=box_type))

# 고양이, 여우, 거북이 아스키 아트를 출력하는 함수들
def draw_cat():
    # 고양이 이모지를 아스키 아트에도 추가
    cat_emoji = random.choice(CAT_EMOJIS)
    cat = [
        f"   /\\_/\\  {cat_emoji}",
        "  ( [bold yellow]o.o[/bold yellow] ) ",
        "   > [bold red]^[/bold red] <  ",
        "  / [bright_cyan]_[/bright_cyan] \\   ",
        " ([bright_magenta]__|__[/bright_magenta])  ",
        f"   [bold cyan]고양이[/bold cyan] {cat_emoji} "
    ]
    cat_text = "\n".join(cat)
    box_type = random.choice(BOX_TYPES)
    border_style = random.choice(BORDER_STYLES)
    cat_emojis = get_random_emojis(CAT_EMOJIS)
    pretty_print(cat_text, title=f"[bold magenta]고양이[/bold magenta]", 
                border_style=border_style, box_type=box_type, emojis=cat_emojis)

def draw_fox():
    # 여우 이모지를 아스키 아트에도 추가
    fox_emoji = random.choice(FOX_EMOJIS)
    fox = [
        f"   /\\___/\\  {fox_emoji}",
        "  /  [bold yellow]o o[/bold yellow]  \\ ",
        " ( =  [bold red]^[/bold red]  = )",
        "  )  [bright_yellow]-*-[/bright_yellow]  ( ",
        " (   [bright_cyan]\\_/[/bright_cyan]   )",
        "  [bright_red]\\_______/[/bright_red] ",
        f"    [bold orange3]여우[/bold orange3] {fox_emoji}   "
    ]
    fox_text = "\n".join(fox)
    box_type = random.choice(BOX_TYPES)
    border_style = random.choice(BORDER_STYLES)
    fox_emojis = get_random_emojis(FOX_EMOJIS)
    pretty_print(fox_text, title=f"[bold orange3]여우[/bold orange3]", 
                border_style=border_style, box_type=box_type, emojis=fox_emojis)

def draw_turtle():
    # 거북이 이모지를 아스키 아트에도 추가
    turtle_emoji = random.choice(TURTLE_EMOJIS)
    turtle = [
        f"    [bright_green]_____[/bright_green]    {turtle_emoji}",
        "   /     \\   ",
        "  | [bold blue]-   -[/bold blue] |  ",
        "  |   [bold green]V[/bold green]   |  ",
        "   [bright_blue]\\_____/[/bright_blue]   ",
        " [bright_green]_/[/bright_green]  | |  [bright_green]\\_[/bright_green] ",
        f"     [bold green]거북이[/bold green] {turtle_emoji}  "
    ]
    turtle_text = "\n".join(turtle)
    box_type = random.choice(BOX_TYPES)
    border_style = random.choice(BORDER_STYLES)
    turtle_emojis = get_random_emojis(TURTLE_EMOJIS)
    pretty_print(turtle_text, title=f"[bold green]거북이[/bold green]", 
                border_style=border_style, box_type=box_type, emojis=turtle_emojis)

# 선택에 따라 동물을 출력하는 play 함수
def play(number):
    menu_emojis = get_random_emojis(GENERAL_EMOJIS)
    
    if number == 1:
        pretty_print(f"[bold blue]1번 고양이를 선택했습니다![/bold blue]", 
                    border_style="cyan", box_type=box.ROUNDED, 
                    emojis=get_random_emojis(CAT_EMOJIS))
        draw_cat()
    elif number == 2:
        pretty_print(f"[bold orange3]2번 여우를 선택했습니다![/bold orange3]", 
                    border_style="orange3", box_type=box.ROUNDED,
                    emojis=get_random_emojis(FOX_EMOJIS))
        draw_fox()
    elif number == 3:
        pretty_print(f"[bold green]3번 거북이를 선택했습니다![/bold green]", 
                    border_style="green", box_type=box.ROUNDED,
                    emojis=get_random_emojis(TURTLE_EMOJIS))
        draw_turtle()
    else:
        pretty_print(f"[bold red]잘못 입력했습니다. 1, 2, 3 중 하나를 선택해주세요.[/bold red]", 
                    border_style="red", box_type=box.HEAVY,
                    emojis="❌ ❌")

# 메인 프로그램
start_emojis = get_random_emojis(["🎮", "🎯", "🎨", "🎭", "🎪"])
pretty_print(f"[bold yellow]동물 아스키 아트 프로그램[/bold yellow]", 
            border_style="bright_yellow", box_type=box.DOUBLE,
            emojis=start_emojis)

exit_info_emojis = get_random_emojis(["📢", "💡", "🔔"])
pretty_print(f"[bold green]0을 입력하면 종료됩니다. 1-3을 입력하여 동물을 선택하세요![/bold green]", 
            border_style="green", box_type=box.ROUNDED,
            emojis=exit_info_emojis)

while True: # 무한 반복 (계속 참)
    try:
        # 입력 프롬프트를 Rich 스타일로 표시
        menu_emojis = " ".join(random.sample(["🔢", "🎮", "🎯", "👉"], 2))
        n_str = console.input(f"[bold cyan]{menu_emojis} 선택(1-3) 종료(0): [/bold cyan]")
        n = int(n_str) # 여기서 ValueError 발생 가능
    except ValueError:
        error_emojis = get_random_emojis(["❌", "⚠️", "🚫", "⛔"])
        pretty_print(f"[bold red]잘못된 입력입니다. 숫자를 입력해주세요.[/bold red]", 
                    border_style="red", box_type=box.HEAVY,
                    emojis=error_emojis)
        continue # 다시 입력 받기 위해 반복문 처음으로 돌아감

    if n == 0:
        break
    play(n) # play 함수는 1, 2, 3 외의 숫자를 받으면 "잘못입력" 처리

bye_emojis = get_random_emojis(["👋", "🎉", "✨", "💫", "🏆"])
pretty_print(f"[bold red]프로그램을 종료합니다. 다음에 또 만나요![/bold red]", 
            border_style="bright_red", box_type=box.DOUBLE,
            emojis=bye_emojis)

