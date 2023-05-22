@echo off
rmdir bin /s /q
pyinstaller --onefile --icon=ico/icon.ico --noupx --noconsole main.py --add-binary="ico/icon.ico;." --add-data "C:\Users\Nora\scoop\apps\python\current\Lib\site-packages\customtkinter;customtkinter/"
REN dist bin
cd bin && REN main.exe MP5CapsulePoolGen.exe && cd ..
PAUSE