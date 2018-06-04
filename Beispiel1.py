def pruefziffer(code):
    return 98 - (code&97)

    land="AT"
    blz="38282"
    konto= "3026713"


    for i in range(len(konto), 11):
        konto = "0" + konto

    iban = blz+konto+"1029"+"00"
    check = pruefziffer(iban)


    p1 = land + check
    p2 = blz[0:4]
    p3 = blz[4:5]+konto[0:3]
    p4 = konto[3:7]
    p5 =konto[7:11]
    print(p1,p2,p3,p4,p5)
 
    #pruefziffer = blz + konto + "1029"+"00"
    ##pruefziffer%97
 