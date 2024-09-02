import os

f = __file__
print(f)

dir_name = os.path.dirname(f)

os.path.join(dir_name, "model.pkl")
