import re
import ctypes

class textcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    END = '\033[0m'

total = 10
for i in range(1, total+1):
    progress = i / total * 100
    print(f"Progress: [{progress}%] {'#' * i}", end="\r")

def read_file(file_path): #returns content of file
    file = open(file_path, 'r')
    content = file.readline()
    file.close()
    return content

def error_handler(response):
    if re.search(r'code 200', response):
        print(f"{textcolors.OKGREEN}[ok]█{textcolors.END}")
    else:
        print(textcolors.FAIL + "[fail]" + textcolors.END)

def main():
    response = read_file(r'...\testfile.txt')
    
    kernel32 = ctypes.windll.kernel32 #supports windows 10 coloring
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    
    error_handler(response)
    

if __name__ == "__main__":
    main()
