import math
import numpy
import matplotlib.pyplot as plt
import random

area_of_rectangle=4
x_cord=numpy.linspace(0,99999,100000)
y_cord=numpy.linspace(0,99999,100000)
radius=1
plt_speed=0.01
count=0
count_inside_circle=0
print(x_cord)

for x in range(0,len(x_cord)):
    x_cord[x]=math.cos(x_cord[x])
for x in range(0,len(y_cord)):
    y_cord[x]=math.sin(y_cord[x])    
plt.axis([0, 2, 0, 2])    
plt.plot(x_cord+1,y_cord+1, ',')

for x in range(0,10000):
 random_x=random.random()*2
 random_y=random.random()*2
 plt.scatter(random_x,random_y)

 distance_from_center= math.sqrt((random_x-1)**2+(random_y-1)**2)
 count=count+1
 if distance_from_center <= radius:
     count_inside_circle=count_inside_circle+1
    
 ratio=count_inside_circle/(count)       
 pi_approximation=round(area_of_rectangle*(ratio),4)  
 plt.pause(0.2)
 str_pi_approx=str(pi_approximation)
 str_inside_circle=str(count_inside_circle)
 plt.title("Pi appproximation: " + str_pi_approx + "\n dots inside circle : " + str_inside_circle )
 
plt.show()

 
print(pi_approximation)



