from collections import namedtuple

place = 48.3, 113.9

print(f"{place[0] = }")
print(f"{place[1] = }")

lat, lon = place
print(lat, lon)

Place = namedtuple('Place', 'latitude longitude')

p1 = Place(48.3, 113.9)
p2 = Place(latitude=55.8, longitude=85.3)
p3 = Place(29.6, 255.3838)

print(f"{p1.latitude = }")
print(f"{p3.longitude = }")

places = [p1, p2, p3]


for p in places:
    print(p.latitude, p.longitude)
