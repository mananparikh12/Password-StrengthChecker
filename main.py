from checker import check_password, get_rating
from generator import make_strong_password

print("=== Password Strength Checker ===")
print("Enter the app name and its password.")
print("Type 'done' as the app name when you finish.\n")

saved = {}   

while True:
    app = input("App name (or 'done'): ").strip()

    if app.lower() == "done":
        break
    if app == "":
        print("App name cannot be empty.\n")
        continue

    password = input("Password for " + app + ": ")
    if password == "":
        print("Password cannot be empty.\n")
        continue

    score, tips = check_password(password)
    print("\nStrength:", get_rating(score), "(" + str(score) + "/6)")

    if len(tips) == 0:
        print("Great password! Nothing to improve.")
    else:
        print("How to improve:")
        for tip in tips:
            print(" -", tip)
    print()

    saved[app] = password

print("\n=== Reuse Check ===")

if len(saved) == 0:
    print("No passwords entered.")
else:
    used_in = {}   
    for app in saved:
        pw = saved[app]
        if pw in used_in:
            used_in[pw].append(app)
        else:
            used_in[pw] = [app]

    found_reuse = False
    for pw in used_in:
        apps_list = used_in[pw]
        if len(apps_list) > 1:
            found_reuse = True
            print("\nSame password used in:", ", ".join(apps_list))
            print("If one app gets hacked, hackers can enter all of these!")
            print("Use a different password for each app. Suggestions:")
            for app in apps_list:
                print("  ", app, "->", make_strong_password())

    if not found_reuse:
        print("Good job! All your passwords are unique.")

print("\nStay safe online!")
