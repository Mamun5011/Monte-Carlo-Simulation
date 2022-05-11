
import numpy as np
import random
DAYLIMIT = 100


def findDistance( mosquito_X,  mosquito_Y,  host_X,  host_Y):

    X1 = host_X - mosquito_X;
    X1=X1*X1;
    Y1 = host_Y - mosquito_Y;
    Y1=Y1*Y1;
    ans = np.sqrt(X1+Y1);
    return ans;




moveCount=0
inSideCircleDeath=0
outSideCircleDeath=0
numberOfRuns=3000
foundHost=0
days=np.zeros(101)
mosquito_X=0
mosquito_Y=0

host_X = input ("Enter the host  X Co-Ordinate :")
host_X = int(host_X)
host_Y = input ("Enter the host  X Co-Ordinate :")
host_Y = int(host_Y)



for i in range(1,numberOfRuns):

  day=1;
  mosquito_X=0;
  mosquito_Y=0;

  while(day<=DAYLIMIT):

      # choosing the direction of the mosquito and move 250 m
      randNum = random.uniform(0, 1);
      if(randNum<=.25):
        mosquito_X+=250;
      elif(randNum<=.50):
        mosquito_Y+=250;
      elif(randNum<=.75):
        mosquito_X-=250;
      else:
          mosquito_Y-=250;

      moveCount+=1

      # Mosquito smells a host within the range of 50m of the host

      if(findDistance(mosquito_X,mosquito_Y,host_X,host_Y)<=50):
      
          foundHost+=1
          days[day]+=1;
          break;
      
      # Mosquito does not find the host at this move
      else:
          day+=1

  # Mosquito does not find a host within 10 days, so she dies
  if(day>DAYLIMIT):

      if(findDistance(mosquito_X,mosquito_Y,0,0)>1000):
        outSideCircleDeath+=1
      else:
            inSideCircleDeath+=1




print("Total number of runs: ",numberOfRuns)
print("The probability that the mosquito will find the host before she dies: ",foundHost/numberOfRuns)
print("The probability that the mosquito will die outside the red region: ",outSideCircleDeath/numberOfRuns)
print("outSideCircleDeath",outSideCircleDeath,"  inSideCircleDeath ",inSideCircleDeath,"  foundhost ",foundHost)

x=[]
y=[]

for i in range(1,101):
    #print("Day: ",i,": ",days[i]/numberOfRuns)
    if(i%5==0):
      x.append(i)
      y.append(days[i]/numberOfRuns)


import matplotlib.pyplot as plt

plt.plot(x, y)

plt.xlabel('Days')

plt.ylabel('Probability of insects find the host')

#plt.title('Monti Carlo Mosquito')

plt.show()

