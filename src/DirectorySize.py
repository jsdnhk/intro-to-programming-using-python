import os

def main():
    path = input("Enter a directory or a file: ").strip()

    try:
        print("%.2f MB" % getSize(path) )
    except:
        print("Directory or file does not exist")

def getSize(path):
    size = 0

    if not os.path.isfile(path):    #if path is dir
        files = os.listdir(path)     #all files and dirs
        for file in files:
            size += getSize(os.path.join(path, file))
    else:   #if path is file
        size += os.path.getsize(path) / float(1024 * 1024)

    return size

main()
