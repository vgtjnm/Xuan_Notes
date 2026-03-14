#first step if else elif

xm_age=25
if xm_age > 18:
    print("xm,You not a child")

ame_age=29
if ame_age < 18:
    print("ame,you are a child")
else:
    print("ame,you are not a child")

xiao8_age=38
if xiao8_age < 18:
    print("xiao8,you are a child")
elif xiao8_age <30:
    print("xiao8,you can go dota2")
else:
    print("what??????????")

#second step boolean logic

is_hot=True
is_sunny=False
is_rainy=True

print("")
if is_hot and is_sunny:
    print("let's go!")
if is_hot and not is_rainy:
    print("let's go!")
if is_sunny or not is_rainy:
    print("let's go!")
if is_rainy:
    print("what the hell!")

#third step little project

age=int(input("what is your age?"))
if age < 18:
    print("you are a young boy")
elif age < 35:
    print("you are a mid man")
else:
    print("you are too old!")