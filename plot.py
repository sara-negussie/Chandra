import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import decimal

#truncate function
def trunc(values, decimals=0):
    return np.trunc(values*10**decimals)/(10**decimals)

galaxiesFull = pd.read_csv("galaxies_full.csv", sep = ',')  
raGalaxies = galaxiesFull["RA(deg)"] #right ascention
decGalaxies = galaxiesFull["DEC(deg)"] #decllination
bestMag = galaxiesFull["Best Mag"]

sdss = pd.read_csv("allMagsSDSS.csv", sep = ',') #to 1degree radius
obsID = sdss["objid"] 
myRA = sdss["myRA"] 
myDEC = sdss["myDEC"] 
sdssRA = sdss["SDSS_RA"] 
sdssDEC = sdss["SDSS_DEC"] 
sdssPetroMag_g = sdss['petroMag_g']
#print(sdssPetroMag_g)
#print(myRA)
#print(sdssRA)


#reorder array
newArray = [] 
for i in range(np.size(myRA)):
    #d_RA = decimal.Decimal(sdssRA[i])
    #decimals = d_RA.as_tuple().exponent
    decimals = len(str(sdssRA[i]).split(".")[1])
    tmp1 = np.where( trunc(myRA,decimals=3) ==  trunc(sdssRA[i],decimals=3) ) 
    #print(tmp1)
    #d_DEC = decimal.Decimal(sdssDEC[i])
    #decimals = d_DEC.as_tuple().exponent
    decimals = len(str(sdssDEC[i]).split(".")[1])
    tmp2 = np.where( trunc(myDEC,decimals=3) ==  trunc(sdssDEC[i],decimals=3) ) 
    #print(tmp2)
    resultArray = (np.intersect1d(tmp1, tmp2))
    print(resultArray)
    if np.size(resultArray) ==0: 
                continue
    else: 
            for j in resultArray:
                newArray.append(sdssPetroMag_g[j])
                #print(j)
    #print(sdssPetroMag_g[resultArray])
    
    #

#a =trunc(myRA,decimals=4)
#print(a)
#Plotting Best Mag vs Petro Mag g
#print(np.size(newArray))

print("Writing file")

with open(r'checkra&dec.txt', 'w') as fp:
    fp.write("Best_Mag\tPetro_Mag_g\tDifference\tMy_RA\tCSC_RA\tMy_DEC\tCSC_DEC\n")
    for j in range(np.size(newArray)):
        fp.write("%d\t%d\t%d\t%d\t%d\t%d\t%d\n" %( (bestMag[i]), (sdssPetroMag_g[i]), (np.fabs(bestMag[i]-sdssPetroMag_g[i])), (sdssRA[i]), (myRA[j]), (sdssDEC[i]), (decGalaxies[j]) ) )


plt.scatter(newArray, bestMag[0:np.size(newArray)], s = 5)
plt.xlabel("PetroMag_g")
plt.ylabel("Best Mag")
plt.xlim(10,30)
plt.ylim(10,30)
plt.grid()
plt.show()  
