import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json("rain.json")
print(df.head(), "\n")

print("Dataframe statistics: ", df.describe)

df.plot(x='Month', y='Temperature')
df.plot(x='Month', y='Rainfall')
plt.show()