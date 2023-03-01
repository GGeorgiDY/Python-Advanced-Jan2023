from pyfiglet import Figlet
import speech_recognition as sr


def get_name(player_number):
    while True:
        # чрез микрофона който програмата ни дава ние го включваме
        with sr.Microphone() as source:
            # включваме разпознаването на гласа
            r = sr.Recognizer()
            print(f"Player {player_number}, say your name")
            # сега ще запишем нашия запис
            audio_data = r.record(source, duration=3)  # микрофона ще е включен за 3 сек
            # подаваме аудиото
            print("Recognizing...")
            try:
                return  r.recognize_google(audio_data)
            except sr.UnknownValueError:
                print("Please say your name again")



def check_for_win():
    player_name, player_symbol = players[0]
    size = len(board)

    # all връща True, ако всичко в скобите[] връща True, иначе връща false
    first_diagonal_win = all([board[x][x] == player_symbol for x in range(size)])
    second_diagonal_win = all([board[x][size - 1 - x] == player_symbol for x in range(size)])

    # ако един ред е True то ще се върне True
    row_win = any([all(True if pos == player_symbol else False for pos in row) for row in board])
    col_win = any([all(True if board[r][c] == player_symbol else False for r in range(size)) for c in range(size)])

    # ако едно от тези е True имаме победител
    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} won!")

        raise SystemExit

    players.append(players.pop(0))


def place_symbol(position):
    row, col = (position - 1) // 3, (position - 1) % 3
    board[row][col] = players[0][1]

    check_for_win()

    print_board()
    choose_position()


def choose_position():
    while True:
        try:
            position = int(input(f" {players[0][0]} choose a free position [1-9]: "))
        except ValueError:
            print(f"{players[0][0]} please select a valid position!")
            continue

        if 1 <= position <= len(board) * len(board):
            place_symbol(int(position))
            break
        else:
            print(f"{players[0][0]} please select a valid position!")


def print_board(begin=False):
    if begin:
        print("This is the numeration of the board:")
        [print(f"| {' | '.join(row)} |") for row in board]
        print(f"{players[0][0]} starts first!")

        # зачистваме дъската
        for row in range(len(board)):
            for col in range(len(board)):
                board[row][col] = " "

    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def start():
    # изписва на конзолата много яко тик-так-тое, като преди това инсталирах pip install pyfiglet==0.7 чрез terminal
    # прозореца отдолу
    figlet = Figlet(font='big',)
    print(figlet.renderText("Tic-Tac-Toe"))

    player_one_name = get_name("one")
    player_two_name = get_name("two")

    while True:
        player_two_symbol = ""
        player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O'? ")

        if player_one_symbol != "X" and player_one_symbol != "O":
            print(f"{player_one_name}, please enter a valid symbol!")

        elif player_one_symbol == "X":
            player_two_symbol = "O"
            break

        elif player_one_symbol == "O":
            player_two_symbol = "X"
            break

    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])
    print_board(begin=True)
    choose_position()


players = []
board = [[str(x), str(x + 1), str(x + 2)] for x in range(1, 10, 3)]

start()



# за да ми разпознае говора инсталирах през терминала pip install SpeechRecognition pydub
# след това инсталирах pip3 install pyaudio, който ни помага да запишем говора, защото без да запишем говора
# другото нещо няма да работи (няма как горната програма да разпознае говора, ако не е записан)