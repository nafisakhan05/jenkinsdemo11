import pandas as pd

print("Extract Data")
data = {
    'Id': [101, 102, 103],
    'Name': ["Hani","Bani","Sani"],
    'Age' : [22, 24, 29]
}
df = pd.DataFrame(data)
print(df)