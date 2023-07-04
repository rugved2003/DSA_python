# Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

# The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

# The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        min_left_value = max(ax1,bx1)
        min_right_value = min(ax2,bx2)
        min_top_value = min(ay2,by2)
        min_bottom_value = max(ay1,by1)


        first_rect_area = (ax2 - ax1)*(ay2- ay1)
        second_rect_area = (bx2 - bx1)*(by2- by1)

        if (min_right_value - min_left_value) < 0 or (min_top_value - min_bottom_value )< 0:
            return first_rect_area + second_rect_area

        intersecting_total_area = (min_right_value - min_left_value) * (min_top_value- min_bottom_value)
        return first_rect_area+second_rect_area - intersecting_total_area
