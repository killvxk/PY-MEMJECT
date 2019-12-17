![logo](images/pylogo.png)
##### PY-MEMJECT: A Windows runtime .DLL injection tool that allows for malicious code to run in another processes memory
![tweet](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2FSHADEGREEN%2FPY-MEMJECT%2Ftree%2Fmaster)
[![](https://img.shields.io/badge/python-3-yellow.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)

----

**Usage:**
```
      ./PY-MEMJECT.py <DLL PATH> <process PID>
```

![pops calculator](images/success.png)

----

**About:**
```
Windows API functions process goes as follows:

     OpenProcess() --> Injector attaches to host process
           |---> VirtualAllocEx() --> Memory allocates for host process
                 |---> WriteProcessMemory() --> Copy DLL to host process
                      |---> CreateRemoteThread() --> Code execution

```

*Preface:* There are a couple of types of DLL injection, this utilizes the "Runtime" injection method, which is a legitimate Win32API usage, using only Win32API functions we can inject malicious.DLL code into other running processes. DLL injection is a very common behavior of malware, with about 40% of malware having the capability to inject itself or other malicious code into running processes, usually to establish persistence on a system. DLL injection is also commonly found in video game cheating, where a user can inject a cheat menu into the game.

*Breaking down the Windows API functions:* There are four main steps to injecting a DLL payload into a running processes. The steps are simply to first attach and set up a handler to a running process which will allow us to communicate with it. Secondly you will allocate a space in memory in the host (victim) process that you are injecting. Thirdly, you will inject and copy the .DLL payload into that host processes allocated space. And finally is this all works out, you will get code execution through the victim program.

![image of process](images/Dll-injection-createremotethread.png)

   1. **OpenProcess()** The full documentation from [Microsoft](https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess). Basically it is responsible for setting up access to a process object and returning a handle to us as a means of communication with the process we select.
   2. **VirtualAllocEx()** The full documentation from [Microsoft](https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-virtualallocex). In the context of DLL injection, this function is responsible for allocating memory space in the victim process. 
   3. **WriteProcessMemory()** The full documentation from [Microsoft](https://docs.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-writeprocessmemory). Like the function name states, this function is simply responsible for writing the malicious DLL data to the area of memory that has been allocated with the previous step. 
   4. **CreateRemoteThread()** The full documentation from [Microsoft](https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createremotethread). After connecting to the victim program, allocating and writing data to the host process, CreateRemoteThread creates a thread in the virtual address space of the host process. 

### Disclaimer
>This tool is only for testing and academic purposes and can only be used where strict consent has been given. Do not use it for illegal purposes! It is the end user’s responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this tool and software in general.

