#generate random numbers using numpy.
import numpy as np

#returns a dictonary 
def assigned(listInputed):
    return {listElement:0.1 * np.random.randint(1,5) for listElement in listInputed}

inputs = ['Alice', 'Mike' ,'Janet', 'Peter','Paolo', 'Esther']
assigned(inputs)