#!/usr/bin/env python

def FindSubLeadingValueInList(valuesList):
    max1, max2 = None, None
    for x in valuesList:
        if x >= max1:
            max1, max2 = x, max1
        elif x > max2:
            max2 = x
        else:
            pass
    return max2


###############################################################
if __name__ == "__main__":

    valuesList1 = [20, 30, 40, 50, 60.5, -123.0, 90.232, 100.0, 100.0]
    valuesList2 = [20, 30, 40, 50, 60.5, -123.0, 90.232, 100.0]

    max2 = FindSubLeadingValueInList(valuesList1)
    print max2
    max2 = FindSubLeadingValueInList(valuesList2)
    print max2
