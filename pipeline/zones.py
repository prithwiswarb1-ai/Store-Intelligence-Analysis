from shapely.geometry import Point, Polygon


def inside_zone(x, y, polygon_points):

    polygon = Polygon(polygon_points)

    point = Point(x, y)

    return polygon.contains(point)