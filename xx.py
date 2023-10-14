import random
def guess_number():
    random.seed(125)
    true_num = random.randint(0,101)
    user_num=-1
    count = 0
    while true_num != user_num:
        user_num = input("Please input:")
        if not user_num.isnumeric():
            print("Please input integer!")
        else:
            user_num=int(user_num)
            if true_num > user_num:
                print("Too small!")
            elif true_num < user_num:
                print("Too big!")
        count += 1
    print("%d times,you got it!" % (count-1))
guess_number()
