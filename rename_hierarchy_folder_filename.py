import os
import glob

path_lst = glob.glob(r"檔案路徑")

for folder in path_lst:
    print(folder)
    for i,filename in enumerate(os.listdir(folder)):
        path = floder+"\\"+filename
        if path.endswith("JPG") or path.endswith("jpg"):
            os.rename(path, "\\".join(path.split("\\")[:-1])+"\\"+str(i).zfill(3)+".jpg")
