#whatsapp
whatsapp=input("do u want to open whatsapp in ur phone")
if whatsapp=="yes":
    print("download from play store")
    number=int(input("enter ur no. which u want to open whatsapp"))
    if number>=7051344816 and number<=8493049492:
        print("connecting")
        country=input("enter ur country")
        if country>="india":
            print("whatsapp open")
        else:
            print("verifing")
    else:
        print("not connecting")        
else:
    print("download failed")