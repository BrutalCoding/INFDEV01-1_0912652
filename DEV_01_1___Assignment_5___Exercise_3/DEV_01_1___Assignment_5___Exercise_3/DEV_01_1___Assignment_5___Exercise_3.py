while 1 == 1:
    raw_password = raw_input("Type in the password that needs to get encrypted:\n")
    amount = int(raw_input("Now fill in a random integer:\n"))
    new_password = ""

    while amount > 26 or amount < -26:
        if amount > 26:
            amount -= 26
        elif amount < -26:
            amount += 26

    for a in raw_password:
        if a.isalpha():
            old_ascii = ord(a)
            new_ascii = old_ascii + amount
            if a.islower():
                if new_ascii > 122:
                    diff = new_ascii - 122
                    new_ascii = 96 + diff
                elif new_ascii < 97:
                    diff =  97 - new_ascii
                    new_ascii = 123 - diff
            else:
                if new_ascii > 90:
                    diff = new_ascii + 90
                    new_ascii = 64 + diff
                elif new_ascii < 65:
                    diff = 65 - new_ascii
                    new_ascii = 91 - diff
            new_password += chr(new_ascii)
        else:
            new_password += a
    print "New password:",new_password,"\n"
