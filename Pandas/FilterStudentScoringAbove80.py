import pandas as pd

data={
    "name": ["alice","john","bob","vini","max","sam"],
    "marks":[67,89,86,90,65,78]
}

df=pd.DataFrame(data)

result=df[df["marks"]>80]

print(result)