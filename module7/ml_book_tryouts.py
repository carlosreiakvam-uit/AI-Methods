import numpy as np

stringLength = 5
popSize = 4

pop = np.random.rand(popSize, stringLength)
pop = np.where(pop < 0.5, 0, 1)
# print(pop)

a = np.ndarray([1, 10, 100])
b = np.ndarray([5, 6, 7])

c = np.kron([1,2,3],[4,5,6])
print(c)

