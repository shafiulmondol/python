email = input("Enter your email: ")
i, j, k, m = 0, 0, 0, 0

if len(email) > 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            if email[-4] == "." or email[-3] == ".":  # Check if dot is at correct position (e.g., ".com" or ".co")
                for ch in email:
                    if ch.isspace():
                        k = 1
                    elif ch.isalpha():
                        if ch == ch.upper():
                            j = 1
                    elif ch.isdigit():  # Ensure digits are allowed
                        continue
                    elif ch == "_" or ch == "@" or ch == ".":  # Allow underscore, @, and dot
                        continue
                    else:
                        i = 1
                if j == 1 or k == 1 or i == 1:
                    print("Wrong email.")
                else:
                    print("Valid email.")
            else:
                print("Wrong email. Your '.' is not set in the appropriate position or is missing.")
        else:
            print("Wrong email. Your '@' character is missing or appears more than once.")
    else:
        print("Wrong email. Your email's first character must be a letter.")
else:
    print("Wrong email. Your email is shorter than 6 characters.")
