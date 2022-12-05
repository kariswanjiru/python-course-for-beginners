import numpy as np
inputs = ['Alice', 'Mike' ,'Janet', 'Peter','Paolo', 'Esther']
dic = {x:0.1 * np.random.randint(1,5) for x in inputs}
print((dic.values() == 2) == True)        

def assigned(listInputed):
    dic = {listElement:0.1 * np.random.randint(1,5) for listElement in listInputed}
    return dic

if dic.values() == 0.2:
    print('hello')
elif dic.values() == 0.3:
    print('world')
else:
    print('Oh yes!')
