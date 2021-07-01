abc = 'hello world'
# [start:stop:stepover]
print(abc[-1])    #output:d
print(abc[6])    #output:w  |start from 6 all upto the end 
print(abc[6:11]) #output:world 
print(abc[6:11:2]) #output:wrd    
print(abc[1:])   #output:ello world  |start from 1 all upto the end 
print(abc[:3])   #output:hel
print(abc[::2])    #output:hlowrd
print(abc[::-1])    #output:dlrow olleh | reversing string
print(len('he1010101010101010101010101010100000001010101000000'))  #output:51  | len() is a buildin function
print(abc[0:len(abc)]) #output:hello world | work same as default