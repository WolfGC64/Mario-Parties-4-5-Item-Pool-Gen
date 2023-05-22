import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from tkinter import filedialog
import os
import csv
import sys
import time
from gecko_code_dictionaries import *

class PrintLogger: 
    def __init__(self, textbox): 
        self.textbox = textbox 
 
    def write(self, text): 
        self.textbox.insert(ctk.END, text) 

    def flush(self):
        pass

#define dictionaries
button_vars = {}
entry_boxes = {}
check_buttons = {}

def clear_selections(tab_name):
    for i, var in enumerate(button_vars[tab_name]):
        entry_boxes[tab_name][i].delete(0, ctk.END)
        entry_boxes[tab_name][i].insert(0, '0')
        check_buttons[tab_name][i].configure(fg_color='grey') # Set the color to a lighter one when not checked
        var.set(0)

def set_button_and_entry(tab_name, index, weight, checked):
    button_vars[tab_name][index].set(checked)
    entry_boxes[tab_name][index].delete(0, ctk.END)
    entry_boxes[tab_name][index].insert(0, str(weight))
    if checked == 0:
        check_buttons[tab_name][index].configure(fg_color='grey')
    else:
        check_buttons[tab_name][index].configure(fg_color='green')

def save_csv(tab_parent):
    file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV Files', '*.csv')])
    if file_path:
        selected_tab = tab_parent.get()  # Get currently selected tab ID
        if selected_tab == "MP4":
            button_text_keys = list(button_texts_mp4.keys())
        elif selected_tab == "MP5":
            button_text_keys = list(button_texts_mp5.keys())

        with open(file_path, 'w', newline='') as file:
            fieldnames = ['name', 'weight', 'on/off']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(button_text_keys)):
                name = button_text_keys[i]
                weight = int(entry_boxes[selected_tab][i].get())
                checked = button_vars[selected_tab][i].get()

                writer.writerow({'name': name, 'weight': weight, 'on/off': checked})


def load_csv(tab_parent):
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    if file_path:
        selected_tab = tab_parent.get()  # Get currently selected tab ID
        if selected_tab == "MP4":
            clear_selections("MP4")
            button_text_keys = list(button_texts_mp4.keys())
        elif selected_tab == "MP5":
            clear_selections("MP5")
            button_text_keys = list(button_texts_mp5.keys())

        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row['name']
                weight = int(row['weight'])
                checked = int(row['on/off'])
                if name in button_text_keys:
                    i = button_text_keys.index(name)
                    set_button_and_entry(selected_tab, i, weight, checked)
                    on_checkbutton_change(i, selected_tab)  # Update checkbox color


def generate_gecko_code(tab_parent, version_var):
    selected_tab = tab_parent.get()  # Get currently selected tab ID
    
    # Draw the appropriate grid
    if selected_tab == "MP5":
        button_text_keys = list(button_texts_mp5.keys())
        entry_boxes_dict = entry_boxes["MP5"]
        button_texts_dict = button_texts_mp5
        if version_var.get() == 3: # PAL
            gecko_code_header = gecko_code_header_mp5_pal
            gecko_code_footer = gecko_code_footer_mp5_pal
        elif version_var.get() == 2: # US
            gecko_code_header = gecko_code_header_mp5_us
            gecko_code_footer = gecko_code_footer_mp5_us
        elif version_var.get() == 1: # JP
            gecko_code_header = gecko_code_header_mp5_jp
            gecko_code_footer = gecko_code_footer_mp5_jp           
        else:
            button_text_keys = []  # Define an empty list if version is not valid
            entry_boxes_dict = {}
            button_texts_dict = {}
            gecko_code_header = ""
            gecko_code_footer = ""
            print("Invalid version!")
            return
    elif selected_tab == "MP4":
        button_text_keys = list(button_texts_mp4.keys())
        entry_boxes_dict = entry_boxes["MP4"]
        button_texts_dict = button_texts_mp4
        if version_var.get() == 3: # PAL
            gecko_code_header = gecko_code_header_mp4_pal
            gecko_code_footer = gecko_code_footer_mp4_pal
        elif version_var.get() == 2: # US
            gecko_code_header = gecko_code_header_mp4_us
            gecko_code_footer = gecko_code_footer_mp4_us
        elif version_var.get() == 1: # JP
            gecko_code_header = gecko_code_header_mp4_jp
            gecko_code_footer = gecko_code_footer_mp4_jp    
        else:
            button_text_keys = []  # Define an empty list if version is not valid
            entry_boxes_dict = {}
            button_texts_dict = {}
            gecko_code_header = ""
            gecko_code_footer = ""
            print("Invalid version!")
            return
    else:
        return

    code_str = ""

    for i in range(len(button_text_keys)):
        if i >= len(entry_boxes_dict):
            break

        current_weight = int(entry_boxes_dict[i].get())
        # Add weight as a 2-byte hexadecimal
        weight_hex = format(current_weight, '04x')
        # Get the item name from button_text_keys
        item_name = button_text_keys[i]
        # Get the item id from button_texts_dict using the item name
        item_id = format(int(button_texts_dict[item_name], 16), '04x')
        # Append to the code string
        code_str += weight_hex + item_id

        # Add a newline character after odd iterations, and a space after even iterations
        if (i+1) % 2 == 0:
            code_str += "\n"
        else:
            code_str += " "
    
    print("\n" + gecko_code_header + code_str + "00000000" + gecko_code_footer)

def on_generate_code(tab_parent, version_var):
    no_weight = 0
    checked_weights = 0
    total_weights = 0
    codeOut.delete('1.0', tk.END)
    selected_tab = tab_parent.get()  # Get currently selected tab ID

    # choose button text keys from mp4 or mp5
    if selected_tab == "MP4":
        button_text_keys = list(button_texts_mp4.keys())
        button_vars_dict = button_vars["MP4"]
        entry_boxes_dict = entry_boxes["MP4"]
        check_buttons_dict = check_buttons["MP4"]
    elif selected_tab == "MP5":
        button_text_keys = list(button_texts_mp5.keys())
        button_vars_dict = button_vars["MP5"]
        entry_boxes_dict = entry_boxes["MP5"]
        check_buttons_dict = check_buttons["MP5"]

    for i, var in enumerate(button_vars_dict):
        current_weight = int(entry_boxes_dict[i].get())
        if check_buttons_dict[i].cget('fg_color') == 'grey':
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
        print(f"Generating code for {selected_tab} JP\n")
    elif selected_value == 2:
        print(f"Generating code for {selected_tab} US\n")
    elif selected_value == 3:
        print(f"Generating code for {selected_tab} PAL\n")

    for i, var in enumerate(button_vars_dict):
        if check_buttons_dict[i].cget('fg_color') == 'grey':
            continue
        current_weight = int(entry_boxes_dict[i].get())
        if current_weight == 0:
            continue
        item_name = button_text_keys[i]  # Get the name of the checked item
        item_percentage = (current_weight / total_weights) * 100
        if item_percentage != 0:
            print(f'{item_name}: {item_percentage:.2f}%')

    checked_buttons = [i + 1 for i, var in enumerate(button_vars_dict) if var.get() == 1]

    if not checked_buttons:
        return
    generate_gecko_code(tab_parent, version_var)


def on_checkbutton_change(index, tab_name):
    if button_vars[tab_name][index].get() == 0:
        entry_boxes[tab_name][index].delete(0, ctk.END)
        entry_boxes[tab_name][index].insert(0, "0")
        check_buttons[tab_name][index].configure(fg_color='grey') # Set the color to a lighter one when not checked
    else:
        check_buttons[tab_name][index].configure(fg_color='green') # Set the color to a darker one when checked

def open_help_window():
    help_window = ctk.CTkToplevel()
    help_window.attributes('-topmost', True)
    help_window.title("About")
    help_window.lift()
    help_window.geometry("300x200")

    frame = ctk.CTkFrame(help_window, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    datafile = "icon.ico"
    if not hasattr(sys, "frozen"):
        datafile = os.path.join(os.path.dirname(__file__), datafile) 
    else:  
        datafile = os.path.join(sys.prefix, "ico/" + datafile)

    img = ctk.CTkImage(Image.open(datafile), size=(64, 64))
    img = ctk.CTkLabel(frame, image=img, text="", height=64, width=64)
    img.pack()

    help_text = "Mario Party 4/5 Item Pool Generator\nWritten by Rain, GUI by Nayla."
    help_label = ctk.CTkLabel(help_window, text=help_text)
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

def clear_options(tab_parent):
    selected_tab = tab_parent.get()  # Get currently selected tab ID
    if selected_tab == "MP4":
        clear_selections("MP4")
    elif selected_tab == "MP5":
        clear_selections("MP5")


# Update the function that creates the grid for a given tab
def create_mp5_grid(parent, root, tab_name):
    num_columns = 3
    if len(button_texts_mp5) % num_columns == 0:
        num_rows = int(len(button_texts_mp5) / num_columns)
    else:
        num_rows = int(len(button_texts_mp5) / num_columns + 1)
    
    button_vars[tab_name] = []
    entry_boxes[tab_name] = []
    check_buttons[tab_name] = []

    for i in range(num_rows):
        for j in range(num_columns):
            index = i * num_columns + j
            button_text_keys = list(button_texts_mp5.keys())
            if index < len(button_texts_mp5):
                var = ctk.IntVar()
                button_vars[tab_name].append(var)

                entry_var = ctk.StringVar()
                entry_var.set('0')  # Set default value to "0"
                vcmd = root.register(limit_size)

                entry = ctk.CTkEntry(master=tab_parent.tab("MP5"), width=30, textvariable=entry_var, validate='key', validatecommand=(vcmd, '%P'))
                entry_boxes[tab_name].append(entry)

                checkbutton = ctk.CTkCheckBox(master=tab_parent.tab("MP5"), text=button_text_keys[index], variable=var, fg_color='grey', command=lambda i=index: on_checkbutton_change(i, tab_name))
                check_buttons[tab_name].append(checkbutton)  # Store the check button

                entry.grid(row=i, column=j*2, padx=5, pady=5, sticky="e")
                checkbutton.grid(row=i, column=j*2+1, padx=5, pady=5, sticky="w")

# Update the function that creates the grid for a given tab
def create_mp4_grid(parent, root, tab_name):
    num_columns = 3
    if len(button_texts_mp4) % num_columns == 0:
        num_rows = int(len(button_texts_mp4) / num_columns)
    else:
        num_rows = int(len(button_texts_mp4) / num_columns + 1)
        
    button_vars[tab_name] = []
    entry_boxes[tab_name] = []
    check_buttons[tab_name] = []

    for i in range(num_rows):
        for j in range(num_columns):
            index = i * num_columns + j
            button_text_keys = list(button_texts_mp4.keys())
            if index < len(button_texts_mp4):
                var = ctk.IntVar()
                button_vars[tab_name].append(var)

                entry_var = ctk.StringVar()
                entry_var.set('0')  # Set default value to "0"
                vcmd = root.register(limit_size)

                entry = ctk.CTkEntry(master=tab_parent.tab("MP4"), width=30, textvariable=entry_var, validate='key', validatecommand=(vcmd, '%P'))
                entry_boxes[tab_name].append(entry)

                checkbutton = ctk.CTkCheckBox(master=tab_parent.tab("MP4"), text=button_text_keys[index], variable=var, fg_color='grey', command=lambda i=index: on_checkbutton_change(i, tab_name))
                check_buttons[tab_name].append(checkbutton)  # Store the check button

                entry.grid(row=i, column=j*2, padx=5, pady=5, sticky="e")
                checkbutton.grid(row=i, column=j*2+1, padx=5, pady=5, sticky="w")
                
def on_tab_changed(event, root):
    selected_tab = event.widget.select()
    selected_tab = event.widget.tab(selected_tab, 'text')

    # Get the frame of the selected tab
    selected_frame = event.widget.nametowidget(selected_tab)

    # Clear grid in selected tab
    for widget in selected_frame.winfo_children():
        widget.destroy()

    # Create new grid based on the selected tab
    if selected_tab == "MP5":
        create_mp5_grid(selected_frame, root, "MP5")
    elif selected_tab == "MP4":
        create_mp4_grid(selected_frame, root, "MP4")




def create_gui():
    global button_vars
    global entry_boxes

    ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

    root = ctk.CTk()
    root.title("Mario Party 4/5 Item Pool Generator")

    # Frozen Icon for Executable
    datafile = "ico/icon.ico"
    datafileFrozen = "icon.ico"
    if not hasattr(sys, "frozen"):
        datafile = os.path.join(os.path.dirname(__file__), datafile) 
    else:  
        datafile = os.path.join(sys.prefix, datafileFrozen)
   
    root.iconbitmap(datafile)

    # No Resizing
    root.resizable(False, False)

    # Set default size of window to be large enough for mp4/mp5 item grids
    root.geometry("800x380")

    main_frame = ctk.CTkFrame(root)  # CTkFrame to hold version_frame and tab_parent
    main_frame.grid()

    # Create a button frame to hold the buttons
    button_frame = ctk.CTkFrame(main_frame)
    button_frame.grid(row=0)

    # Create 'Save CSV' button and add to button_frame
    save_button = ctk.CTkButton(button_frame, text="Save CSV", command=lambda: save_csv(tab_parent))
    save_button.grid(row=0, column=0)

    # Create 'Load CSV' button and add to button_frame
    load_button = ctk.CTkButton(button_frame, text="Load CSV", command=lambda: load_csv(tab_parent))
    load_button.grid(row=0, column=1)

    # Create 'Clear All' button and add to button_frame
    clear_button = ctk.CTkButton(button_frame, text="Clear All", command=lambda: clear_options(tab_parent))
    clear_button.grid(row=0, column=2)

    # Create Code Output Box
    global codeOut
    codeOut = ctk.CTkTextbox(root, width=258, height=378)
    codeOut.bind("<Key>", lambda e: "break")
    codeOut.grid(row=0, column=2, sticky="e")
    printlogger = PrintLogger(codeOut) 
    sys.stdout = printlogger

    # Create version radiobuttons
    version_var = ctk.IntVar(value=1)  # Set default value to 1 (JP)
    version_frame = ctk.CTkFrame(main_frame)
    version_frame.grid()
    version1_button = ctk.CTkRadioButton(version_frame, text="NTSC-J", variable=version_var, value=1)
    version1_button.grid(row=1, column=0)
    version2_button = ctk.CTkRadioButton(version_frame, text="NTSC-U", variable=version_var, value=2)
    version2_button.grid(row=1, column=1)
    version3_button = ctk.CTkRadioButton(version_frame, text="PAL", variable=version_var, value=3)
    version3_button.grid(row=1, column=2)

    global tab_parent
    tab_parent = ctk.CTkTabview(main_frame)  # Place inside main_frame

    mp4_tab = ctk.CTkFrame(tab_parent)
    mp5_tab = ctk.CTkFrame(tab_parent)
    tab_parent.add("MP4")
    tab_parent.add("MP5")
    tab_parent.grid(row=2, column=0)

    # Create a button frame to hold the buttons
    gen_code_button = ctk.CTkFrame(main_frame)
    gen_code_button.grid(row=3, column=0)

    # Create 'Generate Gecko Code' button and add to gen_code_button
    generate_button = ctk.CTkButton(gen_code_button, text="Generate Gecko Code", command=lambda: on_generate_code(tab_parent, version_var))
    generate_button.grid(row=3, column=1)

    # Store tabs in a dictionary
    tab_parent.tabs = {"MP4": mp4_tab, "MP5": mp5_tab}

    create_mp4_grid(mp4_tab, root, "MP4")
    create_mp5_grid(mp5_tab, root, "MP5")
    #tab_parent.bind("", lambda event: on_tab_changed(event, root))
    root.mainloop()


def validate_input(value):
    if len(value) > 3:  # Limit input to 3 characters
        return False
    if not value.isdigit():  # Only allow numeric input
        return False
    return True

if __name__ == "__main__":
    create_gui()