def hello(name='name', age=0):
   # return f"Hello {name}, you are {age} years old"
    string = "Hello {}, you are {} years old"
    return string.format(name, age)


sentenceNoParams = hello()
print('No Params: ' + sentenceNoParams)

sentenceParams = hello('Stewart', 34)
print('With Params: ' + sentenceParams)

def triplePrint(word):
    print(word*3)


triplePrint("hello")