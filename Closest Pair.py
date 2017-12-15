# Find closest pair points by Divide And Conquer (DAC) approach

import matplotlib.pyplot as plt
import math

def ecldist(x, y):
    return math.sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def closestpair(xP, yP):
    if(len(xP) < 2):
        return float('inf'), (xP, xP)
    elif(len(xP) < 3):
        return ecldist(xP[0], xP[1]), (xP[0], xP[1])
    else:
        mid = len(xP) // 2
        xL = xP[:mid]
        xR = xP[mid:]
        xM = xP[mid][0]
        
        yL = []
        yR = []
        
        for p in yP:
            if (p in xL):
                yL.append(p)
            else:
                yR.append(p)

        (dL, pairL) = closestpair(xL, yL)
        (dR, pairR) = closestpair(xR, yR)       
        
        if (dL < dR):
            (dmin, pairMin) = (dL, pairL)
        else:
            (dmin, pairMin) = (dR, pairR)
        
        yS = []
        
        for p in yP:
            if((abs(p[0]) - xM) < dmin):
                yS.append(p)
        
        (closest, closestPair) = (dmin, pairMin)
        
        # yS Sorted doesn't have a meaning since you are using brute force   
             
        if(len(yS) >= 2):
            for i in range(len(yS) - 1):
                k = i + 1
                while((k < len(yS)) and (yS[k][1] - yS[i][1] < dmin)):# for every ith element we taking dmin from from all other elements above it 
                    if(ecldist(yS[k], yS[i]) < closest):
                        (closest, closestPair) = (ecldist(yS[k], yS[i]), (yS[k], yS[i]))
                    k+=1    
        
        return closest, closestPair
        
lst = [(5,5),(4,7),(4,10),(4,13),(6,8),(6,14),(7,7),(7,11),(8,5),(8,13),(9,9),
       (10,4),(10,6),(10,12),(10,14),(11,8),(11,10),(12,6),(12,13),(13,8)]
       
xP = sorted(lst, key=lambda x:x[0]) # xP is P(1) .. P(N) sorted by x coordinate
yP = sorted(lst, key=lambda y:y[1]) # yP is P(1) .. P(N) sorted by y coordinate
(x,y) = closestpair(xP,yP)
print('\n')
print('Min Dist = ')
print(x)
print('Pair = ')
print(y)

plt.plot([5,4,4,4,6,6,7,7,8,8,9,10,10,10,10,11,11,12,12,13],
         [5,7,10,13,8,14,7,11,5,13,9,4,6,12,14,8,10,6,13,8], 'ro')
plt.plot((y[0][0],y[1][0]),(y[0][1],y[1][1]),'bo-')
plt.axis([0, 15, 0, 15])
plt.show()