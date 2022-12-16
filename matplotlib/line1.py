#using line graph plot the data of 2 students a/c to their sem percentage

import matplotlib.pyplot as mp

x1 = [1, 2, 3, 4, 5, 6, 7, 8]
y1 = [89, 76, 92, 64, 57, 78, 99, 94]

x2 = [1, 2, 3, 4, 5, 6, 7, 8 ]
y2 = [78, 81, 98, 82, 56, 86, 74, 65]

mp.plot(x1, y1, color='red')
mp.plot(x2, y2, color='yellow')

mp.title('line graph')
mp.xlabel('x-axis')
mp.ylabel('y-axis')
mp.show()
