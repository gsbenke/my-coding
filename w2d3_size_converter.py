# Measure your height in cm and mm, ".0f" means it will only show integer number without decimals.

measure = float(input('Please enter measurement in meters: '))
cm = float(measure*100)
mm = float(measure*1000)
km = float(measure/1000)
print('{}m is equivalent to {:.0f}cm, {:.0f}mm and {}km'.format(measure, cm, mm, km))
