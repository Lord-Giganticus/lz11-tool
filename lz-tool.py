import sys
import os


try:
    sys.argv[1]
except:
    print('Usage: py lz-tool.py ENC/DEC "file"')
    exit()
try:
    sys.argv[2]
    if os.path.isfile(sys.argv[2]) == False:
        print("File not found.")
        exit()
except:
    print('Usage: py lz-tool.py ENC/DEC/-h "file"')
    exit()

if sys.argv[1] == 'ENC':
    file = sys.argv[2]
    try:
        os.system('cmd /c py -3 compress.py '+file)
        print("Complete.")
        exit()
    except:
        print("File is not LZ11 encodable.")
        exit()
elif sys.argv[1] == "DEC":
    file = sys.argv[2]
    if file.endswith('.lz') == False:
        print("File is not a LZ file.")
        exit()
    try:
        os.system('cmd /c py -3 lzss3.py '+file)
        print("Complete.")
        exit()
    except:
        print("File cannot be decoded.") 
        exit()
else:
    print('Usage: py lz-tool.py ENC/DEC/-h "file"')
    exit()