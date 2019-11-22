import operation
import random

operation.click(900, 1360, 1+random.random())
operation.click(900, 1870, 1+random.random())
operation.click(470, 540, 3+random.random())
operation.click(350, 250, 2+random.random())
operation.swipe(1505, 1016,3+random.random())
for i in range(39):
    operation.swipe(1850, 260, 3+random.random())
operation.home()



