import pandas as pd

data={
    "name":["alice","bob","john"],
    "marks":[89,78,90]
    
}

df=pd.DataFrame(data)
print(df)
df["grade"]=["A+","A","O"]

print(df)
