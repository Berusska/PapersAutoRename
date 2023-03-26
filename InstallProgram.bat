title Instalace Programu
@echo off
cls
::color 2
echo """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
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
echo     Zvolte napr. moznost "Install now".
timeout 2 > nul 
%~dp0\Source\python-3.11.2-amd64.exe
echo     K pokracovani stisknete jakoukoli klavesu.
pause > nul
echo.
echo Aktualne mate Python na ceste:
echo ________________________________________________________________________________________________________________________
echo.
where python
echo ________________________________________________________________________________________________________________________
echo     Pokud tomu je tak a tedy je Python nainstalovan, stisknete Enter.
pause > nul
echo.
echo Nyni se Vam nainstaluji potrebne python moduly.
echo ________________________________________________________________________________________________________________________
echo.
::%~dp0\Source\InstallModules.bat
pip install pathlib
pip install pyquery
pip install pyperclip
pip install keyboard
pip install PySimpleGUI
pip install pyautogui
pip install regex
pip install textwrap3
pip install urllib3
echo _________________________________________________________________________________________________________________________
echo     Moduly nainstalovany. Pokud nektery ne, doreste jeho instalaci dodatecne.
echo     Nyni stisknete libovolnou klavesu.
echo.
pause > nul
echo.
echo Nyni se zjistuje cesta zdrojoveho kodu programu PapersRename.
timeout 2 > nul

::Následující najde python skript a uloží jeho cestu; vyhledává i v podsložkách
for /r ./ %%a in (*) do if "%%~nxa"=="PapersRename.py" set CestaProgramu=%%~dpnxa

echo     Aktualni cesta zdrojoveho kodu je:
if defined CestaProgramu (echo          %CestaProgramu%) else (echo      File not found)
::https://devblogs.microsoft.com/oldnewthing/20120731-00/?p=7003
::https://stackoverflow.com/questions/13876771/find-file-and-return-full-path-using-a-batch-file


echo.
echo Nyni se vytvori spousteci soubor pro program.
set CestaPythonu=python 
set prikaz=%CestaPythonu% %CestaProgramu%
::echo %prikaz%


echo echo off >RunProgram.bat
echo cls >>RunProgram.bat
echo echo.    >>RunProgram.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >>RunProgram.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >>RunProgram.bat
echo echo """                                                                                            """ >>RunProgram.bat
echo echo """                     __,               , _                                                  """ >>RunProgram.bat
echo echo """                    /  |       _|_  _ /|/ \  _        _,           _                        """ >>RunProgram.bat
echo echo """                   |   |  |  |  |  / \_|__/ |/ /|/|  / |  /|/|/|  |/                        """ >>RunProgram.bat
echo echo """                    \_/\_/ \/|_/|_/\_/ | \_/|_/ | |_/\/|_/ | | |_/|_/                       """ >>RunProgram.bat
echo echo """                    ()  _  o  _        _   _     _,   ,_ _|_ o  _  |\  _                    """ >>RunProgram.bat
echo echo """                    /\ /   | |/ /|/|  /   |/    / |  /  | |  | /   |/ |/                    """ >>RunProgram.bat
echo echo """                   /(_)\__/|/|_/ | |_/\__/|_/   \/|_/   |/|_/|/\__/|_/|_/                   """ >>RunProgram.bat
echo echo """                                                                                            """ >>RunProgram.bat
echo echo """--------------------------------------------------------------------------------------------""" >>RunProgram.bat
echo echo """                                                                       by Tomas Spurny      """ >>RunProgram.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >>RunProgram.bat
echo echo """                      _                                                          .--.       """ >>RunProgram.bat
echo echo """                    _(_)_                                 wWWWw      _         .'_\/_'.     """ >>RunProgram.bat
echo echo """    @@@@           (_)@(_)     vVVVv       _      @@@@    (___)    _(_)_       '. /\ .'     """ >>RunProgram.bat
echo echo """   @@()@@   wWWWw    (_)\      (___)     _(_)_   @@()@@     Y     (_)@(_)         ||        """ >>RunProgram.bat
echo echo """    @@@@    (___)       `|/      Y      (_)@(_)   @@@@     \|/      (_)\          || /\     """ >>RunProgram.bat
echo echo """     /        Y         \|      \|/      /(_)     \|        |/         |       /\ ||//\     """ >>RunProgram.bat
echo echo """  \ |       \ |/         | /   \ | /    \|/        |/      \|         \|/      /\\||/_/     """ >>RunProgram.bat
echo echo """   \|//     \\|//  /  \\\|//  \\\|///   \|///   \\\|//    \\|//     \\\|//       \||/       """ >>RunProgram.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >>RunProgram.bat
echo echo """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" >>RunProgram.bat
echo echo. >>RunProgram.bat
echo %prikaz% >> RunProgram.bat 
::Nebo lze také ::echo|set /p=%CestaPythonu% %CestaProgramu% > RunProgram.bat 
echo exit 0 >> RunProgram.bat

timeout 2 > nul
echo     Spousteci soubor RunProgram.bat byl vytvoren. Naleznete jej ve zdejsi slozce.
::https://stackoverflow.com/questions/2027070/how-to-concatenate-strings-in-a-windows-batch-file
::@pause
echo.
echo ........................................................................................................................
echo Instalace (pokus o ni) dokoncena. Stisknete jakoukoli klavesu, by jste ukoncili instalaci...
pause > nul 
echo Zaviram instalacni program...
timeout 2 > nul
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


::https://stackoverflow.com/questions/2048509/how-to-echo-with-different-colors-in-the-windows-command-line