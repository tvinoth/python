import statistics
import ownmodule

x,y	=	ownmodule.test()	
print(y)

example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]
print(example_list)
x = statistics.mean(example_list)
print(x)

y = statistics.median(example_list)
print(y)

z = statistics.mode(example_list)
print(z)

a = statistics.stdev(example_list)
print(a)

b = statistics.variance(example_list)
print(b)