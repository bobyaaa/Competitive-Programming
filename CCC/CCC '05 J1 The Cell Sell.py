daytime = input()
evening = input()
weekend = input()

def PlanA(a, b, c):
  if a > 100:
    return (a - 100)*0.25 + b*0.15 + c*0.20
  else:
    return b*0.15 + c*0.2
    
def PlanB(a, b, c):
  if a > 250:
    return (a - 250)*0.45 + b*0.35 + c*0.25
  else:
    return b*0.35 + c*0.25
    
print "Plan A costs " + str(PlanA(daytime, evening, weekend))
print "Plan B costs " + str(PlanB(daytime, evening, weekend))

if PlanA(daytime, evening, weekend) < PlanB(daytime, evening, weekend):
  print "Plan A is cheapest."
elif PlanB(daytime, evening, weekend) < PlanA(daytime, evening, weekend):
  print "Plan B is cheapest."
else:
  print "Plan A and B are the same price."
