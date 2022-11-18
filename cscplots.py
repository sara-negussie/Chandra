import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time


start = time.time() #start a time to see how long it takes
galaxiesFull = pd.read_csv("mag_change.txt", delim_whitespace=True)
sdssRA = galaxiesFull["SDSS_RA"] #right ascention
sdssDEC = galaxiesFull["SDSS_DEC"] #decllination


#first example
csc10am= pd.read_csv("csc10arcmin.txt", delim_whitespace=True) 
matches = csc10am['Num']
cscRA  = csc10am['CSC_RA']
cscMyRA = csc10am['My_RA']
cscDEC = csc10am['CSC_DEC']
cscMyDEC = csc10am['My_DEC']

"""
fig = plt.figure(figsize =(10, 10))
plt.title("All nearby sources")
plt.scatter(sdssRA, sdssDEC, s = 5, color = 'r', label ='sdss')
plt.scatter(cscRA, cscDEC, s = 5, color = 'b', label = 'csc')
plt.legend()
plt.xlabel("RA")
plt.ylabel("DEC")
#plt.xlim(10,30)
#plt.ylim(10,30)
plt.grid()
plt.show()  
"""

cscMyRAnew = []
cscMyDECnew = []
cscRAnew  = []
cscDECnew = []
angSep = []
idx = 0
count = 0
for i in range(np.size(cscRA)):
    num = matches[i]
    if idx == num:
        continue
    else:

        #angular separation
        thetaRad = np.sin(cscMyDEC[i]*np.pi/180)* np.sin(cscDEC[i]*np.pi/180) + np.cos(cscMyDEC[i]*np.pi/180)*np.cos(cscDEC[i]*np.pi/180)*np.cos(np.absolute(cscMyRA[i]-cscRA[i])*np.pi/180) #returns answer in rad
        theta_arcsec = np.arccos(thetaRad) * 206265
        if theta_arcsec < 15:
            cscMyRAnew.append(cscMyRA[i])
            cscMyDECnew.append(cscMyDEC[i])
            cscRAnew.append(cscRA[i])
            cscDECnew.append(cscDEC[i])
            angSep.append(theta_arcsec)         
            count = count +1
        #print("d1 =",cscMyDEC[i], "d2 = ", cscDEC[i], "angSep=", theta_arcsec)       
    idx = num

print("Count =", count)

#comment out 

print("Writing file")
with open(r'checksdsspics10arcsec.txt', 'w') as fp:
    fp.write("Num\t\t\t\tSDSS_RA\t\t\t\tCSC_RA\t\t\tSDSS_DEC\t\t\tCSC_DEC\t\tAngular_Separation\n")
    for i in range(count):
        fp.write("%3d\t%12.6f\t%12.6f\t%12.6f\t%12.6f\t%12.6f\n" %( (i) ,(cscMyRAnew[i]), (cscRAnew[i]), (cscMyDECnew[i]), (cscDECnew[i]), (angSep[i]) ) )
                 
#comment out


# taking an input list
#uniqueNums = []
# taking an counter
sum = 0
 
# traversing the array
"""
for item in matches:
    if item not in uniqueNums:
        sum += 1
        uniqueNums.append(item)
 """
# printing the output
print("No of unique items are:", sum)
#categories = np.array(len(cscMyRAnew))

# use colormap
#colormap = np.array(['r', 'g', 'b'])

fig = plt.figure(figsize =(15, 10))
plt.title("All nearby sources--using astropy vo 10arcmin")
#plt.scatter(cscMyRAnew, cscMyDECnew, s = 5, c= cscDECnew, label ='sdss')
#plt.scatter(cscRAnew, cscDECnew, s = 5, c = cscDECnew, label = 'csc')
plt.scatter(cscRAnew, cscDECnew, s = 5, color = "coral", label = 'csc')
plt.scatter(cscMyRAnew, cscMyDECnew, s = 5, color = "b", label ='sdss')
plt.legend()
plt.xlabel("RA")
plt.ylabel("DEC")
#plt.xlim(10,30)
#plt.ylim(10,30)
plt.grid()
plt.show()  


#histogram

fig = plt.figure(figsize =(10, 7))

n, bins, patches = plt.hist(x=angSep, bins = 40, color='#0504aa',
                            alpha=0.7, rwidth=0.85)
#plt.grid(axis='y', alpha=0.75)
plt.xlabel('Theta in arcsec')
plt.ylabel('Count')
plt.title('Angular Separation from astropy vo 10arcmin')
#plt.axvline(2.6, color='k', linestyle='dashed', linewidth=1)

plt.show()  

print("finished")
print(f'Numpy: {time.time() - start} seconds')
