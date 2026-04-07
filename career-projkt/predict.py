import joblib

model = joblib.load(r"C:\Users\utkar\Downloads\career-projkt\model\model.pkl")

sample = [[0, 6, 4, 8, 6, 5, 7, 0]]

pred = model.predict(sample)
print(pred)