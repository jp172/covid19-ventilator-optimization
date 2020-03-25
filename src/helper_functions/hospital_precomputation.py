from ..globals import NBR_SEGMENTS


def get_area_pts(v):
    min_val = min(v)
    max_val = max(v)
    spread = max_val - min_val
    pts = [min_val + spread * i / NBR_SEGMENTS for i in range(NBR_SEGMENTS)]
    return pts
