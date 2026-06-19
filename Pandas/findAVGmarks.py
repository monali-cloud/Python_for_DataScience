import pandas as pd

data={
    "name":["alice","bob","john"],
    "marks":[45,56,43]
}

df=pd.DataFrame(data)

print("Average Marks : ",df["marks"].mean())