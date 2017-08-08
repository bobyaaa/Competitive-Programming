x1,y1,x2,y2 = map(int,input().split())

N = int(input()) #number of buildings

int1 = [min(x1,x2),max(x1,x2)]

if x2 != x1:
  m = (y2-y1)/(x2-x1)
  b1 = y1-m*x1
else:
  m = 100000
  b1 = 100000

def intersect(x1,y1,x2,y2,x3,y3,x4,y4,m1,b1): #x1-y2 are the telephone points, x3-y4 are the building's two points
  int2 = [max(min(x1,x2),min(x3,x4)),min(max(x1,x2),max(x3,x4))]
  if min(x1,x2) > max(x3,x4) or min(x3,x4) > max(x1,x2): #checks to see if segments have a chance of intersecting
    return False
  if x3 != x4:
    m2 = (y4-y3)/(x4-x3)
    b2 = y3-m2*x3
  else:
    m2 = 100000
    b2 = 100000
  
  if m1 == m2 or m1 == 0 and m2 == 100000 or m2 == 0 and m1 == 100000: #if the lines are parallel or vertical/horizontal
    if m1 == 0 and m2 == 100000: #line 1 is horizontal and line 2 is vertical
      if x3 >= min(x1,x2) and x3 <= max(x1,x2):
        if y1 >= min(y3,y4) and y1 <= max(y3,y4):
          return True
        else:
          return False
      else:
        return False
    elif m2 == 0 and m1 == 100000: #line 1 is vertical and line 2 is horizontal
      if x1 >= min(x3,x4) and x1 <= max(x3,x4):
        if y3 >= min(y1,y2) and y3 <= max(y1,y2):
          return True
        else:
          return False
      else:
        return False
    elif m1 == 0: #horizontal line
      if y1 == y3:
        if min(x1,x2) >= min(x3,x4) and min(x1,x2) <= max(x3,x4) or min(x3,x4) >= min(x1,x2) and min(x3,x4) <= max(x1,x2):
          return True
        else:
          return False
      else:
        return False
    elif m1 == 100000: #vertical line
      if x1 == x3:
        if min(y1,y2) >= min(y3,y4) and min(y1,y2) <= max(y3,y4) or min(y3,y4) >= min(y1,y2) and min(y3,y4) <= max(y1,y2):
          return True
        else:
          return False
      else:
        return False
    else: #all other lines
      if b1 == b2: #if it is the same line
        return True
      else:
        return False
        
  if m1 == 100000: #if line1 is vertical
    intx = x1
    inty = m2*intx+b2
  elif m2 == 100000: #if line2 is vertical
    intx = x3
    inty = m1*intx+b1
  else:
    intx = ((x2*y1-x1*y2)*(x4-x3)-(x4*y3-x3*y4)*(x2-x1))/((x2-x1)*(y4-y3)-(x4-x3)*(y2-y1))
    inty = m1*intx+b1
  if (intx < max(min(x1,x2),min(x3,x4))) or (intx > min(max(x1,x2), max(x3,x4))):
    return False
  elif (inty < max(min(y1,y2), min(y3,y4))) or (inty > min(max(y1,y2), max(y3,y4))):
    return False
  else:
    return True
    
count = 0

for i in range(N):
  points = input().split()
  points = [int(x) for x in points]
  points.pop(0)
  for j in range(int(len(points)/2)): #amount of corners
    if j < int(len(points)/2)-1:
      if intersect(x1,y1,x2,y2,points[j*2],points[j*2+1],points[j*2+2],points[j*2+3],m,b1):
        count += 1
        break
    else:
      if intersect(x1,y1,x2,y2,points[j*2],points[j*2+1],points[0],points[1],m,b1):
        count += 1
        break
print (count)
