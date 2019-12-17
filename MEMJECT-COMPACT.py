import sys
from ctypes import *
l=windll.kernel32.OpenProcess(983040|1048576|4095,False,int(sys.argv[2]))
a=windll.kernel32.VirtualAllocEx(l,0,len(sys.argv[1]),4096|8192,4)
w=windll.kernel32.WriteProcessMemory(l,a,sys.argv[1],len(sys.argv[1]),byref(c_int(0)))
c=windll.kernel32.CreateRemoteThread(l,None,0,windll.kernel32.GetProcAddress(windll.kernel32.GetModuleHandleA('kernel32.dll'),'LoadLibraryA'),a,0,byref(c_ulong(0)))
