import class_Point as cP


def intersection(l1, l2):
    x1, y1 = l1.ipt.x_cor, l1.ipt.y_cor
    x2, y2 = l1.fpt.x_cor, l1.fpt.y_cor
    x3, y3 = l2.ipt.x_cor, l2.ipt.y_cor
    x4, y4 = l2.fpt.x_cor, l2.fpt.y_cor

    denominator = round(((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)), 2)
    x_temp = round(((x1 * y2 - x2 * y1) * (x3 - x4) - (x1 - x2) * (x3 * y4 - x4 * y3)), 2)
    y_temp = round(((x1 * y2 - x2 * y1) * (y3 - y4) - (y1 - y2) * (x3 * y4 - x4 * y3)), 2)

    if denominator != 0:
        x_value = round(((x1 * y2 - x2 * y1) * (x3 - x4) - (x1 - x2) * (x3 * y4 - x4 * y3)) / denominator, 2)
        y_value = round(((x1 * y2 - x2 * y1) * (y3 - y4) - (y1 - y2) * (x3 * y4 - x4 * y3)) / denominator, 2)

        if x1 >= x2:
            c_x_l1 = (x1 >= x_value) and (x_value >= x2)
        else:
            c_x_l1 = (x2 >= x_value) and (x_value >= x1)
        if y1 >= y2:
            c_y_l1 = (y1 >= y_value) and (y_value >= y2)
        else:
            c_y_l1 = (y2 >= y_value) and (y_value >= y1)
        c_l1 = c_x_l1 and c_y_l1

        if x3 >= x4:
            c_x_l2 = (x3 >= x_value) and (x_value >= x4)
        else:
            c_x_l2 = (x4 >= x_value) and (x_value >= x3)
        if y3 >= y4:
            c_y_l2 = (y3 >= y_value) and (y_value >= y4)
        else:
            c_y_l2 = (y4 >= y_value) and (y_value >= y3)
        c_l2 = c_x_l2 and c_y_l2

        if c_l1 and c_l2:
            return cP.Point(x_value, y_value), 0  # perfect intersection
        else:
            return cP.Point(None, None), 1  # intersection on extension
    else:  # parallel lines
        if x_temp == 0 and y_temp == 0:
            c1 = x1 == x2 and y1 == y2
            c2 = x3 == x4 and y3 == y4
            if c1 or c2:  # either of them is point,  complete case
                return cP.Point(None, None), 2
            else:

                cx1 = x1 < x4 and x1 < x3 and x2 < x4 and x2 < x3  # (x1x2)...(x3x4) in any order within same line
                cx2 = x1 > x4 and x1 > x3 and x2 > x4 and x2 > x3  # x3x4...x1x2,  in any order within same line
                cy1 = y1 < y4 and y1 < y3 and y2 < y4 and y2 < y3
                cy2 = y1 > y4 and y1 > y3 and y2 > y4 and y2 > y3
                if cx1 or cx2 or cy1 or cy2:  # non overlapping lines, same line (complete case)
                    return cP.Point(None, None), 3
                else:
                    cx1 = x1 < x3 and x3 < x2 and x1 < x4 and x4 < x2  # x1 (x3/x4) x2
                    cx2 = x2 < x3 and x3 < x1 and x2 < x4 and x4 < x1  # x2 (x3/x4) x1
                    cx3 = x3 < x1 and x1 < x4 and x3 < x2 and x2 < x4  # x3 (x1/x2) x4
                    cx4 = x4 < x1 and x1 < x3 and x4 < x2 and x2 < x3  # x4 (x1/x2) x4

                    cy1 = y1 < y3 and y3 < y2 and y1 < y4 and y4 < y2
                    cy2 = y2 < y3 and y3 < y1 and y2 < y4 and y4 < y1
                    cy3 = y3 < y1 and y1 < y4 and y3 < y2 and y2 < y4
                    cy4 = y4 < y1 and y1 < y3 and y4 < y2 and y2 < y3

                    c1 = cx1 or cx2 or cx3 or cx4
                    c2 = cy1 or cy2 or cy3 or cy4

                    if c1 or c2:  # one line is completely within the other, same line complete case
                        return cP.Point(None, None), 4
                    else:
                        cx1 = x1 < x3 and x1 < x4 and x3 < x2 and x2 < x4  # x1, x3, x2, x4
                        cx2 = x1 < x4 and x1 < x3 and x4 < x2 and x2 < x3  # x1, x4, x2, x3
                        cx3 = x2 < x3 and x2 < x4 and x3 < x1 and x1 < x4  # x2, x3, x1, x4
                        cx4 = x2 < x4 and x2 < x3 and x4 < x1 and x1 < x3  # x2, x4, x1, x3
                        cx5 = x3 < x1 and x3 < x2 and x1 < x4 and x4 < x2  # x3, x1, x4, x2
                        cx6 = x3 < x2 and x3 < x1 and x2 < x4 and x4 < x1  # x3, x2, x4, x1
                        cx7 = x4 < x1 and x4 < x2 and x1 < x3 and x3 < x2  # x4, x1, x3, x2
                        cx8 = x4 < x2 and x4 < x1 and x2 < x3 and x3 < x1  # x4, x2, x3, x1

                        cy1 = y1 < y3 and y1 < y4 and y3 < y2 and y2 < y4  # x1, x3, x2, x4
                        cy2 = y1 < y4 and y1 < y3 and y4 < y2 and y2 < y3  # x1, x4, x2, x3
                        cy3 = y2 < y3 and y2 < y4 and y3 < y1 and y1 < y4  # x2, x3, x1, x4
                        cy4 = y2 < y4 and y2 < y3 and y4 < y1 and y1 < y3  # x2, x4, x1, x3
                        cy5 = y3 < y1 and y3 < y2 and y1 < y4 and y4 < y2  # x3, x1, x4, x2
                        cy6 = y3 < y2 and y3 < y1 and y2 < y4 and y4 < y1  # x3, x2, x4, x1
                        cy7 = y4 < y1 and y4 < y2 and y1 < y3 and y3 < y2  # x4, x1, x3, x2
                        cy8 = y4 < y2 and y4 < y1 and y2 < y3 and y3 < y1  # x4, x2, x3, x1

                        c1 = cx1 or cx2 or cx3 or cx4 or cx5 or cx6 or cx7 or cx8
                        c2 = cy1 or cy2 or cy3 or cy4 or cy5 or cy6 or cy7 or cy8

                        if c1 or c2:  # overlapping at one end , same line, complete case
                            return cP.Point(None, None), 5
                        else:
                            cx1 = x1 < x3 and x1 < x4 and x3 == x2 and x2 < x4  # x1, x3, x2, x4
                            cx2 = x1 < x4 and x1 < x3 and x4 == x2 and x2 < x3  # x1, x4, x2, x3
                            cx3 = x2 < x3 and x2 < x4 and x3 == x1 and x1 < x4  # x2, x3, x1, x4
                            cx4 = x2 < x4 and x2 < x3 and x4 == x1 and x1 < x3  # x2, x4, x1, x3
                            cx5 = x3 < x1 and x3 < x2 and x1 == x4 and x4 < x2  # x3, x1, x4, x2
                            cx6 = x3 < x2 and x3 < x1 and x2 == x4 and x4 < x1  # x3, x2, x4, x1
                            cx7 = x4 < x1 and x4 < x2 and x1 == x3 and x3 < x2  # x4, x1, x3, x2
                            cx8 = x4 < x2 and x4 < x1 and x2 == x3 and x3 < x1  # x4, x2, x3, x1

                            cy1 = y1 < y3 and y1 < y4 and y3 == y2 and y2 < y4  # x1, x3, x2, x4
                            cy2 = y1 < y4 and y1 < y3 and y4 == y2 and y2 < y3  # x1, x4, x2, x3
                            cy3 = y2 < y3 and y2 < y4 and y3 == y1 and y1 < y4  # x2, x3, x1, x4
                            cy4 = y2 < y4 and y2 < y3 and y4 == y1 and y1 < y3  # x2, x4, x1, x3
                            cy5 = y3 < y1 and y3 < y2 and y1 == y4 and y4 < y2  # x3, x1, x4, x2
                            cy6 = y3 < y2 and y3 < y1 and y2 == y4 and y4 < y1  # x3, x2, x4, x1
                            cy7 = y4 < y1 and y4 < y2 and y1 == y3 and y3 < y2  # x4, x1, x3, x2
                            cy8 = y4 < y2 and y4 < y1 and y2 == y3 and y3 < y1  # x4, x2, x3, x1

                            c1 = cx1 or cx2 or cx3 or cx4 or cx5 or cx6 or cx7 or cx8
                            c2 = cy1 or cy2 or cy3 or cy4 or cy5 or cy6 or cy7 or cy8

                            if c1 or c2:  # overlapping at one end , same line, complete case
                                return cP.Point(None, None), 6
                            else:
                                cx1 = x1 < x3 and x1 < x4 and x3 < x2 and x2 == x4  # x1, x3, x2, x4
                                cx2 = x1 < x4 and x1 < x3 and x4 < x2 and x2 == x3  # x1, x4, x2, x3
                                cx3 = x2 < x3 and x2 < x4 and x3 < x1 and x1 == x4  # x2, x3, x1, x4
                                cx4 = x2 < x4 and x2 < x3 and x4 < x1 and x1 == x3  # x2, x4, x1, x3
                                cx5 = x3 < x1 and x3 < x2 and x1 < x4 and x4 == x2  # x3, x1, x4, x2
                                cx6 = x3 < x2 and x3 < x1 and x2 < x4 and x4 == x1  # x3, x2, x4, x1
                                cx7 = x4 < x1 and x4 < x2 and x1 < x3 and x3 == x2  # x4, x1, x3, x2
                                cx8 = x4 < x2 and x4 < x1 and x2 < x3 and x3 == x1  # x4, x2, x3, x1

                                cy1 = y1 < y3 and y1 < y4 and y3 < y2 and y2 == y4  # x1, x3, x2, x4
                                cy2 = y1 < y4 and y1 < y3 and y4 < y2 and y2 == y3  # x1, x4, x2, x3
                                cy3 = y2 < y3 and y2 < y4 and y3 < y1 and y1 == y4  # x2, x3, x1, x4
                                cy4 = y2 < y4 and y2 < y3 and y4 < y1 and y1 == y3  # x2, x4, x1, x3
                                cy5 = y3 < y1 and y3 < y2 and y1 < y4 and y4 == y2  # x3, x1, x4, x2
                                cy6 = y3 < y2 and y3 < y1 and y2 < y4 and y4 == y1  # x3, x2, x4, x1
                                cy7 = y4 < y1 and y4 < y2 and y1 < y3 and y3 == y2  # x4, x1, x3, x2
                                cy8 = y4 < y2 and y4 < y1 and y2 < y3 and y3 == y1  # x4, x2, x3, x1

                                c1 = cx1 or cx2 or cx3 or cx4 or cx5 or cx6 or cx7 or cx8
                                c2 = cy1 or cy2 or cy3 or cy4 or cy5 or cy6 or cy7 or cy8

                                if c1 or c2:  # overlapping at right end , same line, complete case
                                    return cP.Point(None, None), 7
                                else:
                                    cx1 = x1 == x3 and x1 < x4 and x3 < x2 and x2 > x4  # x1, x3, x4, x2
                                    cx2 = x1 == x4 and x1 < x3 and x4 < x2 and x2 > x3  # x1, x4, x3, x2
                                    cx3 = x2 == x3 and x2 < x4 and x3 < x1 and x1 > x4  # x2, x3, x4, x1
                                    cx4 = x2 == x4 and x2 < x3 and x4 < x1 and x1 > x3  # x2, x4, x3, x1
                                    cx5 = x3 == x1 and x3 < x2 and x1 < x4 and x4 > x2  # x3, x1, x2, x4
                                    cx6 = x3 == x2 and x3 < x1 and x2 < x4 and x4 > x1  # x3, x2, x1, x4
                                    cx7 = x4 == x1 and x4 < x2 and x1 < x3 and x3 > x2  # x4, x1, x2, x3
                                    cx8 = x4 == x2 and x4 < x1 and x2 < x3 and x3 > x1  # x4, x2, x1, x3

                                    cy1 = y1 == y3 and y1 < y4 and y3 < y2 and y2 > y4  # x1, x3, x2, x4
                                    cy2 = y1 == y4 and y1 < y3 and y4 < y2 and y2 > y3  # x1, x4, x2, x3
                                    cy3 = y2 == y3 and y2 < y4 and y3 < y1 and y1 > y4  # x2, x3, x1, x4
                                    cy4 = y2 == y4 and y2 < y3 and y4 < y1 and y1 > y3  # x2, x4, x1, x3
                                    cy5 = y3 == y1 and y3 < y2 and y1 < y4 and y4 > y2  # x3, x1, x4, x2
                                    cy6 = y3 == y2 and y3 < y1 and y2 < y4 and y4 > y1  # x3, x2, x4, x1
                                    cy7 = y4 == y1 and y4 < y2 and y1 < y3 and y3 > y2  # x4, x1, x3, x2
                                    cy8 = y4 == y2 and y4 < y1 and y2 < y3 and y3 > y1  # x4, x2, x3, x1

                                    c1 = cx1 or cx2 or cx3 or cx4 or cx5 or cx6 or cx7 or cx8
                                    c2 = cy1 or cy2 or cy3 or cy4 or cy5 or cy6 or cy7 or cy8

                                    if c1 or c2:  # overlapping at left end , same line, complete case
                                        return cP.Point(None, None), 8
                                    else:
                                        return cP.Point(None, None), 9

        else:
            return cP.Point(None, None), 10  # parallel lines with distance in between
