print("\n \nWhat's the type of picture you want the caption for ?" )
print("Enter se [If it's a selfie]")
print("Enter sp [If it's a potrait featuring only you]")
print("Enter op [If it's a potrait with a group or anything you love]")
picType= input()


# def picSelection():
   
#     if(picType.lower=="se"):
#         picChoice="Happiness ^_^"
#         flag=flag+1
#     elif(picType.lower=="sp"):
#         picChoice="Swag :)"
#         flag=flag+1
#     elif(picType.lower=="po"):
#         picChoice="Funny/Cool"
        
#     else:
#         print("Your selection does not match our options.\n Please TRY Again")
#         flag=-1

# trial1= picSelection()
# if(flag==1):
#     print(f"Based on the type of photo we suggest {picChoice} as the theme of your caption  ")   
# else:
#     trial2=picSelection()

type1="se"#selfie
type2="sp"#single potralit
type3="op"#other potrait
flag=0
if(picType.lower()==type1):
   print("Based on the type of photo your caption must depict happiness ")
   flag=1
elif(picType.lower()==type2):
    print("Based on the type of photo your caption must depict swag ")
    flag=2
elif(picType.lower()==type3):
    print("Based on the type of photo your caption must be funny/relatable ")
    flag=3
else:
    print('No match')
        
if (picType!=type1 and picType!=type2 and picType!=type3):
    print("Your selection does not match our options.")
    exit(0)

'''if picChoice==1:
    print("Based on the type of photo your caption must depict happiness ")
elif picChoice==2:
    print("Based on the type of photo your caption must depict swag ")
else:
    print("Based on the type of photo your caption must be funny/relatable ")'''

print("\n")
print("Do yout want to go with our suggestion ?\nEnter YES if you do or enter NEXT if you want to choose the theme")
picTheme=str(input())

# write quotes
happiness=['1 Do more of what makes you happy','2 Enjoy life as it is',"3 Bringing the sun wherever I go","4 DO more of what makes you happy","5 Happiess makes you glow better","6 Happy thoughts happy life","7 Happy people are always beautiful","Miles of smiles"]
swag=["1 Be happy ,it drives people crazy",'2 Dream without fear love without limits','3 Born to stand out','4 I play life like a pro!','5 Something big is happenning soon !!',"6 Love me or hate me either way I'm gonna shine",'7 Embrase the glorious mess that you are']
funny=["1 Weekend, please don't leave me","2 All I need is coffee","3 Confidence level:Selfie with no filter",'4 Brains are awesome. I wish everybody would have one!',"5 Did it for the memories – totally worth it!","6 When nothing goes right, go left.","7 I am not lazy, I am just on save energy mode.","8 Always classy, never trashy, and a little bit sassy."]








# fix it the condition is not working....says list obj is not callable

if(picTheme.lower()=="yes"):
    if flag==1:
        # for i in range(len(happiness)):
        joined_string = "\n".join(happiness)
        print(joined_string)
        
    elif flag==2:
        joined_string = "\n".join(swag)
        print(joined_string)                                                    # for i in range(len(swag)):
                                                             # print(swag)
    else:
        # joined_string = "\n".join(happiness)
        print("\n".join(funny))
elif(picTheme.lower()=="no"):
   
    userChoice=input("Choose the caption theme from the options\n      HAPPY , COOL , SWAG : ")
    if userChoice.lower()=="happy":
        print("\n".join(happiness))
    elif userChoice.lower()=='swag':
        print("\n".join(swag))
    elif userChoice.lower()=='cool':
        print("\n".join(funny))
else:
    print("Your choice does not match")

    
# do add comments and say what each line does