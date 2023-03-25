::TODO: pip install etc.
::TODO: vytvoří spouštěcí BAT skript s patřičnými názvy

::echo %~dp0
::echo %~dpnx0
echo off

::Následující najde python skript a uloží jeho cestu; vyhledává i v podsložkách
for /r ./ %%a in (*) do if "%%~nxa"=="PapersRename.py" set p=%%~dpnxa
if defined p (
echo %p%
) else (
echo File not found
)

::Zde se vytvoří spouštěcí program R






pause