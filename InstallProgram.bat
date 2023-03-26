::TODO: pip install etc.
::TODO: vytvoří spouštěcí BAT skript s patřičnými názvy

title Instalace Programu
@echo off
cls
color 2

echo """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
echo """                                                                                            """
echo """                     __,               , _                                                  """
echo """                    /  |       _|_  _ /|/ \  _        _,           _                        """
echo """                   |   |  |  |  |  / \_|__/ |/ /|/|  / |  /|/|/|  |/                        """
echo """                    \_/\_/ \/|_/|_/\_/ | \_/|_/ | |_/\/|_/ | | |_/|_/                       """
echo """                    ()  _  o  _        _   _     _,   ,_ _|_ o  _  |\  _                    """
echo """                    /\ /   | |/ /|/|  /   |/    / |  /  | |  | /   |/ |/                    """
echo """                   /(_)\__/|/|_/ | |_/\__/|_/   \/|_/   |/|_/|/\__/|_/|_/                   """
echo """                                                                                            """
echo """--------------------------------------------------------------------------------------------"""
echo """                                                                       by Tomas Spurny      """
echo """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
echo """                      _                                                          .--.       """
echo """                    _(_)_                                 wWWWw      _         .'_\/_'.     """
echo """    @@@@           (_)@(_)     vVVVv       _      @@@@    (___)    _(_)_       '. /\ .'     """
echo """   @@()@@   wWWWw    (_)\      (___)     _(_)_   @@()@@     Y     (_)@(_)         ||        """
echo """    @@@@    (___)       `|/      Y      (_)@(_)   @@@@     \|/      (_)\          || /\     """
echo """     /        Y         \|      \|/      /(_)     \|        |/         |       /\ ||//\     """
echo """  \ |       \ |/         | /   \ | /    \|/        |/      \|         \|/      /\\||/_/     """
echo """   \|//     \\|//  /  \\\|//  \\\|///   \|///   \\\|//    \\|//     \\\|//       \||/       """
echo """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
echo """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
echo.
echo.
echo Vitejte u instalace programu!
echo.
echo Hint: Instalacni soubor by nemel byt umisten ve slozce, ceste ke slozce, v niz je diakritika.
echo Aktualni cesta je %~dp0
echo    K pokracovani stisknete jakoukoli klavesu.
echo.
pause > nul
echo Nyni se Vam spusti instalace programovaciho jazyku Python 3.11.2.
echo     Zaskrknete moznost "Add Python to PATH".
timeout 2 > nul 
%~dp0\Source\python-3.11.2-amd64.exe
echo     K pokracovani stisknete jakoukoli klavesu.
pause > nul
echo Aktualne mate Python na ceste:
where python
echo     Pokud tomu je tedy Python nainstalovan, stisknete Enter.
pause > nul
echo.
echo Nyni se Vam nainstaluji potrebne python moduly.
::TODO: pip install
echo.
echo Prave se zjistuje cesta zdrojoveho kodu programu.
timeout 2 > nul

::Následující najde python skript a uloží jeho cestu; vyhledává i v podsložkách
for /r ./ %%a in (*) do if "%%~nxa"=="PapersRename.py" set CestaProgramu=%%~dpnxa

echo    - Aktualni cesta zdrojoveho kodu je:
if defined CestaProgramu (echo          %CestaProgramu%) else (echo      File not found)
::https://devblogs.microsoft.com/oldnewthing/20120731-00/?p=7003
::https://stackoverflow.com/questions/13876771/find-file-and-return-full-path-using-a-batch-file


echo.
echo Nyni se vytvori spousteci soubor pro program.
set CestaPythonu=python 
set prikaz=%CestaPythonu% %CestaProgramu%
::echo %prikaz%


echo echo off >RunProgramTEST.bat
echo cls >>RunProgramTEST.bat
echo echo.    >>RunProgramTEST.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >>RunProgramTEST.bat
echo echo "         __,               , _                                      " >>RunProgramTEST.bat
echo echo "        /  |       _|_  _ /|/ \  _        _,           _            " >>RunProgramTEST.bat
echo echo "       |   |  |  |  |  / \_|__/ |/ /|/|  / |  /|/|/|  |/            " >>RunProgramTEST.bat
echo echo "        \_/\_/ \/|_/|_/\_/ | \_/|_/ | |_/\/|_/ | | |_/|_/           " >>RunProgramTEST.bat
echo echo "        ()  _  o  _        _   _     _,   ,_ _|_ o  _  |\  _        " >>RunProgramTEST.bat
echo echo "        /\ /   | |/ /|/|  /   |/    / |  /  | |  | /   |/ |/        " >>RunProgramTEST.bat
echo echo "       /(_)\__/|/|_/ | |_/\__/|_/   \/|_/   |/|_/|/\__/|_/|_/       " >>RunProgramTEST.bat
echo echo "--------------------------------------------------------------------" >>RunProgramTEST.bat
echo echo "                                                   by Tomas Spurny  " >>RunProgramTEST.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >>RunProgramTEST.bat
echo echo "                    _                                               " >>RunProgramTEST.bat    
echo echo "                  _(_)_                          wWWWw   _          " >>RunProgramTEST.bat  
echo echo "      @@@@       (_)@(_)   vVVVv     _     @@@@  (___) _(_)_        " >>RunProgramTEST.bat     
echo echo "     @@()@@ wWWWw  (_)\    (___)   _(_)_  @@()@@   Y  (_)@(_)       " >>RunProgramTEST.bat   
echo echo "      @@@@  (___)     `|/    Y    (_)@(_)  @@@@   \|/   (_)\        " >>RunProgramTEST.bat 
echo echo "       /      Y       \|    \|/    /(_)    \|      |/      |        " >>RunProgramTEST.bat
echo echo "    \ |     \ |/       | / \ | /  \|/       |/    \|      \|/       " >>RunProgramTEST.bat
echo echo "     \|//   \\|///  \\\|//\\\|/// \|///  \\\|//  \\|//  \\\|//      " >>RunProgramTEST.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >>RunProgramTEST.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >>RunProgramTEST.bat
echo echo. >>RunProgramTEST.bat
echo %prikaz% >> RunProgramTEST.bat 
::Nebo lze také ::echo|set /p=%CestaPythonu% %CestaProgramu% > RunProgramTEST.bat 
echo exit 0 >> RunProgramTEST.bat

timeout 2 > nul
echo    - Spousteci soubor RunProgram.bat byl vytvoren. Naleznete jej ve zdejsi slozce.
::https://stackoverflow.com/questions/2027070/how-to-concatenate-strings-in-a-windows-batch-file
::@pause
echo.
echo Instalace (pokus o ni) dokoncena. Stisknete jakoukoli klavesu, bys ukoncili instalaci...
pause > nul 
echo Zaviram instalacni program...
timeout 1 > nul
exit 0







::https://www.itninja.com/question/copying-one-line-output-from-a-text-file-into-a-batch-file-as-a-variable
::https://stackoverflow.com/questions/19642622/how-do-i-echo-ascii-art-that-contains-special-characters-in-a-batch-file
::https://patorjk.com/software/taag/#p=testall&h=3&v=3&c=bash&f=Electronic&t=instalation


::https://asciiart.club/
::▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒▒░░░░▒▒░░░░▒▒▒▒░░░░░▒▒▒░░░░░▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▒▒▒▒░░░
::▓▓▓▓▓▓▓▓▓█▓▓▓▓▒▒▒░░▒▒▒'jφ▄░░░░░▒▒▒▒▒░░░`░▒░▒▒▒╢╣▒▒▒▒░░░╢▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░
::▓▓▓▓▓▓▓▓▓▒░░▒▒▒▒░░░▒@░`░▀▓█▓▒¡░▒▓▓▒▒▒░╫▒░▒╢╣▒╣╣▒▒▒▒▒░░▒╣▒░¡▒▒▒▒▒░▒▒▒░░░▒▒▒▒▒░▒▒
::▒░▀▓▓▓▓▓█▓▓░░░▒▒░▒▓▓▓▒Ñ▄;`╙▓██▒▒▒▓█▒░╠▓░▒▒╢▓▓▓▒▒▒▒▒▒░░▒▒░░░▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒░░▒░`
::░▒░░░░▀▓▓▓▓╙░░░░▒╢╢▒▓▓▓▓▓▓▄░╙▓▓▓▒▒▓▓▒▒▒▒▒▒╢▓▓▒░░░▒░░░╜╜▒@▒▒▒▒░▒░░▒▒▒▒░'` ░▒░▒▒`
::░░░░░░░░░░░░░░░░░▒▒▒▒░░╢▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▄▓▓▓▓▌░░░▄▓▓▓▓▓▓▄▄▒▒▒▒░░░░░░░▒▒░`░
::░░░░░░░░▒▒▒░░░░░▒▒▒▒▒µg▒░▒╫▓▓▓▓▒▒▒▒▒░░░░░░░░░▒▒▓▓▓▓▓██████▓▓▓▓▒▒╜╢▒▒░░'░░░░▒▒░¡▒
::░░░░░░░▒▒▒▒░░'└╙░░▒▒░╙╙▒▒▒╣╣▓▓▒░░░▒░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▒░░░▒░░╙▒▒░░░░░▒▒░`░░
::░░░¡¡░░▒▒▒▒▒▒▒▓▓▓▓▓▓▓@▓▓▓▓▓▓▒▒░░░░░░└░░,:░░░░░░░▒▓▓▓▓▓▓▓▄▄▄▄░░░░░░░░╙▒`,░░░░`¡▒░
::░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▀▀▓▓▓▓▓▓▓▓▓▓▒░` '`:.' ` '^=``'░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓@░░.@▒▒░░ ░░░
:: ░▒▒▒▒▒▒▒▒░░░░░▄▓██▓▓▓▓▓▀▀▀░▒@╣@╖╖           ,¿▒╫▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▒▒▒▒`:░░
::¡└░░▒▒▒▒▒░░▄▓▓▓▓▓▓▓▓▓▄φ@▓▓▓▓▓▓▓▓▓░░╥@@╖╓p@g╖╫▓▓▓▓▓▓▓▓▓▓▓▄▒▒▒▓▓▓╨╣╣╣▒▒╫▒║▒▒░░░▒▒▒
::▒,░░░░░░░░░╜▀▀▀▀▀▀▒▒╢▒╣▒▒░░▄████▒▓▓▓▓╣▓▓╣▓▓▓▓▓▓▓▓▓▓▓▓█▓▓▓▓▓▓▓▓▒▒▒░░░░╫░░▒▒`░▒▒▒▒
::▒░░░░░░░` ,¡░`┌░░╫╢@▓▓▓▓▓▒█████▓▓▓▓▓░]▓██▓▒█▓▓▓░▀█▓▓▓▓██▓░▀▀▀▓▓▓▓▀╜░ ░░░░░¡░░░░▒
::▒░░░░░░░¡¡`¡¡¡╥╣╫╣▒╜╜▒▒╜╙▓█▓██▓▓▓▓▓░░▐▓██▓▌▐█▓▓▓▒▒░▀▓▓▓▓▓█▄░░░░░░░░░ ░░░░ `░░░ ¡
::▒▒▒`░▒░░░¡░░░╜╙░░░▒r ░` ░▀▀▀╫▓▓▓▓▒░░░▐▓█▓▓▓,▓█▌▓▓░░░░░░╢▓▓▓▒▒▒▒▒░░░░,░░░░`░░░` ░
::░░▒░░░░░¡└░░░ ░░╫▒▒ :░ :░░░╫▓▓▓▓░▒▒▒▒▒▓██▓▓░░▀▒╫▓░░░░░¡░╟▓▓▌░░▒▒▒░░▒▒▒▒▒ ,▒░░ ,░
::░░░░░░░░░░░░ ¡¡░░░░ ░  ░░░░╫╫▒░░░▒▒▒▒▒╬███▓▒░░░░▓▓░░░░░░░░▓▓▒▒░░░░░╢╢▒╣  ░░░░ ░░
::░░░░░░░░░░░░░░░░▒▒` ▒░'░░░▒▒▒▒▒░░░░▒▒▒░░▀╢▓▌▒▒▒░░░░░░░░▒▒▒░░░░░░░░░░╢▒`,░░░░░░░░
::░░░▒▒▒▒▒▒▒▒▒▒░░▒▒░ ;░`'░▒▒▒░░░░░░▒▒▒▒░``'╟▓▓▒▒░░░▒░▒▒▒▒▒░░░╢▒▒▒▒▒░░`└`└░░░▒▒░▒░░
::░░░░` `└░░░░░░░▒░` ░░  ░░░░░░░░░░░░░░░░`'¡░¡░░▒░░,,░▒▒░░░░░░░▒▒▒▒▒▒░  ¡m░░░░▒▒▒▒