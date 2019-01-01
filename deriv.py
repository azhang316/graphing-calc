def dydx (xvals, yvals):
  deriv = []
  for counter in range(0,len(xvals)-1):
    deriv.append((yvals[counter+1]-yvals[counter])/(xvals[counter+1]-xvals[counter]))
    print("(" + str(xvals[counter]) + "," + str(deriv[counter]) + ")")
  return deriv
  
xvals = range(-1000,1000)
yvals = range(-1000,1000)
firstderv = dydx(xvals, yvals)

for counter in range(0, len(firstderv)):
  print ("(" + str(counter) + " , " + str(firstderv[counter]) + ")")