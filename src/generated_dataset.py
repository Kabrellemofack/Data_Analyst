import numpy as np 
import matplotlib.pyplot as plt 
from math import *
import pandas as pd
import random

# Nombre de clients
n = 1000

data = []

for i in range(n):
    visits = random.randint(1, 50)
    purchases = random.randint(0, visits)
    total_spent = purchases * random.randint(20, 500)

    data.append({
        "customer_id": i+1,
        "age": random.randint(18, 65),
        "gender": random.choice(["Male", "Female"]),
        "city": random.choice(["Paris", "Lyon", "Marseille", "Toulouse"]),
        "visits": visits,
        "purchases": purchases,
        "total_spent": total_spent,
        "campaign": random.choice(["Email", "Social Media", "Ads"]),
        "last_purchase_days": random.randint(1, 365)
    })

df = pd.DataFrame(data)

#df.to_csv("../donnéés/src/customers.csv", index=False)


df = pd.read_csv("../src/customers.csv")

print(df.head(5))
#conaitre mon chiffre d'affaire 
df["conversion_rate"] = df["purchases"] / df["visits"]
print(df['conversion_rate'])