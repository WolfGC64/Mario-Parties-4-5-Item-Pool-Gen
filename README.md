# Mario Party 4 5 Item Pool Gen
This program generates a gecko code based on the selected item/weights given for mp4/mp5<br>
This allows you to specify exactly what items you want to appear and the odds of getting each individual item<br>
The odds are printed as perctanges when you hit `Generate Gecko Code`<br>

There is a custom tkinter build, and a normal tkinter build<br>
To build the custom tkinter version, run `./build.bat` in powershell. You can then run the program with `./bin/MP4-MP5-ItemPoolGen.exe`<br>

To run the normal tkinter build, simply run `python3 ./main.alt.py`<br>

# Currently supported Games/Versions
Mario party 4 supports US/PAL<br>
Mario party 5 only supports PAL<br>

# Known Issues
As of commit `2aeb8710dc41519429a9cb139a7d67ce29f7d9b6`, the normal tkinter build works fine<br>
The custom tkinter build has issues loading a csv if you are not on the correct tab<br>
