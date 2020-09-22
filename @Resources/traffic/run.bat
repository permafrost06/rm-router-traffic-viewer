tasklist /FI "IMAGENAME eq pythonrm.exe" 2>NUL | find /I /N "pythonrm.exe">NUL
if not "%ERRORLEVEL%"=="0" cd /d E:\Documents\Rainmeter\Skins\illustro\@Resources\traffic && start pythonrm tprm.py