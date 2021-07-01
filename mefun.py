quote = "to be or not to be"
print(quote.upper())  #output:TO BE OR NOT TO BE
print(quote.capitalize())   #output:To be or not to be
print(quote.find('be')) #output:3
print(quote.replace("be" , "me"))       #output:to me or not to me
print(quote)        #output:to be or not to be  |  because string is immutable
quote = quote.replace("be" , "me")
print(quote)    #output:to me or not to me