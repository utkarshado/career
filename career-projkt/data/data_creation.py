import pandas as pd
import random


data = []

for _ in range(1000):
    prog = random.randint(0,10)
    math = random.randint(0,10)
    comm = random.randint(0,10)
    creative = random.randint(0,10)
    logic = random.randint(0,10)
    tech = random.randint(0,10)
    business = random.randint(0,10)
    cgpa = round(random.uniform(5,10), 2)


    if prog > 7 and logic > 7:
        career = "Software Engineer"
    elif math > 7 and tech > 7:
        career = "Data Scientist"
    elif comm > 7 and business > 7:
        career = "Product Manager"
    elif creative > 7:
        career = "Designer"
    else:
        career = "Core Engineer"

    data.append([prog, math, comm, creative, logic, tech, business, cgpa, career])

df = pd.DataFrame(data, columns=[
    "prog","math","comm","creative","logic","tech","business","cgpa","career"
])

df.to_csv("career_data.csv", index=False)
