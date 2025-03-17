b = int(input("Your current age: "))
a = int(input("age when you started praying salah: "))

if a==b:
    c = int(input("month no, when you started praying salah : "))
    # 2 months = 30*2 days = 60 days
    days = 30*c

    approx = b-a
    remain=a-approx
        
    print("1. remaining fazir")
    print("2. remaining zohar")
    print("3. remaining asir")
    print("4. remaining magrib")
    print("5. remaining isha")
    my = int(input("select (1-5): "))

    if my==1:
        s = remain*(365+days)
        print(s, "and", s*2, "rakah")

    elif my==2:
        s = remain*(365+days)
        print(s, "and", s*4, "rakah")

    elif my==3:
        s = remain*(365+days)
        print(s, "and", s*4, "rakah")

    elif my==4:
        s = remain*(365+days)
        print(s, "and", s*3, "rakah")

    elif my==5:
        s = remain*(365+days)
        print(s, "and", s*4, "rakah and", s*3, "witr")

    else:
        print("Invalid input") 
    
    
# case 2

else:
    approx = b-a
    remain=a-approx
    
print("1. remaining fazir")
print("2. remaining zohar")
print("3. remaining asir")
print("4. remaining magrib")
print("5. remaining isha")
my = int(input("select (1-5): "))

if my==1:
    s = remain*365
    print(s, "and", s*2, "rakah")

elif my==2:
    s = remain*365
    print(s, "and", s*4, "rakah")

elif my==3:
    s = remain*365
    print(s, "and", s*4, "rakah")

elif my==4:
    s = remain*365
    print(s, "and", s*3, "rakah")

elif my==5:
    s = remain*365
    print(s, "and", s*4, "rakah and", s*3, "witr")

else:
    print("Invalid input")