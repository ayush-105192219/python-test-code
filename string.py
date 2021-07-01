print(type('this is a string')) #output:<class 'str'>
name = 'Ayush'
longstring = '''
WOW
0 0 
---
'''
print(longstring)

fullname = name + '''

''' + longstring #string concatenation | or name + ' ' longstring | 
print(fullname)
# output:
# WOW
# 0 0
# ---

# Ayush


# WOW
# 0 0
# ---


print(name + 5) #TypeError: can only concatenate string