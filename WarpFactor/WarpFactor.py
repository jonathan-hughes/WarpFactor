'''
Created on Feb 17, 2019

@author: Jonathan Hughes

References:
    Joseph, F. 1975. Starfleet Technical Manual. Ballantine Books
    Sternbach, R., Okuda, M. 1991. Star Trek The Next Generation Technical Manual. Pocket Books
    Sternbach, R., Okuda, M. 1994. Star Trek Voyager Techincal Manual. (Never published.)
    
    Velocity is the cube of warp factor times the speed of light. 

    v = (w^3)*c

Thus: 
    Warp Factor 1 is the speed of light (1.0c)
    Warp Factor 2 is 8 times the speed of light (8.0c)
    Warp Factor 3 is 27 times the speed of light (27.0c)
    etc...    

Later editions have a revised warp scale that is non-linear but this formula is 
sufficiently accurate for our purposes. 

Full impulse is 25% of Warp Factor 1 (0.25c)

'''

# speed of light in m/s
c = 299792458 
metersPerStatute = 1609.34
metersPerNautical = 1852.0
metersPerKilometer = 1000.0
secondsPerHour = 3600
secondsPerMinute = 60
metersPerFoot = 0.3048

# Warp Factor 10 is the maximum theoretical limit for Warp Drive and is unobtainable.
maximumWarpDriveVelocity = c * 10 ** 3

# 100 percent impulse for normal operations is 25% of warp factor 1
impulse100 = c / 4

def InputVelocityInMetersPerSecond():
    
    try:
        inputVelocity = input("Enter velocity in m/s, fpm, mph, kph, or kts and include the units (e.g. ""100 kph""): ")
        validUnits = ['m/s', 'fpm', 'mph', 'kph', 'kts', 'c', 'i']
        
        if not any(unit in inputVelocity.lower() for unit in validUnits):
            raise Exception("A valid unit was not entered!")

        if "fpm" in inputVelocity.lower():
            v = float(inputVelocity[0:inputVelocity.lower().index("fpm")]) * metersPerFoot / secondsPerMinute
        elif "mph" in inputVelocity.lower():
            v = float(inputVelocity[0:inputVelocity.lower().index("mph")]) * metersPerStatute / secondsPerHour
        elif "kph" in inputVelocity.lower():
            v = float(inputVelocity[0:inputVelocity.lower().index("kph")]) * metersPerKilometer / secondsPerHour
        elif "kts" in inputVelocity.lower():
            v = float(inputVelocity[0:inputVelocity.lower().index("kts")]) * metersPerNautical / secondsPerHour
        elif "c" in inputVelocity.lower():
            if inputVelocity.lower().index("c") == 0:
                v = c
            else:
                v = float(inputVelocity[0:inputVelocity.lower().index("c")]) * c
        elif "i" in inputVelocity.lower():
            if inputVelocity.lower().index("i") == 0:
                v = impulse100
            else:
                v = float(inputVelocity[0:inputVelocity.lower().index("i")]) * impulse100
        else:
            v = float(inputVelocity[0:inputVelocity.lower().index("m/s")])
        
        if v >= maximumWarpDriveVelocity:
            raise Exception("Entered velocity exceeds Warp Drive theoretical limits!")
        else:
            print("\nA velocity of " + inputVelocity + " is:\n")            
            return(v)
    
    except Exception as e:
        print("Error: " + str(e))
    

def CalculateWarpFactor(v = None):
    
    if v is None:
        raise Exception("Velocity not specified!")
    
    try:
        if v >= c:
            # Warp factor is the cube root of the ship velocity divided by the speed of light.
            w = (v / c) ** (1 / 3)
        else:
            w = None
            
        return(w) 

    except Exception as e:
        print("Error: " + str(e))
    

def CalculateImpulse(v = None):
    
    if v is None:
        raise Exception("Velocity not specified!")
        
    try:
        # Full impulse for normal operations is 25% the speed of light.
        if v >= c:
            i = None
        else:
            i = (v / impulse100) * 100
        
        return(i) 

    except Exception as e:
        print("Error: " + str(e))
  
    
if __name__ == '__main__':
    v = InputVelocityInMetersPerSecond()
    w = CalculateWarpFactor(v)
    i = CalculateImpulse(v)
    print("Warp Factor: " + str(w))
    if i is not None:
        print("Percent Impulse: " + str(i) + " %")
    else:
        print("Percent Impulse: " + str(i))
    