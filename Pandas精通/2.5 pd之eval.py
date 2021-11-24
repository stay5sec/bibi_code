# coding:utf-8
# author:stay5sec
import pandas as pd

pd.set_option('expand_frame_repr', False)
pd.set_option('display.max_rows', 1000)

df = pd.DataFrame({"animal": ["dog", "pig"], "age": [10, 20]})

print(df)
print("\n")

df2 = pd.eval("double_age = df.age * 2", target=df)

print(df2)
print("\n")

exec("""df2["big_age"]=df2["double_age"]*10""")

print(df2)
