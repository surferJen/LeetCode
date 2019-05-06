# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

# Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

# Given two (axis-aligned) rectangles, return whether they overlap.

[x1, y1, x2, y2]
[bottom left : top-right]

Example:
Input: rec1 = [0, 0, 2, 2], rec2 = [1, 1, 3, 3]
Output: True
x1, y1 of rec2 must be < than x2, y2 of rec1

Input: rec1 = [2, 3, 3, 4], rec2 = [1, 2, 3, 3]

Input: rec1 = [0, 0, 1, 1], rec2 = [1, 0, 2, 1]
Output: False 


def isRectangleOverlap(rec1, rec2) -> bool:
    if rec2[1] < rec1[3] and rec2[0] < rec1[2]:
        return True
    else:
        return False 