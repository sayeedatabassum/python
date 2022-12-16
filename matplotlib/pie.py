import matplotlib.pyplot as mp

labels = ['java','python','c++','c']
colors = ['yellow','blue','green','pink']
size = [270,200,150,50]

#chop
explode=[0.3,0.1,0.2,0.2]

mp.pie(size,labels=labels,colors=colors,explode=explode)
mp.title('pie chart')
# mp.legend
mp.show()