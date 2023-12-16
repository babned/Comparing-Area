length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))

area1 = length1 * width1

length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

area2 = length2 * width2

if area1 > area2:
    print("The area of the first rectangle is greater.")
elif area1 < area2:
    print("The area of the second rectangle is greater.")
else:
    print("The areas of the two rectangles are the same.")