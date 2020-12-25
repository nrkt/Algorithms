def check_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    #2つの線分交差判定
    #(x1, y1),(x2, y2)を結ぶ線分と(x3, y3),(x4, y4)を結ぶ線分の交差判定
    s = (x1 - x2) * (y3 - y1) - (y1 - y2) * (x3 - x1)
    t = (x1 - x2) * (y4 - y1) - (y1 - y2) * (x4 - x1)
    if s*t > 0:
        return False
    s = (x3 - x4) * (y1 - y3) - (y3 - y4) * (x1 - x3)
    t = (x3 - x4) * (y2 - y3) - (y3 - y4) * (x2 - x3)
    if s*t > 0:
        return False
    return True