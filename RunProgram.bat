::Toto je spouštěcí skript

echo %~dp0

@py.exe C:\Users\Admin\Desktop\PapersAutoRename\PapersRename.py%*
::@pause

exit 0


:: lze také napsat echo off; umístění python.exe umístění skriptu; pause
