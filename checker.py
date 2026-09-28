def load_common_passwords():
    try:
        with open("common_passwords.txt", "r") as f:
            return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        # Fallback list if the text file is missing
        return ["password", "123456", "12345678", "qwerty"]

def check_password(password):
    score = 0
    tips = []
    common_passwords = load_common_passwords()

    if password.lower() in common_passwords:
        tips.append("This is a very common password. Hackers try these first! Change it fully.")
        return 0, tips

    if len(password) >= 12:
        score = score + 2
    elif len(password) >= 8:
        score = score + 1
        tips.append("Make it at least 12 characters long.")
    else:
        tips.append("Too short! Use at least 8 characters (12 or more is better).")

    has_upper = has_lower = has_digit = has_special = False

    for ch in password:
        if ch.isupper(): has_upper = True
        elif ch.islower(): has_lower = True
        elif ch.isdigit(): has_digit = True
        else: has_special = True

    if has_upper: score = score + 1
    else: tips.append("Add at least one UPPERCASE letter.")

    if has_lower: score = score + 1
    else: tips.append("Add at least one lowercase letter.")

    if has_digit: score = score + 1
    else: tips.append("Add at least one number.")

    if has_special: score = score + 1
    else: tips.append("Add at least one special character like ! @ # $ %")

    for i in range(len(password) - 2):
        if password[i] == password[i + 1] and password[i] == password[i + 2]:
            score = score - 1
            tips.append("Avoid repeating the same character 3 times in a row (like 'aaa').")
            break

    easy_patterns = ["123", "234", "345", "456", "567", "678", "789", "abc", "bcd", "cde", "qwe", "asd"]
    for pattern in easy_patterns:
        if pattern in password.lower():
            score = score - 1
            tips.append("Avoid easy patterns like '123' or 'abc'.")
            break

    if score < 0:
        score = 0

    return score, tips

def get_rating(score):
    if score <= 2: return "WEAK"
    elif score <= 4: return "MEDIUM"
    elif score == 5: return "STRONG"
    else: return "VERY STRONG"
