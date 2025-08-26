# 5.Write a program to check if three sides length form a valid triangle and also check it is forming a right angle triangle.
def valid_triangle(sideA,sideB,sideC):
    
    if (sideA + sideB > sideC) and (sideB + sideC > sideA) and (sideC + sideA > sideB):
        print('valid triangle')    
    else:
            print('not a valid triangle')
    if (sideA + sideB > sideC) and (sideB + sideC > sideA) and (sideC + sideA > sideB):
        if sideA == sideB == sideC:
            print('equilateral traingle')
        elif sideA == sideB or sideB == sideC or sideC == sideA:
            print('isosceles traingle')
        else:
            print('scalen triangle') 
    if sideA * sideA == sideB * sideB + sideC * sideC or sideB * sideB == sideA * sideA + sideC * sideC or sideC * sideC == sideB * sideB + sideA * sideA:
        print('right angle triangle')
    else:
        print('not a right angle triangle')

side1 = int(input('enter number:'))
side2 = int(input('enter number:'))
side3 = int(input('enter number:'))
valid_triangle(side1,side2,side3)