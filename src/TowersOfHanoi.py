#!/usr/bin/python3

"""
def moveDisks(n, fromTower, toTower, auxTower):
if n == 1:
    Move disk 1 from the fromTower to the toTower
else:
    moveDisks(n - 1, fromTower, auxTower, toTower)
    Move disk n from the fromTower to the toTower
    moveDisks(n - 1, auxTower, toTower, fromTower)
"""
count = 0

def main():
    n = eval(input("Enter number of disks: "))
    # Find the solution recursively
    print("The moves are: ")
    moveDisks(n, 'A', 'B', 'C')

def moveDisks(n, fromTower, toTower, auxTower):
    """
    The function for finding the solution to move n disks
    from fromTower to toTower with auxTower
    :param n: Disk Amount
    :param fromTower:
    :param toTower:
    :param auxTower:
    :return: None
    """
    #print("moveDisks(%s, %s, %s, %s)" % (n, fromTower, toTower, auxTower))
    global count
    count += 1

    if n == 1: # Stopping condition
        print("Move disk", n, "from", fromTower, "to", toTower)    #Placed directly
    else:   #When n > 1, the generic 3-steps to move a tower
        moveDisks(n - 1, fromTower, auxTower, toTower)  # top (n - 1) disks move fromTower -> auxTower
        print("Move disk", n, "from", fromTower, "to", toTower) # the most under disk (n) fromTower -> toTower
        moveDisks(n - 1, auxTower, toTower, fromTower)  # top (n - 1) disks move auxTower -> toTower

main()  # Call the main function
print("count = %s" % (count))