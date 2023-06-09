# geotoolkit
A lightweight python library for working with geographic coordinates. This library can be used in things such as drone navigation, speed measurement, and more.

## Examples
Measuring distance between two points:
```
p1 = (33.93369079118477, -118.41900963926824)
p2 = (33.937366248549935, -118.38276824755901)
distance = distance(p1, p2)
print(distance) # 2.0952233910697995, in miles
```

Checking if a point lies within (inside of) a polygon:
```
raw_json:str = "[[34.04709656460684, -118.51420813970792], [34.0173210880725, -118.00731306657742], [33.92068010802825, -117.92185949106074], [33.695565897860064, -118.00828413031054], [33.693142098170746, -118.38020139809352]]" # load a polygon from a JSON array of arrays
polygon:list[tuple[float, float]] = load_polygon(raw_json)
point1:tuple[float, float] = (33.924709007544834, -118.22191807002923)
point2:tuple[float, float] = (33.88682983206357, -118.72492888526082)
print(inside_polygon(point1, polygon)) # True (it is within the polygon)
print(inside_polygon(point2, polygon)) # False (it is outside of the polygon)
```

Measuring speed:
```
mph = speed_mph((33.92533554514059, -118.32099118005947), (33.92532143656184, -118.31715080400728), 9.8)
print(mph) # 80.96760998067498 MPH
```