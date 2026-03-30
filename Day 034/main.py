'''
So we can also make a variable by defining its data type at initial level.
like 👇
'''
from werkzeug.serving import can_fork

# age: int
# name: str
# height: float
# is_human: bool

'''Also we can set data type inside a variable which is inside a function'''
# Ex. ->

def police_check(age: int) -> bool:
    if age >= 18:
        can_drive = True
    else:
        can_drive = False

    return can_drive


print(police_check(18))
