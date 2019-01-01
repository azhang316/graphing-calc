def zero(first,second):
  if first < 0.1 & second > -0.1 & first > -0.1 & second < 0.1:
    if first>0 & second<0 :
      return True
    if first<0 & second>0 :
      return True
      
      
def findzero (xvals, yvals):
  zeroes = []
  for counter in range(0,len(yvals)-1):
    if zero(yvals[counter], yvals[counter+1]) :
      zeroes.append(xvals(counter))
  return zeroes