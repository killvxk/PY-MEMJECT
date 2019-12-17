import sys # This is the most compact version of a DLL injector with CLI arguments I can write
from ctypes import *
l = windll.kernel32.OpenProcess(( 0x00F0000 | 0x00100000 | 0xFFF ), False, int(sys.argv[2]))
a = windll.kernel32.VirtualAllocEx(l, 0, len(sys.argv[1]), ( 0x1000 | 0x2000 ), 0x04)
w = windll.kernel32.WriteProcessMemory(l, a, sys.argv[1], len(sys.argv[1]), byref(c_int(0)))
c = windll.kernel32.CreateRemoteThread(l, None, 0,windll.kernel32.GetProcAddress(windll.kernel32.GetModuleHandleA("kernel32.dll"), "LoadLibraryA"), a, 0, byref(c_ulong(0)))
