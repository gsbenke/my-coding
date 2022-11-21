# Calculates wall area
print("Let's calculate wall area in Square Meters!")
larg = float(input("How wide is it (in meters)? "))
alt = float(input("How tall is it (in meters)? "))
area = larg * alt

# Tells you how much product you need to paint this area 
ink = area / 2
print("\nThis {} x {} wall has an area of {:.4f}sqm!".format(larg, alt, area))
print("Get {:.4f} liters of paint for this job.".format(ink))

# Calculates paint price and extra costs
ink = float(input("How much is the paint per litre? "))
extras = ink + (ink * 15/100)
print("\nAdding 15 percent for other tools, project will cost ${:.02f} ".format(extras))



