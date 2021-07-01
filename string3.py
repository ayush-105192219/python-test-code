simple = '012345678'
#simple[0] = '9'  | TypeError: 'str' object does not support item assignment
simple = 'abcdefgh' #valid
#simple = simple + 100 | TypeError: can only concatenate str (not "int") to str
simple = simple + '100'
print(simple)  #output:abcdefgh100