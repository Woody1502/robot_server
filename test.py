with open('/dev/sda1/text2.txt','wb') as file:
    file.write('123')
import os
print(os.path.exists('/dev/ttyUSB0'))