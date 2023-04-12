def squareFootage(length=0, width=0):
    print(f'Length entered: {length}.')
    print(f'Width entered: {width}.')
    total_area = length*width
    print(f'Calculated square footage: {total_area}.')
    return(total_area)

def circumferenceCircle(radius=0):
    print(f'Radius entered: {radius}.')
    temp_circum = round(2*3.14159*radius,2)
    print(f'Calculated circumference: {temp_circum}.')
    return(temp_circum)