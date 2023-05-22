import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import csv
import time
from gecko_code_dictionaries import *

#define dictionaries
button_vars = {}
entry_boxes = {}
check_buttons = {}

def clear_selections(tab_name):
    for i, var in enumerate(button_vars[tab_name]):
        entry_boxes[tab_name][i].delete(0, tk.END)
        entry_boxes[tab_name][i].insert(0, '0')
        check_buttons[tab_name][i].config(fg='grey') # Set the color to a lighter one when not checked
        var.set(0)

def set_button_and_entry(tab_name, index, weight, checked):
    button_vars[tab_name][index].set(checked)
    entry_boxes[tab_name][index].delete(0, tk.END)
    entry_boxes[tab_name][index].insert(0, str(weight))
    if checked == 0:
        check_buttons[tab_name][index].config(fg='grey')
    else:
        check_buttons[tab_name][index].config(fg='black')

def save_csv(tab_parent):
    file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV Files', '*.csv')])
    if file_path:
        selected_tab = tab_parent.select()  # Get currently selected tab ID
        selected_tab_text = tab_parent.tab(selected_tab, "text")  # Get the text of the selected tab
        if selected_tab_text == "MP4":
            button_text_keys = list(button_texts_mp4.keys())
        elif selected_tab_text == "MP5":
            button_text_keys = list(button_texts_mp5.keys())

        with open(file_path, 'w', newline='') as file:
            fieldnames = ['name', 'weight', 'on/off']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(button_text_keys)):
                name = button_text_keys[i]
                weight = int(entry_boxes[selected_tab_text][i].get())
                checked = button_vars[selected_tab_text][i].get()

                writer.writerow({'name': name, 'weight': weight, 'on/off': checked})


def load_csv(tab_parent):
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    if file_path:
        selected_tab = tab_parent.select()  # Get currently selected tab ID
        selected_tab_text = tab_parent.tab(selected_tab, "text")  # Get the text of the selected tab
        if selected_tab_text == "MP4":
            clear_selections("MP4")
            button_text_keys = list(button_texts_mp4.keys())
        elif selected_tab_text == "MP5":
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
                    set_button_and_entry(selected_tab_text, i, weight, checked)
                    on_checkbutton_change(i, selected_tab_text)  # Update checkbox color


def generate_gecko_code(tab_parent, version_var):
    selected_tab = tab_parent.select()  # Get currently selected tab ID
    selected_tab_text = tab_parent.tab(selected_tab, "text")  # Get the text of the selected tab
    
    # Draw the appropriate grid
    if selected_tab_text == "MP5":
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
    elif selected_tab_text == "MP4":
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
    #clear twice to avoid powershell leaving stuff in the window
    os.system('cls')  # Clear console for Windows
    os.system('cls')  # Clear console for Windows

    selected_tab = tab_parent.select()  # Get currently selected tab ID
    selected_tab_text = tab_parent.tab(selected_tab, "text")  # Get the text of the selected tab

    # choose button text keys from mp4 or mp5
    if selected_tab_text == "MP4":
        button_text_keys = list(button_texts_mp4.keys())
        button_vars_dict = button_vars["MP4"]
        entry_boxes_dict = entry_boxes["MP4"]
        check_buttons_dict = check_buttons["MP4"]
    elif selected_tab_text == "MP5":
        button_text_keys = list(button_texts_mp5.keys())
        button_vars_dict = button_vars["MP5"]
        entry_boxes_dict = entry_boxes["MP5"]
        check_buttons_dict = check_buttons["MP5"]

    for i, var in enumerate(button_vars_dict):
        current_weight = int(entry_boxes_dict[i].get())
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
        current_weight = int(entry_boxes_dict[i].get())
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
        entry_boxes[tab_name][index].delete(0, tk.END)
        entry_boxes[tab_name][index].insert(0, "0")
        check_buttons[tab_name][index].config(fg='grey') # Set the color to a lighter one when not checked
    else:
        check_buttons[tab_name][index].config(fg='black') # Set the color to a darker one when checked

def open_help_window():
    help_window = tk.Toplevel()
    help_window.title("Help")
    help_window.geometry("300x200")

    #TODO fill in help text
    help_text = "This is the help text.\n\nYou can provide instructions or information here."
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

def clear_options(tab_parent):
    selected_tab = tab_parent.select()  # Get currently selected tab ID
    selected_tab_text = tab_parent.tab(selected_tab, "text")  # Get the text of the selected tab
    if selected_tab_text == "MP4":
        clear_selections("MP4")
    elif selected_tab_text == "MP5":
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
                var = tk.IntVar()
                button_vars[tab_name].append(var)

                entry_var = tk.StringVar()
                entry_var.set('0')  # Set default value to "0"
                vcmd = root.register(limit_size)

                entry = tk.Entry(parent, width=4, textvariable=entry_var, validate='key', validatecommand=(vcmd, '%P'))
                entry_boxes[tab_name].append(entry)

                checkbutton = tk.Checkbutton(parent, text=button_text_keys[index], variable=var, fg='grey', command=lambda i=index: on_checkbutton_change(i, tab_name))
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
                var = tk.IntVar()
                button_vars[tab_name].append(var)

                entry_var = tk.StringVar()
                entry_var.set('0')  # Set default value to "0"
                vcmd = root.register(limit_size)

                entry = tk.Entry(parent, width=4, textvariable=entry_var, validate='key', validatecommand=(vcmd, '%P'))
                entry_boxes[tab_name].append(entry)

                checkbutton = tk.Checkbutton(parent, text=button_text_keys[index], variable=var, fg='grey', command=lambda i=index: on_checkbutton_change(i, tab_name))
                check_buttons[tab_name].append(checkbutton)  # Store the check button

                entry.grid(row=i, column=j*2, padx=5, pady=5, sticky="e")
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
    if selected_tab_text == "MP5":
        create_mp5_grid(selected_frame, root, "MP5")
    elif selected_tab_text == "MP4":
        create_mp4_grid(selected_frame, root, "MP4")




def create_gui():
    global button_vars
    global entry_boxes

    root = tk.Tk()
    root.title("Mario Party 4/5 Item Pool Generator")
    root.iconbitmap("ico/Miracle_Capsule.ico")

    # Set default size of window to be large enough for mp4/mp5 item grids
    root.geometry("600x550")  # Width x Height in pixels

    main_frame = tk.Frame(root)  # Frame to hold version_frame and tab_parent
    main_frame.pack()

    # Create a button frame to hold the buttons
    button_frame = tk.Frame(main_frame)
    button_frame.pack(side=tk.TOP, fill=tk.X)

    # Create 'Save CSV' button and add to button_frame
    save_button = tk.Button(button_frame, text="Save CSV", command=lambda: save_csv(tab_parent))
    save_button.pack(side=tk.LEFT)

    # Create 'Load CSV' button and add to button_frame
    load_button = tk.Button(button_frame, text="Load CSV", command=lambda: load_csv(tab_parent))
    load_button.pack(side=tk.LEFT)

    # Create 'Clear All' button and add to button_frame
    clear_button = tk.Button(button_frame, text="Clear All", command=lambda: clear_options(tab_parent))
    clear_button.pack(side=tk.LEFT)

    # Create version radiobuttons
    version_var = tk.IntVar(value=1)  # Set default value to 1 (JP)
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
    tab_parent.add(mp4_tab, text="MP4")
    tab_parent.add(mp5_tab, text="MP5")
    tab_parent.pack(expand=1, fill='both')

    # Create a button frame to hold the buttons
    gen_code_button = tk.Frame(main_frame)
    gen_code_button.pack(side=tk.TOP, fill=tk.X)

    # Create 'Generate Gecko Code' button and add to gen_code_button
    generate_button = tk.Button(gen_code_button, text="Generate Gecko Code", command=lambda: on_generate_code(tab_parent, version_var))
    generate_button.pack(side=tk.LEFT)

    # Store tabs in a dictionary
    tab_parent.tabs = {"MP4": mp4_tab, "MP5": mp5_tab}

    create_mp4_grid(mp4_tab, root, "MP4")
    create_mp5_grid(mp5_tab, root, "MP5")
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