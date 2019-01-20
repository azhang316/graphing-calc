import math
import numpy as np
import matplotlib.pyplot as plt
eqa = input("What equation do you want to evaluate?")

def dydx (xvals, yvals): #Derivative Function
  deriv = []
  for counter in range(-1,len(yvals)-1):
    try:
      slope = (yvals[counter+1]-yvals[counter])/(xvals[counter+1]-xvals[counter]) #finds slope with y1-y2 / x1-x2 on small interval
      if isinstance(slope, complex):
        deriv.append(None)
      #makes sure it is not imaginary
      else:
        deriv.append(slope)
      #basically just a really small slope calculation
    except:
      deriv.append(None)
      #for when derivative cannot be found
  return deriv

def integrate(a, b, yvals, precision):     #integration function
  summation = 0 #summation starts at zero and accumulates values from a to b
  for counter1 in range (a , b):  #converts the range for the array
    summation += (yvals [counter1] + yvals [counter1 + 1]) / (precision *2) 
    # trapizoidal sum is used here with really small distances
  return summation

numpoints = eval(input("Precision? (datapoints between each number)")) #data points per number
rounding = eval(input("how many decimals to round to?"))
low = int(eval(input("What is the lower bound?"))* numpoints - numpoints) #here, we collect data for the evaluation and graph
high = int(eval(input("What is the upper bound?"))* numpoints + numpoints)
lowY=int(input("What is the lower range?"))
highY=int(input("What is the upper range?"))
plt.grid()
plt.ylim(lowY,highY)
plt.xlim(int(low/numpoints)+1,int(high/numpoints-1))
#creates the outline for the graph
xpoints = [] #empty array for putting x values in
for num in range(low, high): #repeats for different values of x and puts them in an array
  xpoints.append(num / numpoints)

eqa = eqa.replace("sin", "np.sin") #translates rough input into runnable code
eqa = eqa.replace("cos", "np.cos")
eqa = eqa.replace("tan", "np.tan")
eqa = eqa.replace("^", "**")
eqa = eqa.replace("log", "np.log10")
eqa = eqa.replace("ln", "np.log")
eqa = eqa.replace("1x", "1*x") #Makes it so we don't have to input "n*x" for value nx
eqa = eqa.replace("2x", "2*x")
eqa = eqa.replace("3x", "3*x")
eqa = eqa.replace("4x", "4*x")
eqa = eqa.replace("5x", "5*x")
eqa = eqa.replace("6x", "6*x")
eqa = eqa.replace("7x", "7*x")
eqa = eqa.replace("8x", "8*x")
eqa = eqa.replace("9x", "9*x")
eqa = eqa.replace("0x", "0*x")
eqa = eqa.replace("x", "(x)")

values = []

for num in range(low, high): #repeats for different values of x
  x = num/numpoints #input("What is x?")
  new = eqa.replace("x","("+ str(x) + ")")
  try:
    val = eval(new) #save this in datatable. end of loop
    if isinstance(val, complex):
      values.append(None)
    else:
      values.append(val)
  except:
    values.append(None)
    
firstderv = dydx(xpoints, values)
#Creates First Derivative Points
secderv = dydx(xpoints, firstderv)
#Creates Second Derivative Points

counter = low
for val in range(0, high-low-2):
  try:
    print( "(" + str(xpoints[val]) + "," + str(round(values[val], rounding)) + ") " )
  except:
    print( "(" + str(xpoints[val]) + "," + str(values[val]) + ") " )
  try:
    print( "(" + str(xpoints[val]) + "," + str(round(firstderv[val], rounding)) + ")" )
  except:
    print( "(" + str(xpoints[val]) + "," + str(firstderv[val]) + ")" )
  try:
    print( "(" + str(xpoints[val]) + "," + str(round(secderv[val], rounding)) + ")" )
  except:
    print( "(" + str(xpoints[val]) + "," + str(secderv[val]) + ")" )
    
  counter = counter + 1
  
def changesign(first ,second,rounding):  #tests if the two values are different signs ie pos and negative
    try:
        if (first < 10) & (second > -10) and (first > -10) & (second < 10):
            if (round(first,rounding)>0) & (round(second, rounding)<-0) :
                return True
            else:
                return(round(first,rounding)<-0) & (round(second, rounding)>0)
    except:
        first==None or second==None

def findsignchange(xvals, yvals,rounding): #accepts x values and y values to determine which values of x have changes in sign
    signchange = []
    for count in range (1, len(yvals) - 1):
      try:
        if changesign(yvals[count-1], yvals[count+1], rounding): #this additional step is to ensure zeroes are still included
            signchange.append(xvals[count])
      except:
        yvals[count] == none or yvals[count-1] == none or yvals[count+1] == none
    return signchange

  
def findholes(xvals, yvals): #finds the holes of the function values given
  holex = []
  holey = []
  for count in range(1,len(yvals)-1): #for all values except first and last which cant be hole
      try:
          if(yvals[count] == None): #if value is undefined, holes are only at undefined values
              if(yvals[count - 1]- yvals[count + 1] < 1 and yvals[count - 1]- yvals[count + 1] > -1):
        #makes sure right and left values are close to one another
                  holex.append(xvals[count])
                  holey.append( (yvals[count + 1] + yvals[count - 1]) / 2)
        #averages before and after hole to determine estimated value for the hole's y value
      except: 
          yvals[count-1]==None                
  return(holex, holey)

def zero(first ,second): #finds if a value is a zero
  if (first == 0):
    return True
  if (first < 0.1) & (second > -0.1) & (first > -0.1) & (second < 0.1): #makes sure values are close to 0
    if (first>0) & (second<0) : #these three if statements test if change in sign or a zero is there and return true if so. otherwise, default is false
      return True
    if (first<0) & (second>0) :
      return True
    if (first == 0) :
      return True

def findzero (xvals, yvals): #like the findsignchange function, this returns the zeroes of the function values
  vals = []
  for count in range(0,len(yvals)-1):
    try:
      if zero(yvals[count], yvals[count+1]):
        vals.append(xvals[count])
    except:
      vals = vals
  return vals
print('IMPORTANT INFORMATION')
Zeroes = findzero(xpoints, values)
Extrema = findsignchange(xpoints,firstderv,rounding)     #these three utilize functions created above to find arrays for the zeroes, extrema, and poi       
POI = findsignchange(xpoints,secderv,rounding)
try:
    for val in range(0, len(Zeroes)):
        print("Zeroes:",Zeroes[val])
except:
    blah = 1
mins = []
maxs = []
for val in range(0, len(Extrema)):
    if(secderv[int(Extrema[val]*numpoints-low)] > 0):
        mins.append(Extrema[val])
        print("Mins:", Extrema[val])
    else:
        maxs.append(Extrema[val])
        print("Maxs:", Extrema[val])


try:
    for val in range(0, len(POI)):
        print("POI:", POI[val])
except:
    blah = 1
print("Holes:") #this area finds the holes of the function and prints them
holex, holey = findholes(xpoints, values)
for val in range(0, len(holex)):
  print("(" + str(holex[val]) + " , "  + str(round(holey[val], rounding)) + ")")    


plt.plot(xpoints,values,'r',label='Function')
#Plotting Function

plt.plot(xpoints,firstderv, 'b',  label='1st Derivative')
#Plotting First Derivative

plt.plot(xpoints,secderv, 'g',label='2nd Derivative')
#Plotting Second Derivative

try:
    for val in range(0, len(maxs)):
        try:
            maxx=(maxs[val])
            maxy=values[xpoints.index(maxs[val])]
            plt.plot(maxx,maxy,c='m', marker='o')
        except:
          maxs[val] = None
        #Creating Marker for Extrema
except: blah = 1

try:
    for val in range(0, len(mins)):
        try:
            minx=(mins[val])
            miny=values[xpoints.index(mins[val])]
            plt.plot(minx,miny,c='c', marker='o')
        except:
          maxs[val] = None
        #Creating Marker for Extrema
except: blah = 1

try:
    for val in range(0, len(POI)):
        try:
            POIx=POI[val]
            POIy=values[xpoints.index(POI[val])]
            plt.scatter(POIx,POIy, c='g', marker='8')
        #Creating Marker for Points of Inflection
        except:
            POI=False
except: blah = 1
            
try:
    for val in range(low,high):
        try:
            plt.scatter(holex[val],holey[val],c='r', marker='o')
        except:
            Holes=False
except: blah = 1

plt.scatter([],[],c='b', marker='o',label="Extremum")

plt.scatter([],[], c='g', marker='8', label="Inflection Point")

plt.scatter([],[],c='r', marker='o',label="Hole")

plt.legend()
plt.show()


lowlimit = eval(input("What is the lower limit of integration?")) * numpoints
uplimit = eval(input("What is the upper limit of integration?")) * numpoints
if (uplimit > high or lowlimit < low):
  print("invalid limit")
print(round(integrate(lowlimit - low, uplimit - low, values, numpoints), rounding)) 