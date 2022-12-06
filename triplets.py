##############################################################################
## Pythagorean Triplets 
## Calculate a subset of Pythagorean triplets such as 3,4,5
## following the a^2 + b^2 = c^2 formula where the triplets are whole numbers
## Paul Saletzki May 1998
##############################################################################
import sys
import math 
import csv

#####################################################################
# Given a and b values check to see if they are Pythagorean Triplets
#####################################################################
def IsPythagoreanTriplet(a, b):
    c = math.sqrt(a * a + b * b)
    return int(c), c == math.floor(c)

##################################
# Given data write to csv file.
##################################
def WriteCSVFile(data, header, max): 
    fileName = 'Pythagorean Triplets up to ' + str(max) + '.csv'
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)
    print('File:', fileName, 'written...')

defaultMax = 1000
max= defaultMax

#######################################
# Command Line Arguments
# get the arguments passed in if any
#######################################
parmLen = len(sys.argv)

if parmLen > 1:
    tmp = sys.argv[1]
    try:
        tmp = int(tmp)
        max = tmp
        if (max <= 0):
            max = defaultMax
    except:
        # catch and move on.  Not a valid value passed in.
        max = defaultMax
        
print('Calculating Pythagorean Triplets up to', max)
cnt = 0
data = []
header = ['count', 'a', 'b', 'c']
for a in range(2, max + 1):
    for b in range(a+1, max + 11):
        c = 0
        res = IsPythagoreanTriplet(a, b)
        if res[1]:
            cnt = cnt+1
            print('#', cnt, ': a =', a, ', b =', b , ', c =', res[0])
            data.append( [cnt, a, b, res[0]])
            # print(a*a + b*b, int(tmp*tmp))

WriteCSVFile(data, header, max)

print('Done...')