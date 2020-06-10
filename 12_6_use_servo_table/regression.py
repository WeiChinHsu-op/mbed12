import matplotlib.pyplot as plt
import numpy as np

Ts = 30;   # signal interval
end = 300; # signal end point
n = int(end/Ts)+1;

x = np.linspace(-150, 150, num=n) # signal vector

#TODO: revise this array to your results
y = np.array([-17.305,-17.066,-16.109,-12.839,-6.141,0.000, 6.380, 12.839, 16.189, 17.305, 17.704]) # speed vector

z = np.polyfit(x, y, 2) # Least squares polynomial fit, and return the coefficients.

goal = 8             # if we want to let the servo run at 7 cm/sec
                     # equation : z[0]*x^2 + z[1]*x + z[2] = goal
z[2] -= goal         # z[0]*x^2 + z[1]*x + z[2] - goal = 0

result = np.roots(z) # Return the roots of a polynomial with coefficients given

# output the correct one
if (0 <= result[0]) and (result[0] <= end):
    print(result[0])
else:
    print(result[1])