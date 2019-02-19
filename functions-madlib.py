# import "madlib_def" module

import madlib_def

while True:
    user_name = input("What is your name? ")
    user_subj = input("What is your fav subj? ")

    # print("your name is %s and your fav subj is %s" % (user_name, user_subj))

    # print(make_madlib(user_name, user_subj))
    print(madlib_def.make_madlib(user_name, user_subj))