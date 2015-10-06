while 1 is 1:
    raw_password = raw_input("Type in the password that you would like to check:\n")
    def checkPasswordStrength():
        passwordLength = len(raw_password)
        caps = sum(1 for a in raw_password if a.isupper())
        lower = sum(1 for a in raw_password if a.islower())
        alpha = sum(1 for a in raw_password if not a.isalpha())
        digits = sum(1 for a in raw_password if a.isdigit())
        special = alpha - digits
    
        score = 0

        #length check
        if passwordLength >= 6 and passwordLength <= 11:
            score += 0
        if passwordLength >= 12:
            score += 1

        #caps check
        if caps >= 1 and caps <= 2:
            score += 0
        if caps >= 3 and lower >= 9:
            score += 3
        elif caps >= 3 and lower <= 5:
            score += 1

        #digits check
        if digits >= 1 and digits <= 2:
            score += 1
        if digits >= 3:
            score += 2

        #specialchars check
        if special >= 1 and special <= 2:
            score += 0
        if special >= 3:
            score += 1
        return score

    score = checkPasswordStrength()
    strength = ""
    if score == 0:
        strength = "very weak"
    elif score == 1:
        strength = "weak"
    elif score == 2:
        strength = "medium"
    elif score == 3:
        strength = "strong"
    elif score >= 4:
        strength = "very strong"
    print "\nYour password strength is",strength
