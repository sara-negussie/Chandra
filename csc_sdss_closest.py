import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time


start = time.time() #start a time to see how long it takes


galaxiesFull = pd.read_csv("mag_change.txt", delim_whitespace=True)
sdssRA = galaxiesFull["SDSS_RA"] #right ascention
sdssDEC = galaxiesFull["SDSS_DEC"] #decllination

csc10am= pd.read_csv("CSC21_SDSS_10arcmin_crossmatch.txt", delim_whitespace=True) 
#matches = csc10am['Num']
cscRA  = csc10am['CSC_RA']
cscMyRA = csc10am['SDSS_RA']
cscDEC = csc10am['CSC_DEC']
cscMyDEC = csc10am['SDSS_DEC']


cscMyRAnew = []
cscMyDECnew = []
cscRAnew  = []
cscDECnew = []
angSep = []
idx = 0
count = 0
for i in range(np.size(cscRA)):
    #num = matches[i]
    #if idx == num:
    #    continue
    #else:

        #angular separation
        thetaRad = np.sin(cscMyDEC[i]*np.pi/180)* np.sin(cscDEC[i]*np.pi/180) + np.cos(cscMyDEC[i]*np.pi/180)*np.cos(cscDEC[i]*np.pi/180)*np.cos(np.absolute(cscMyRA[i]-cscRA[i])*np.pi/180) #returns answer in rad
        theta_arcsec = np.arccos(thetaRad) * 206265
        if theta_arcsec < 600:
            cscMyRAnew.append(cscMyRA[i])
            cscMyDECnew.append(cscMyDEC[i])
            cscRAnew.append(cscRA[i])
            cscDECnew.append(cscDEC[i])
            angSep.append(theta_arcsec)         
            count = count +1
        #print("d1 =",cscMyDEC[i], "d2 = ", cscDEC[i], "angSep=", theta_arcsec)       
    #idx = num
        
print("Count =", count)

print("Writing second file...")
with open('CSC21_SDSS_10arcmin_crossmatch.txt','w') as f:
    f.write('Target_Name\t\t\t\tCSC_RA\t\tSDSS_RA\t\tCSC_DEC\t\tSDSS_DEC\n')
    for i in range(np.size(Ccount)):
        #f.write(f'{re.sub(" ","",cat["name"][i])},{cat["ra"][i]},{cat["dec"][i]}\n')
        f.write("%27s\t%12.6f\t%12.6f\t%12.6f\t%12.6f\n" % ( ([i]), (CSC_RA_matches[i]), (SDSS_RA_matches[i]), (CSC_dec_matches[i]), (SDSS_dec_matches[i]) ) )
