import hou

def save():
    node = hou.pwd()
    geo = node.geometry()
    
    param_geo = node.parm("rop_out")
    rop_geo = param_geo.evalAsString()
    
    geo.saveToFile(rop_geo)
    print(rop_geo)