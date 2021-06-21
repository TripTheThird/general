import math

def main():
    circleCount = getNumberOfCircles()
    areas = circleCountLoop(int(circleCount))
    displayAreas(areas)
    
    
    

def circleCountLoop(circleCount):
    areas = []
    for _ in range(circleCount):
        r = getRadius()
        areas.append(computeCircleArea(r))
    return areas

def displayAreas(areas):
    zeroes = '.2f'
    # roundedAreaList = [round(a, 2) for a in areas]6
    roundedAreaList = [f"{a:,{zeroes}}" for a in areas] 
     
    print(roundedAreaList)
        
def getNumberOfCircles():
    numCheck = True
    while numCheck:
        try: 
            return float(input("How many circles are you working with? "))
            numCheck = False
            return num
        except:
            print("not an integer")
     

def getRadius():
    return float(input("Please enter a radius: "))

def computeCircleArea(radius):
    return math.pi * radius ** 2



main()
