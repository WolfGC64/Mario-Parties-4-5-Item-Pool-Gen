import tkinter as tk
from tkinter import ttk, Label
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import PhotoImage
import os
import csv
import time
from gecko_code_dictionaries import *


# Global variables
# Define dictionaries
button_vars = {}
weight_boxes = {}
price_boxes = {}
check_buttons = {}

# Tabs
mp4_tab = None
mp5_tab = None
mp6_tab = None

def clear_selections(tab_name):
    for i, var in enumerate(button_vars[tab_name]):
        weight_boxes[tab_name][i].delete(0, tk.END)
        weight_boxes[tab_name][i].insert(0, '0')
        price_boxes[tab_name][i].delete(0, tk.END)
        price_boxes[tab_name][i].insert(0, '0')
        check_buttons[tab_name][i].config(fg='grey') # Set the color to a lighter one when not checked
        var.set(0)

def set_button_and_entry(tab_name, index, weight, price, checked):
    button_vars[tab_name][index].set(checked)
    weight_boxes[tab_name][index].delete(0, tk.END)
    weight_boxes[tab_name][index].insert(0, str(weight))
    price_boxes[tab_name][index].delete(0, tk.END)
    price_boxes[tab_name][index].insert(0, str(price))
    if checked == 0:
        check_buttons[tab_name][index].config(fg='grey')
    else:
        check_buttons[tab_name][index].config(fg='black')

def save_csv(tab_parent, version_var):
    file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV Files', '*.csv')])
    if file_path:
        selected_tab = tab_parent.select()  # Get currently selected tab ID
        selected_tab_text = tab_parent.tab(selected_tab, "text")  # Get the text of the selected tab
        if selected_tab_text == "MP4":
            button_text_keys = list(button_texts_mp4.keys())
        elif selected_tab_text == "MP5":
            button_text_keys = list(button_texts_mp5.keys())
        elif selected_tab_text == "MP6":
            button_text_keys = list(button_texts_mp6.keys())

        with open(file_path, 'w', newline='') as file:
            fieldnames = ['name', 'weight', 'price', 'on/off', 'game', 'version']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(button_text_keys)):
                name = button_text_keys[i]
                weight = int(weight_boxes[selected_tab_text][i].get())
                price = int(price_boxes[selected_tab_text][i].get())
                checked = button_vars[selected_tab_text][i].get()
                version = version_var.get()
                writer.writerow({'name': name, 'weight': weight, 'price': price, 'on/off': checked, 'game': selected_tab_text, 'version': version})


def load_csv(tab_parent, version_var):
    verList = ["JP", "US", "PAL"]
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    if file_path:
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            first_row = next(csv_reader)  # Read the first row
            
            game = first_row['game']
            version = first_row['version']
            verInt = int(first_row['version'])
            print(f"Game: {game}, Version: {verList[verInt-1]}")  # Print game and version

            # Process the first row separately
            if game == "MP4":
                version_var.set(version)
                tab_parent.select(mp4_tab)
                clear_selections("MP4")
                button_text_keys = list(button_texts_mp4.keys())

            elif game == "MP5":
                version_var.set(version)
                tab_parent.select(mp5_tab)
                clear_selections("MP5")
                button_text_keys = list(button_texts_mp5.keys())

            elif game == "MP6":
                version_var.set(version)
                tab_parent.select(mp6_tab)
                clear_selections("MP6")
                button_text_keys = list(button_texts_mp6.keys())

            # Update the grid for the selected tab
            tab_parent.update()

            # Process the remaining rows in the CSV
            for row in [first_row] + list(csv_reader):
                name = row['name']
                weight = int(row['weight'])
                price = int(row['price'])
                checked = int(row['on/off'])
                if name in button_text_keys:
                    i = button_text_keys.index(name)
                    set_button_and_entry(game, i, weight, price, checked)
                    on_checkbutton_change(i, game)  # Update checkbox color               

def generate_gecko_code(tab_parent, version_var):
    selected_tab = tab_parent.select()  # Get currently selected tab ID
    selected_tab_text = tab_parent.tab(selected_tab, "text")  # Get the text of the selected tab
    
    # Draw the appropriate grid
    if selected_tab_text == "MP5":
        button_text_keys = list(button_texts_mp5.keys())
        weight_boxes_dict = weight_boxes["MP5"]
        price_boxes_dict = price_boxes["MP5"]
        button_texts_dict = button_texts_mp5
        if version_var.get() == 3: # PAL
            gecko_code_header = gecko_code_header_mp5_pal
            gecko_code_footer = gecko_code_footer_mp5_pal
            price_base_addr = 0   
        elif version_var.get() == 2: # US
            gecko_code_header = gecko_code_header_mp5_us
            gecko_code_footer = gecko_code_footer_mp5_us
            price_base_addr = 0   
        elif version_var.get() == 1: # JP
            gecko_code_header = gecko_code_header_mp5_jp
            gecko_code_footer = gecko_code_footer_mp5_jp
            price_base_addr = 0           
        else:
            button_text_keys = []  # Define an empty list if version is not valid
            weight_boxes_dict = {}
            button_texts_dict = {}
            gecko_code_header = ""
            gecko_code_footer = ""
            print("Invalid version!")
            return
    elif selected_tab_text == "MP4":
        button_text_keys = list(button_texts_mp4.keys())
        weight_boxes_dict = weight_boxes["MP4"]
        button_texts_dict = button_texts_mp4
        price_boxes_dict = price_boxes["MP4"]
        if version_var.get() == 3: # PAL
            gecko_code_header = gecko_code_header_mp4_pal
            gecko_code_footer = gecko_code_footer_mp4_pal
            price_base_addr = 0x001570B4
        elif version_var.get() == 2: # US
            gecko_code_header = gecko_code_header_mp4_us
            gecko_code_footer = gecko_code_footer_mp4_us
            price_base_addr = 0x00139D2C
        elif version_var.get() == 1: # JP
            gecko_code_header = gecko_code_header_mp4_jp
            gecko_code_footer = gecko_code_footer_mp4_jp
    elif selected_tab_text == "MP6":
        button_text_keys = list(button_texts_mp6.keys())
        weight_boxes_dict = weight_boxes["MP6"]
        button_texts_dict = button_texts_mp6
        price_boxes_dict = price_boxes["MP6"]
        if version_var.get() == 3: # PAL
            gecko_code_header = gecko_code_header_mp6_pal
            gecko_code_footer = gecko_code_footer_mp6_pal
            price_base_addr = 0x001570B4 #TODO
        elif version_var.get() == 2: # US
            gecko_code_header = gecko_code_header_mp6_us
            gecko_code_footer = gecko_code_footer_mp6_us
            price_base_addr = 0x00139D2C #TODO
        elif version_var.get() == 1: # JP
            gecko_code_header = gecko_code_header_mp6_jp
            gecko_code_footer = gecko_code_footer_mp6_jp 
        else:
            button_text_keys = []  # Define an empty list if version is not valid
            weight_boxes_dict = {}
            price_boxes_dict = {}
            button_texts_dict = {}
            gecko_code_header = ""
            gecko_code_footer = ""
            print("Invalid version!")
            return
    else:
        return

    code_str = ""
    price_str = ""

    if selected_tab_text == "MP6":
        for i in range(len(button_text_keys)):
            if i >= len(weight_boxes_dict):
                break

            # Add weight as a 2-byte hexadecimal
            current_weight = int(weight_boxes_dict[i].get())
            weight_hex = format(current_weight, '04x')

            # Add coin price as 2 byte hexadecimal integer
            current_price = int(price_boxes_dict[i].get())
            price = format(current_price, '02x')

            # Get the item name from button_text_keys
            item_name = button_text_keys[i]

            # Get the item id from button_texts_dict using the item name
            item_id = format(int(button_texts_dict[item_name], 16), '02x')

            # Append to the code string
            code_str += weight_hex + item_id + price
            
            if (price_base_addr != 0):
                price_str += str(hex(price_base_addr + int(item_id, 16)))[2:].upper().zfill(8) + " " + price.upper() + "\n"
            
            #price_str += price

            # Add a newline character after odd iterations, and a space after even iterations
            if (i+1) % 2 == 0:
                code_str += "\n"
            else:
                code_str += " "
        
        print("\n" + gecko_code_header + code_str + "00000000" + gecko_code_footer)
    else:
        for i in range(len(button_text_keys)):
            if i >= len(weight_boxes_dict):
                break

            # Add weight as a 2-byte hexadecimal
            current_weight = int(weight_boxes_dict[i].get())
            weight_hex = format(current_weight, '04x')

            # Add coin price as 2 byte hexadecimal integer
            current_price = int(price_boxes_dict[i].get())
            price = format(current_price, '08x')

            # Get the item name from button_text_keys
            item_name = button_text_keys[i]

            # Get the item id from button_texts_dict using the item name
            item_id = format(int(button_texts_dict[item_name], 16), '04x')

            # Append to the code string
            code_str += weight_hex + item_id
            
            if (price_base_addr != 0):
                price_str += str(hex(price_base_addr + int(item_id, 16)))[2:].upper().zfill(8) + " " + price.upper() + "\n"
            
            #price_str += price

            # Add a newline character after odd iterations, and a space after even iterations
            if (i+1) % 2 == 0:
                code_str += "\n"
            else:
                code_str += " "
        
        print("\n" + gecko_code_header + code_str + "00000000" + gecko_code_footer)
        if (price_base_addr != 0):
            print(f"{price_str}")

def on_generate_code(tab_parent, version_var):
    no_weight = 0
    checked_weights = 0
    total_weights = 0
    #clear twice to avoid powershell leaving stuff in the window
    os.system('cls')  # Clear console for Windows
    os.system('cls')  # Clear console for Windows

    selected_tab = tab_parent.select()  # Get currently selected tab ID
    selected_tab_text = tab_parent.tab(selected_tab, "text")  # Get the text of the selected tab

    # choose button text keys from mp4, mp5, or mp6
    if selected_tab_text == "MP4":
        button_text_keys = list(button_texts_mp4.keys())
        button_vars_dict = button_vars["MP4"]
        weight_boxes_dict = weight_boxes["MP4"]
        check_buttons_dict = check_buttons["MP4"]
        price_boxes_dict = price_boxes["MP4"]
    elif selected_tab_text == "MP5":
        button_text_keys = list(button_texts_mp5.keys())
        button_vars_dict = button_vars["MP5"]
        weight_boxes_dict = weight_boxes["MP5"]
        check_buttons_dict = check_buttons["MP5"]
        price_boxes_dict = price_boxes["MP5"]
    elif selected_tab_text == "MP6":
        button_text_keys = list(button_texts_mp6.keys())
        button_vars_dict = button_vars["MP6"]
        weight_boxes_dict = weight_boxes["MP6"]
        check_buttons_dict = check_buttons["MP6"]
        price_boxes_dict = price_boxes["MP6"]

    for i, var in enumerate(button_vars_dict):
        current_weight = int(weight_boxes_dict[i].get())
        if check_buttons_dict[i].cget('fg') == 'grey':
            continue
        total_weights += current_weight
        if var.get() == 1:
            if current_weight == 0:
                no_weight = 1
                print(f"{button_text_keys[i]} has no weight!")
            else:
                checked_weights += current_weight
    if total_weights == 0:
        print("Weight Total was 0!")
        return
    if no_weight == 1:
        print("All selected items must have weights!")
        return

    selected_value = version_var.get()

    if selected_value == 1:
        print(f"Generating code for {selected_tab_text} JP")
    elif selected_value == 2:
        print(f"Generating code for {selected_tab_text} US")
    elif selected_value == 3:
        print(f"Generating code for {selected_tab_text} PAL")

    for i, var in enumerate(button_vars_dict):
        if check_buttons_dict[i].cget('fg') == 'grey':
            continue
        current_weight = int(weight_boxes_dict[i].get())
        if current_weight == 0:
            continue
        item_name = button_text_keys[i]  # Get the name of the checked item
        item_percentage = (current_weight / total_weights) * 100
        if item_percentage != 0:
            print(f'  {item_name}: {item_percentage:.2f}%')

    checked_buttons = [i + 1 for i, var in enumerate(button_vars_dict) if var.get() == 1]

    if not checked_buttons:
        return
    generate_gecko_code(tab_parent, version_var)


def on_checkbutton_change(index, tab_name):
    if button_vars[tab_name][index].get() == 0:
        weight_boxes[tab_name][index].delete(0, tk.END)
        weight_boxes[tab_name][index].insert(0, "0")
        price_boxes[tab_name][index].delete(0, tk.END)
        price_boxes[tab_name][index].insert(0, "0")
        check_buttons[tab_name][index].config(fg='grey') # Set the color to a lighter one when not checked
    else:
        check_buttons[tab_name][index].config(fg='black') # Set the color to a darker one when checked

def open_help_window():
    help_window = tk.Toplevel()
    help_window.title("Help")
    help_window.geometry("300x200")

    help_text = "Mario Party 4/5 Item Pool Generator\nWritten by Rain, GUI by Nayla."
    help_label = tk.Label(help_window, text=help_text)
    help_label.pack()

def limit_size(P):
    if len(P) > 3: 
        return False
    if len(P) < 1: # Allow empty entries
        return True
    if P.isdigit() and 0 <= int(P) <= 999: # Check for a valid integer within the range
        return True
    else:
        return False

def create_mp6_grid(parent, root, tab_name):
    # Load the icons
    weight_icon = PhotoImage(file="ico/price_icon_small.png")
    price_icon = PhotoImage(file="ico/weight_icon_small.png")

    num_columns = 3
    if len(button_texts_mp6) % num_columns == 0:
        num_rows = int(len(button_texts_mp6) / num_columns)
    else:
        num_rows = int(len(button_texts_mp6) / num_columns + 1)
    
    button_vars[tab_name] = []
    weight_boxes[tab_name] = []
    price_boxes[tab_name] = []
    check_buttons[tab_name] = []

    for i in range(num_rows):
        for j in range(num_columns):
            index = i * num_columns + j
            button_text_keys = list(button_texts_mp6.keys())
            if index < len(button_texts_mp6):
                var = tk.IntVar()
                button_vars[tab_name].append(var)

                entry_var = tk.StringVar()
                entry_var.set('0')  # Set default value to "0"
                price_var = tk.StringVar()
                price_var.set('0')  # Set default value to "0"
                vcmd = root.register(limit_size)

                # Create label with icon and place it above the entry field
                weight_icon_label = tk.Label(parent, image=weight_icon)
                weight_icon_label.image = weight_icon  # Keep a reference to the image
                weight_icon_label.grid(row=i, column=j*2, pady=5, sticky="e")

                entry = tk.Entry(parent, width=3, textvariable=entry_var, validate='key', validatecommand=(vcmd, '%P'))
                weight_boxes[tab_name].append(entry)

                # Create label with icon and place it above the price field
                price_icon_label = tk.Label(parent, image=price_icon)
                price_icon_label.image = price_icon  # Keep a reference to the image
                price_icon_label.grid(row=i, column=j*2, pady=5, sticky="e")

                price = tk.Entry(parent, width=3, textvariable=price_var, validate='key', validatecommand=(vcmd, '%P'))
                price_boxes[tab_name].append(price)

                checkbutton = tk.Checkbutton(parent, text=button_text_keys[index], variable=var, fg='grey', command=lambda i=index: on_checkbutton_change(i, tab_name))
                check_buttons[tab_name].append(checkbutton)  # Store the check button

                entry.grid(row=i+1, column=j*2, padx=20, pady=5, sticky="e")
                price.grid(row=i+1, column=j*2, padx=0, pady=5, sticky="e")
                checkbutton.grid(row=i+1, column=j*2+1, padx=5, pady=5, sticky="w")


# Update the function that creates the grid for a given tab
def create_mp5_grid(parent, root, tab_name):
    num_columns = 3
    if len(button_texts_mp5) % num_columns == 0:
        num_rows = int(len(button_texts_mp5) / num_columns)
    else:
        num_rows = int(len(button_texts_mp5) / num_columns + 1)
    
    button_vars[tab_name] = []
    weight_boxes[tab_name] = []
    price_boxes[tab_name] = []
    check_buttons[tab_name] = []

    for i in range(num_rows):
        for j in range(num_columns):
            index = i * num_columns + j
            button_text_keys = list(button_texts_mp5.keys())
            if index < len(button_texts_mp5):
                var = tk.IntVar()
                button_vars[tab_name].append(var)

                entry_var = tk.StringVar()
                entry_var.set('0')  # Set default value to "0"
                price_var = tk.StringVar()
                price_var.set('0')  # Set default value to "0"
                vcmd = root.register(limit_size)

                entry = tk.Entry(parent, width=3, textvariable=entry_var, validate='key', validatecommand=(vcmd, '%P'))
                weight_boxes[tab_name].append(entry)

                price = tk.Entry(parent, width=3, textvariable=price_var, validate='key', validatecommand=(vcmd, '%P'))
                price_boxes[tab_name].append(price)

                checkbutton = tk.Checkbutton(parent, text=button_text_keys[index], variable=var, fg='grey', command=lambda i=index: on_checkbutton_change(i, tab_name))
                check_buttons[tab_name].append(checkbutton)  # Store the check button

                entry.grid(row=i, column=j*2, padx=20, pady=5, sticky="e")
                price.grid(row=i, column=j*2, padx=0, pady=5, sticky="e")
                checkbutton.grid(row=i, column=j*2+1, padx=5, pady=5, sticky="w")

# Update the function that creates the grid for a given tab
def create_mp4_grid(parent, root, tab_name):
    num_columns = 3
    if len(button_texts_mp4) % num_columns == 0:
        num_rows = int(len(button_texts_mp4) / num_columns)
    else:
        num_rows = int(len(button_texts_mp4) / num_columns + 1)
        
    button_vars[tab_name] = []
    weight_boxes[tab_name] = []
    price_boxes[tab_name] = []
    check_buttons[tab_name] = []

    for i in range(num_rows):
        for j in range(num_columns):
            index = i * num_columns + j
            button_text_keys = list(button_texts_mp4.keys())
            if index < len(button_texts_mp4):
                var = tk.IntVar()
                button_vars[tab_name].append(var)

                entry_var = tk.StringVar()
                entry_var.set('0')  # Set default value to "0"
                price_var = tk.StringVar()
                price_var.set('0')  # Set default value to "0"
                vcmd = root.register(limit_size)

                entry = tk.Entry(parent, width=3, textvariable=entry_var, validate='key', validatecommand=(vcmd, '%P'))
                weight_boxes[tab_name].append(entry)

                price = tk.Entry(parent, width=3, textvariable=price_var, validate='key', validatecommand=(vcmd, '%P'))
                price_boxes[tab_name].append(price)

                checkbutton = tk.Checkbutton(parent, text=button_text_keys[index], variable=var, fg='grey', command=lambda i=index: on_checkbutton_change(i, tab_name))
                check_buttons[tab_name].append(checkbutton)  # Store the check button

                entry.grid(row=i, column=j*2, padx=20, pady=5, sticky="e")
                price.grid(row=i, column=j*2, padx=0, pady=5, sticky="e")
                checkbutton.grid(row=i, column=j*2+1, padx=5, pady=5, sticky="w")


def on_tab_changed(event, root):
    selected_tab = event.widget.select()
    selected_tab_text = event.widget.tab(selected_tab, 'text')

    # Get the frame of the selected tab
    selected_frame = event.widget.nametowidget(selected_tab)

    # Clear grid in selected tab
    for widget in selected_frame.winfo_children():
        widget.destroy()

    # Create new grid based on the selected tab
    if selected_tab_text == "MP4":
        create_mp4_grid(selected_frame, root, "MP4")
    elif selected_tab_text == "MP5":
        create_mp5_grid(selected_frame, root, "MP5")
    elif selected_tab_text == "MP6":
        create_mp6_grid(selected_frame, root, "MP6")


def create_gui():
    global button_vars
    global weight_boxes
    global price_boxes
    global mp4_tab
    global mp5_tab
    global mp6_tab

    root = tk.Tk()
    root.title("Mario Party 4/5 Item Pool Generator")
    root.iconbitmap("ico/icon.ico")

    # Set default size of window to be large enough for mp4/mp5 item grids
    root.geometry("600x550")  # Width x Height in pixels

    main_frame = tk.Frame(root)  # Frame to hold version_frame and tab_parent
    main_frame.pack()

    # Create version_var for save/load csv
    version_var = tk.IntVar(value=2)  # Set default value to 2 (US)

    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=lambda: clear_options(tab_parent))
    filemenu.add_command(label="Open", command=lambda: load_csv(tab_parent, version_var))
    filemenu.add_command(label="Save", command=lambda: save_csv(tab_parent, version_var))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About...", command=open_help_window)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)

    # Create version radiobuttons
    version_frame = tk.Frame(main_frame)
    version_frame.pack()
    version1_button = tk.Radiobutton(version_frame, text="JP", variable=version_var, value=1)
    version1_button.pack(side=tk.LEFT)
    version2_button = tk.Radiobutton(version_frame, text="US", variable=version_var, value=2)
    version2_button.pack(side=tk.LEFT)
    version3_button = tk.Radiobutton(version_frame, text="PAL", variable=version_var, value=3)
    version3_button.pack(side=tk.LEFT)

    tab_parent = ttk.Notebook(main_frame)  # Place inside main_frame

    mp4_tab = ttk.Frame(tab_parent)
    mp5_tab = ttk.Frame(tab_parent)
    mp6_tab = ttk.Frame(tab_parent)
    tab_parent.add(mp4_tab, text="MP4")
    tab_parent.add(mp5_tab, text="MP5")
    tab_parent.add(mp6_tab, text="MP6")
    tab_parent.pack(expand=1, fill='both')
    
    # Store tabs in a dictionary
    tab_parent.tabs = {
        "MP4": mp4_tab,
        "MP5": mp5_tab,
        "MP6": mp6_tab
    }

    # Create a button frame to hold the buttons
    gen_code_button = tk.Frame(main_frame)
    gen_code_button.pack(side=tk.TOP, fill=tk.X)

    # Create 'Generate Gecko Code' button and add to generate_button
    generate_button = tk.Button(gen_code_button, text="Generate Gecko Code", command=lambda: on_generate_code(tab_parent, version_var))
    generate_button.pack(side=tk.LEFT)


    create_mp4_grid(mp4_tab, root, "MP4")
    create_mp5_grid(mp5_tab, root, "MP5")
    create_mp6_grid(mp6_tab, root, "MP6")
    tab_parent.bind("<<NotebookTabChanged>>", lambda event: on_tab_changed(event, root))
    root.mainloop()


def validate_input(value):
    if len(value) > 3:  # Limit input to 3 characters
        return False
    if not value.isdigit():  # Only allow numeric input
        return False
    return True

if __name__ == "__main__":
    create_gui()