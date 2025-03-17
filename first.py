print("Student percentage calculater")

# percentage portal

totalmarks = float(input("Enter total marks:"))
obtainedmarks = float(input("Enter obtained marks:"))
percentage = round(obtainedmarks / totalmarks * 100) 
critical = 35
if percentage >= critical:
    print("you passed with", percentage,"%")
else:
    print("you failed with", percentage,"%")

# college applications

clg = float(input("Enter your percentage:"))

if clg != percentage:
    print("incorrect percentage")

else:    

# portal for tier 3 college
    if  35<= clg <=60:
        print("you will get tier 3 college ")

        print("tier 3 college: aps college (23) , sumaya college(34) , srv college(12)")
        t = float(input("Enter teir 3 college no:"))
        aps= 23
        sumaya= 34
        srv= 12

        if t==aps:
            print("you are now admitted into aps college")
        elif t==srv:
            print("you are now admitted into srv college")

        elif t==sumaya:
            print("you are now admitted into sumaya ")
            
# portal for teir 2 college

    elif 61<= clg <=80:
        print("you will get tier 2 college ")
    
        print("tier 2 colleges: sfp college (64) , iiser college(51) , CMI college(78)")
        s = float(input("Enter teir 2 college no:"))
        sfp= 64
        iiser= 51
        cmi= 78

        if s==sfp:
            print("you are now admitted into sfp college")

        elif s==iiser:
            print("you are now admitted into iiser college")

        elif s==cmi:
            print("you are now admitted into CMI ")


    elif clg < 35:
        print("please reattempt the exam you got failed with", clg,"%")



# portal for tier 1 college
    elif 81<= clg <=100:

        
        print("you will get tier 1 college")

        print("tier 1 college: iisc college (64) , vit college(40) , bits college(87)")
        u = float(input("Enter teir 1 college no:"))
        iisc= 64
        vit= 40
        bits=87

        if u==iisc:
            print("you are now admitted into iisc college")
        elif u==vit:
            print("you are now admitted into vit college")

        elif u==bits:
            print("you are now admitted into bits college")


