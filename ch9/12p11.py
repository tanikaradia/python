#delete a file,, use os

import os

filePath='filenew.txt'

if os.path.exists(filePath):
    os.remove(filePath)
    print(f'{filePath} deleted successfully')
else:
    print('File does not exist')