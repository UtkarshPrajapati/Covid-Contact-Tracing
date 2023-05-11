import random
import time
from datetime import datetime, timedelta
names = ["David", "Frank", "Carol", "Ivan", "Erin", "Bob", "Grace", "Alice", "Judy"]
start_date = datetime(2020, 7, 4)
end_date = datetime(2020, 7, 5)
lat_range = [13.0, 13.3]
lon_range = [77.5, 77.7]
data = []
for name in names:
    for i in range(random.randint(1, 100)):
        timestamp = start_date + (end_date - start_date) * random.random()
        timestamp = int(time.mktime(timestamp.timetuple()))
        latitude = round(random.uniform(*lat_range), 7)
        longitude = round(random.uniform(*lon_range), 7)
        data.append({
            "id": name,
            "timestamp": timestamp,
            "latitude": str(latitude),
            "longitude": str(longitude)
        })

print(data)