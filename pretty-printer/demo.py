import gdb

class dawangDemoPrinter:
    def __init__ (self, val):
        self.val = val

    def to_string (self):
        # print (self.val)
        return 'dawang_demo with x val %s' % (str(self.val['a']))

class dawangDemoMatch:
    def __call__(self, val):
        typetag = val.type.tag
        if typetag != 'dawang_demo':
            return None
        return dawangDemoPrinter(val)

dmatch = dawangDemoMatch()
gdb.pretty_printers.append(dmatch)