import gdb

class VectorPrinter:
    def __init__ (self, val):
        self.val = val

    def to_string (self):
        s = self.val.cast(gdb.lookup_type("facebook::velox::FlatVector<int>"))
        v = s['values_']
        px = v['px']
        bp = px.cast(gdb.lookup_type("facebook::velox::Buffer").pointer())
        starbp = bp.dereference()
        size = starbp['size_']
        data = starbp['data_'].cast(gdb.lookup_type("unsigned char").pointer())
        t = gdb.lookup_type('int').pointer()
        retval = '[ '
        arr = data.reinterpret_cast(t)
        for i in range(size/4):
            retval += str(arr[i]) + ', '
        retval += ']'
        return retval

def isSupported(encoding, typeKind):
    if encoding == "facebook::velox::VectorEncoding::Simple::FLAT":
        if typeKind == "facebook::velox::TypeKind::INTEGER":
            return True
    return False

class VeloxMatch:
    def __call__(self, val):
        typetag = val.type.tag
        if typetag == 'facebook::velox::BaseVector':
            if isSupported(str(val['encoding_']), str(val['typeKind_'])):
                return VectorPrinter(val)
        return None

vmatch = VeloxMatch()
gdb.pretty_printers.append(vmatch)
