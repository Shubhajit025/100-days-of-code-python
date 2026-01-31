import random
import maths


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])


'''
1. Breakpoint - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are). 
This line will be where the program pauses during debug run.
'''

'''
2. Step Over - This button will go through the execution of your 
code line by line and allow you to view the intermediate values of your variables.
'''

'''
3. Step Into - This will enter into any other modules that your code references. e.g. If you use a function from the random `module` it will 
show you the original code for that function so you can better understand its functionality and how it relates to your problems.
'''

'''
4. Step Into My Code - This does the same thing as Step Into, but it limits the scope to your own project code and 
ignores library code such as random.
'''

