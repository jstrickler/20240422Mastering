import sys
import alpha.mathlib.geometry as geometry   # execute code in geometry.py

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# module search algorithm
# 1. current folder
# 2. folders in PYTHONPATH (if it exists)
# 3. builtin folders in sys.prefix/lib

# sys.path  list of folders to searh
for path in sys.path:
    print(path)
