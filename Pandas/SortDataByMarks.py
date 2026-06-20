import pandas as pd

data={
    "name":["alice","bob","max","sam"],
    "marks":[56,78,90,45]
}

df=pd.DataFrame(data)

print(df.sort_values(by="marks",ascending=False)) 