def countdown_to_one(n):
    if n == 0:
        return 
    print(n)
    countdown_to_one(n - 1) # recursive call and moving towards a "base case"

countdown_to_one(5)

'''
recursive sum 
build a structure to work from the inside out
'''

def sum_list(items):
    if len(items) == 1:
        return items[0]
    else:
        return items[0] + sum_list(items[1:])

'''
0! = 1
1! = 1
2! = 2 * 1
3! = 3 * 2 * 1
4! = 4 * 3* 2 * 1
5! = 5 * 3 * 2 * 1

refactored
0! =1
1! =1
2! = 2 * 1!
3! = 3 * 2!

n
'''
'''
recursive factorial
'''

# def recursive_factorial(n):
#     if n == 1:
#         return 1
#         else:
#             return 


'''
SPRINT CHALLENGE HELP
'''

def count_st(word):
    # base case
    if len(word) < 2:
        return 0 # there can't be a match cuz we are looking for 2 letters
    else:
        if word[:2] == "st":
            return 1 + count_st(word[2:])
        else:
            return count_st(word[1:])



    # recursive case


print("count", count_st("stepstool")) # expect two