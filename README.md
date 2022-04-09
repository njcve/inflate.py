# inflate.py
A quick and simple script that can be used to inflate binary files by padding them out with null bytes. Simply call the script along with the name or location of the binary you want to inflate plus an integer value to inflate it by.

I have used this to successfully evade AV and EDR solutions as many security vendors simply do not check large files!

# Example
```
----
$ ls -la
-rwxrwxrwx 1 kali kali 1001224 Mar  8  2020 mimikatz.exe

----
$ python inflate.py -f mimikatz.exe -s 150
[!]     Inflating mimikatz.exe by 150 MB
[!]     Operation Complete...
----

$ ls -la
-rwxrwxrwx 1 kali kali 158287624 Mar  8  2020 mimikatz.exe
----
```
