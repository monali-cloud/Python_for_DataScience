import pandas as pd

data={
    "name":["alice","bob","john"],
    "marks":[45,67,89]
}
df=pd.DataFrame(data)

top_student=df.loc[df["marks"].idxmax()]

print(top_student) 