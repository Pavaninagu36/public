#distance b/w two points on earth
#distance=6371.01*arccos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2))
#radians which converts from degress to radians
import math
t_1=int(input("enter a number in degress for t_1: "))
t_2=int(input("enter a number in degress for t_2: "))
g_1=int(input("enter a number for g1: "))
g_2=int(input("enter a number for g2: "))
Distance=6371.01*math.acos(math.sin(t_1)*math.sin(t_2)+math.cos(t_1)*math.cos(t_1)*math.cos(g_1-g_2))
print("The distance is%.2fkm.",Distance)
