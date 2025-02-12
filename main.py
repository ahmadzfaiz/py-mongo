import uuid
import random
from datetime import datetime

with open("data.csv", "a") as f:
  f.write("%s,%s,%s" % (
    uuid.uuid4(), 
    random.randint(1, 100_000),
    datetime.now()
  ))