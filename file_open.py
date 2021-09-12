from json import load,dump
class file_open:
    def __init__(self, f_name, f_mode, f_encode='utf-8'):
        """
        f_name=path to file\n
        f_mode=mode file open\n
        f_encode=encoding open file
        """
        self.f_name = f_name
        self.f_mode = f_mode
        self.f_encode = f_encode

    def write(self, data):
        try:
            with open(file=self.f_name, mode=self.f_mode, encoding=self.f_encode) as fi:
                fi.write(data)
                return True
        except:
            return False

    def read(self):
        try:
            with open(file=self.f_name, mode=self.f_mode, encoding=self.f_encode) as fi:
                return fi.read()
        except:
            return False

    def readlines(self):
        try:
            with open(file=self.f_name, mode=self.f_mode, encoding=self.f_encode) as fi:
                return fi.readlines()
        except:
            return False

    def json_load(self):
        try:
            with open(file=self.f_name, mode=self.f_mode, encoding=self.f_encode) as fi:
                return load(fi)
        except:
            return False

    def json_load(self, Object):
        try:
            with open(file=self.f_name, mode=self.f_mode, encoding=self.f_encode) as fi:
                return dump(Object, fi)
        except:
            return False