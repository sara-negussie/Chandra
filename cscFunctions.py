#here are all the functions I will use

def test(x):
    print("This is a test and x = ", x)

"""
def angular_separation(cscMyRA, cscMyDEC, cscMyDEC, csc )

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

print("Count =", count)"""