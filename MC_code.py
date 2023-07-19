import random
inside=0
outside=0
for i in range(0,1000000):
    x=random.random()
    y=random.random()
    if (((x-0.5)**2 +(y-0.5)**2)**(1/2))<=0.5:
        inside=inside+1
    else:
        outside=outside+1
    i=i+1
pi=4*(inside/(inside+outside))
print(pi)
