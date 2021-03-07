# Máy tính sẽ chọn ra 1 số ngẫu nhiên trong khoảng từ 1 tới 100
# Người chơi được phép đoán sai tối đa 7 lần
# Mỗi lần đoán sai, máy tính sẽ trả về thông báo rằng số đoán sai lớn hơn hay nhỏ hơn số ngẫu nhiên được chọn
# Và thông báo người chơi còn bao nhiêu lần đoán sai nữa
# Trò chơi kết thúc khi người chơi đoán đúng
from random import randrange

while True:
    # Generate a random number in [1,100]
    mysNumber = randrange(1, 100)
    print(mysNumber)
    # Interface to user
    print("-" * 60)
    print("Guessing number game")
    print("-" * 60)
    wrongGuess = 0
    maxGuess = 7
    while wrongGuess < maxGuess:
        x = int(input("Input your guess: "))
        if x is not mysNumber:
            wrongGuess += 1
            if x > mysNumber:
                print("The number you guessed is greater than the mysterious number!")
            else:
                print("The number you guessed is lower than the mysterious number!")
            print("You have {0} times to guess".format(maxGuess - wrongGuess))
        else:
            print("Good job!")
            break
    s = input("Continue? (y,n)? ")
    if s == "n":
        print("Goodbye!")
        exit()




