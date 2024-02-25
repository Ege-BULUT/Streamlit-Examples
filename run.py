import os

path = os.path.dirname(os.path.abspath(__file__))
files = [x for x in os.listdir(path) if x.endswith(".py") and x != "run.py"]
print(os.listdir(path))

if not files:
    filepath = input("No .py file found. Please enter the Welcome Page's FULL path manually:")
else:
    print("path : ", path)
    print("files : ", files)
    filepath = os.path.join(path, files[0])

print("filepath : ", filepath)

command = 'streamlit run "' + filepath + '"'

try:
    os.system(command)
except Exception as e:
    print("An error occurred at run.py : \n", e)

print("Streamlit is CLOSED")
