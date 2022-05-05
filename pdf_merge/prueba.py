import os

# obj = os.scandir('./')
# for o in obj:
#     if o.is_dir():
#         print(o.name)

subcarpetas = [_.name for _ in os.scandir('./') if _.is_dir()]
print(subcarpetas)