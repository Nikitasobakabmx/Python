import sys

'''define global varable'''
class File_corect:
    file = None
    option = None
    name = None
    def __init__(self, name = "text.txt", option = "r"):
        self.name = name
        self.option = option
    def open_file(self):
        if((self.name == None) & (self.option == None)):
            return
        self.file = open(self.name,self.option)
    def close_file(self):
        self.file.close()
        self.file = None
    def processing_text(self):
        if self.file == None:
            return
        prevStr = None
        check = True
        helper = open("help.txt", "w")
        for str in self.file:
            if check:
                prevStr = str
                check = False
                helper.write(str)
                continue
            if ((str.strip() == prevStr.strip()) and ( str != "\n")):
                prevStr = str
                continue
            helper.write(str)
            prevStr = str
        self.file.close()
        helper.close()
def main():
    name = None
    option = None
    if len(sys.argv) > 1:
        name = sys.argv[1]
        option = sys.argv[2]
    else:
        print("You mast input name and options of file!!!")
        name = input()
        option = input()
    file = File_corect(name, option)
    file.open_file()
    file.processing_text()
    file.close_file()
    return
main()