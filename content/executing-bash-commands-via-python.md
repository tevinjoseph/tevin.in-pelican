Title: Executing bash commands via python
Date: 2014-09-04 10:00 
Category: Programming
Tags: Programming, Python, Linux, bash
Author: Tevin Joseph K O
Email:   tevinjosephko@gmail.com
Summary: In python, executing bash commands can be done using [subprocess ](https://docs.python.org/2/library/subprocess.html) module. It’s pretty easy to use and it’s a powerful module. For simple commands,  we can use [subprocess.call](https://docs.python.org/2/library/subprocess.html#subprocess.call)

In python, executing bash commands can be done using [subprocess ](https://docs.python.org/2/library/subprocess.html) module. It’s pretty easy to use and it’s a powerful module. For simple commands,  we can use [subprocess.call](https://docs.python.org/2/library/subprocess.html#subprocess.call)

Usage:


    import subprocess
     
    subprocess.call("command1")
     
    subprocess.call(["command1", "arg1", "arg2"])

Eg:

    import subprocess
     
    subprocess.call(["ls", "-l"])
    total 4
    
    -rw-rw-r-- 1 tevin tevin 15 Sep 3 15:29 test.txt

You can also use [subprocess.check_call](https://docs.python.org/2/library/subprocess.html#subprocess.check_call)  and [subprocess.check_output](https://docs.python.org/2/library/subprocess.html#subprocess.check_output())

**Popen:**

For more flexibility, you can use [Popen](https://docs.python.org/2/library/subprocess.html#popen-constructor) . Using this you can store the output of command as well as any error occurred during command execution.

Eg:

    process = subprocess.Popen(["ls", "-l"])
    (output, err) = process.communicate()

[communicate](https://docs.python.org/2/library/subprocess.html#subprocess.Popen.communicate)  method interacts with process and waits for the process to complete. It returns a tuple consisting of stdout and stderr.

**Executing commands in background:**

subprocess.Popen() only runs a process in the background if nothing in the python script depends on the output of the command being run. For example, the following code won’t be executed in background.

    import subprocess
     
    process = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)

Thinking about what is subprocess.PIPE?

subprocess.PIPE: Special value that can be used as the stdin, stdout or stderr argument to Popen and indicates that a pipe to the standard stream should be opened.

**Changing directory(cd command):**

You might be thinking that why ‘cd’? Why it can’t be executed using subprocess?

If you use subprocess.call(“cd ..”), it will throw an error ‘No such file or directory’. It is because cd is a shell internal. So you can only call it as

    subprocess.call('cd ..', shell=True)

But it is pointless to do so.  As no process can change another process’s working directory (again, at least on a UNIX-like OS, but as well on Windows), this call will have the subshell change its dir and exit immediately. Don’t worry you can change directory using os.chdir(path).