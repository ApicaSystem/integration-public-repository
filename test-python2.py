#!/usr/bin/env python
# Returns a random value between 1 and 200
import random
import json
import time
import sys
import requests

start_time = time.time()
value = random.randint(1, 200)
str_value = str(value)
end_time = time.time()

response = requests.get(sys.argv[1])

json_return = {
 "returncode": 0,
 "start_time": start_time,
 "end_time": end_time,
 "message": "Random Value: " + str_value,
 "unit": "ms",
 "value": str_value,
 "python": True,
 "response_status": response.status_code
}

print(json.dumps(json_return))
