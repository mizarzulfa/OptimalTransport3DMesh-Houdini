import hou
import subprocess

def cmd_call():
    
    node = hou.pwd()
    geo = node.geometry()

    exe_file = node.parm("executable").eval()
    rop_geo = node.parm("rop_out").eval()
    output = node.parm("output").eval()
    
    cmd = f"{exe_file} --in {rop_geo} --out {output}"
    subprocess.call(cmd)
    print(cmd)