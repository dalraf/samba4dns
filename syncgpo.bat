@echo off

robocopy.exe  C:\Windows\SYSVOL\sysvol  \\smb01\SYSVOL\ /mir  /sec /mt

exit

