import time
from datetime import datetime, date

print(f"Started at {datetime.now()}")
start = time.perf_counter()  # seconds since 1/1/70
# code here ....
end  = time.perf_counter()
print(f"Finished at {datetime.now()}")

elapsed_seconds = end - start

date1 = date(1861, 7, 22)
date2 = date(1941, 12, 7)
print(f"{date1 = }")
print(f"{date2 = }")
elapsed = date2 - date1
print(f"{elapsed = }")
print(f"{elapsed.days/365.25 = }")

