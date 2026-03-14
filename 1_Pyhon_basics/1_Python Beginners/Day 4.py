#first step while loop

i=5
while i:
    print(i)
    i-=1

a=5
while a>0:
    print(a)
    a-=1

#second step continue and break

answer=55

while True:
    reply=int(input("guess the answer"))
    if reply > answer:
        print("lower")
        continue
    elif reply < answer:
        print("higher")
        continue
    print("Congratulations!")
    print("You win the one hundred dollars")
    break

