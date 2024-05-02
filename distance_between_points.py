import math

def distance(x1, y1, x2, y2):
    """Calculate the distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Get user input for the coordinates
x1, y1 = map(float, input("Enter the x and y coordinates for the first point (x1 y1), separated by a space: ").split())
x2, y2 = map(float, input("Enter the x and y coordinates for the second point (x2 y2), separated by a space: ").split())

result = distance(x1, y1, x2, y2)
print(f"The distance between the two points is {result:.2f}")