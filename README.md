# Password Strength Checker

## About the Project
This is a small Python project I made for my cyber security course.
It checks how strong a password is and tells the user how to make it
better. The user can enter passwords for different apps, and the
program warns if the same password is used in more than one app.
If a password is reused, it also suggests new strong passwords.

I made this because a lot of people use weak passwords like
"password123" or use one password everywhere. If one account gets
hacked, all the other accounts are in danger too.

## Features
- Checks password strength and gives a score out of 6
- Shows a rating: WEAK, MEDIUM, STRONG or VERY STRONG
- Gives tips on how to improve the password
- Finds common passwords like "123456" and "qwerty"
- Finds easy patterns like "abc" or "123" and repeated letters like "aaa"
- Takes passwords for many apps in one run
- Warns if the same password is used in more than one app
- Suggests random strong passwords
- Checks for empty input

## Technologies Used
- Python 3
- `string` module (for letters, digits)
- `secrets` module (to make safe random passwords)
- `unittest` (for testing)
- Git and GitHub (for version control)

## Project Structure
password_checker/
├── main.py
├── checker.py
├── rating.py
├── generator.py
├── reuse_checker.py
├── validator.py
├── logger.py
├── common_passwords.txt
├── tests/
│ ├── test_checker.py
│ ├── test_generator.py
│ └── test_reuse.py
├── README.md
└── statement.md


## How to Install and Run
1. Install Python 3 from python.org if you don't have it.
2. Download or clone this project:
git clone <your-repo-link>
3. Open a terminal in the project folder:
cd password_checker
4. Run the program:
python password_checker.py
5. Type the app name and its password. Type `done` as the app
   name when you are finished.

No extra libraries are needed. Everything used comes with Python.

## How to Use
Example:App name (or 'done'): instagram
Password for instagram: hello123

Strength: WEAK (2/6)
How to improve:

Too short! Use at least 8 characters (12 or more is better).
Add at least one UPPERCASE letter.
Add at least one special character like ! @ # $ %

## How to Test
Run all the tests from the main project folder:
python -m unittest discover tests

The tests check things like:
- Common passwords get a score of 0
- Strong passwords get a high score
- Same passwords in different apps are found
- The generator makes passwords of the right length

## Screenshots
(Add your screenshots here)

1. Weak password result: ![Weak Password Result](Weak_Password.png)
2. Strong password result: ![Strong Password Result](Strong_Password.png)
3. Reuse warning: ![Reuse Warning](Reuse.png)

## Limitations
- It works only in the terminal, there is no GUI
- It does not check passwords against real hacked-password lists
- Passwords are not saved after the program closes

## Future Improvements
- Add a simple GUI
- Check passwords with a bigger common-password list
- Save a report of the results (without the actual passwords)

## Author
Manan Parikh
Registration Number-26BCY10078