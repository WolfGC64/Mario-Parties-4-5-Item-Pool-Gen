# Mario Party 4-5 Item Pool Gen
This program generates a gecko code based on the selected item/weights given for mp4/mp5<br>
This allows you to specify exactly what items you want to appear and the odds of getting each individual item<br>
There is a custom tkinter build, and a normal tkinter build<br>
To build the custom tkinter version, run `./build.bat` in powershell. You can then run the program with `./bin/MP4-MP5-ItemPoolGen.exe`<br>
To run the normal tkinter build, simply run `python3 ./main.alt.py`<br>

# Usage
You will firstly need python 3 https://www.python.org/downloads/<br>
As of this readme, the version is 3.11<br>
After python has installed, simply double click the `main_alt.py` file<br>
Customize the items you want by checking them and then adding weights in each textbox<br>
The weights are calculated by adding all the values togther, then dividing by the weights given for each item<br>
Once you select a game, region, and items you want to make a code for, hit `Generate Gecko Code`<br>
The console will print some information about the odds of each item, and the gecko code that was generated<br>

# Currently supported Games/Versions
Mario Party 4 supports US/PAL<br>
Mario Party 5 supports US/PAL<br>

# Known Issues
As of commit `2aeb8710dc41519429a9cb139a7d67ce29f7d9b6`, the normal tkinter build works fine<br>
The custom tkinter build has issues loading a csv if you are not on the correct tab<br>
