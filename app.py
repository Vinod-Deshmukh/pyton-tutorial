from pathlib import Path

print("#45 Files And Directories")

path=Path()
for file in path.glob('*.*'):
    print(file)


# path=Path("ecommerce")
# print(path.exists())
# path2=Path("email")
# print(path2.exists())
#  print(path2.mkdir())
#  print(path2.rmdir())
