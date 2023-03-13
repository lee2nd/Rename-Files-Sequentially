import os
_src = "/path/to/directory/"
_ext = ".jpg"
for i,filename in enumerate(os.listdir(_src)):
    filename = filename.lower()
    if filename.endswith(_ext):
        os.rename(filename, _src+'opening' + str(i).zfill(3)+_ext)
