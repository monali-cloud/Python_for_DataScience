import pandas as pd

data={
    "name":["alice","bob","john"],
    "marks":[45,67,57],
    "Grade":["O","A+","A"]
}

df=pd.DataFrame(data)

print(df["Grade"].value_counts())