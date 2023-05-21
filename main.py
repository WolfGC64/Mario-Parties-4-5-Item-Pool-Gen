import tkinter as tk
from tkinter import ttk
import os

button_vars = []
entry_boxes = []
check_buttons = []

button_texts = [
    "Super Mushroom", #1
    "Cursed Mushroom", #2
    "Warp Pipe", #3
    "Klepto", #4
    "Bubble", #5
    "Wiggler", #6
    "Hammer Bro", #A
    "Coin Block", #B
    "Spiny", #C
    "Paratroopa", #D
    "Bullet Bill", #E
    "Goomba", #F
    "Bob-omb", #10
    "Koopa Bank", #11
    "Kamek", #14
    "Mr. Blizzard" #15
    "Piranha Plant", #16
    "Magikoopa", #17
    "Ukiki", #18
    "Lakitu", #19
    "Tweester", #1E
    "Duel", #1F
    "Chain Chomp", #20
    "Bone", #21
    "Bowser", #22
    "Chance", #23
    "Miracle", #24
    "Donkey Kong", #25
    "Versus" #26
]

def on_button_click(button_number):
    print(button_texts[button_number - 1] + " checked!")

def on_generate_code():
    checked_weights = 0
    total_weights = 0
    os.system('cls')  # Clear console for Windows
    for i, var in enumerate(button_vars):
        current_weight = int(entry_boxes[i].get())
        if check_buttons[i].cget('fg') == 'grey':
            continue
        total_weights += current_weight
        if var.get() == 1 and check_buttons[i].cget('fg') != 'grey':
            if current_weight == 0:
                print(f"{button_texts[i]} has no weight!")
            else:
                checked_weights += current_weight

    if total_weights == 0:
        print("Weight Total was 0!")
        return
    for i, var in enumerate(button_vars):
        if check_buttons[i].cget('fg') == 'grey':
            continue
        current_weight = int(entry_boxes[i].get())
        if current_weight == 0:
            continue
        item_name = button_texts[i]  # Get the name of the checked item
        item_percentage = (current_weight / total_weights) * 100
        if item_percentage != 0:
            print(f'{item_name}, Percentage: {item_percentage:.2f}%')

    checked_buttons = [i+1 for i, var in enumerate(button_vars) if var.get() == 1]

    if not checked_buttons:
        return

def on_checkbutton_change(index):
    if button_vars[index].get() == 0:
        entry_boxes[index].delete(0, tk.END)
        entry_boxes[index].insert(0, "0")
        check_buttons[index].config(fg='grey') # Set the color to a lighter one when not checked
    else:
        check_buttons[index].config(fg='black') # Set the color to a darker one when checked


def open_help_window():
    help_window = tk.Toplevel()
    help_window.title("Help")
    help_window.geometry("300x200")

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

def create_gui():
    global button_vars
    global entry_boxes

    root = tk.Tk()
    root.title("Mario Party 5 Capsule Pool Gen")
    root.iconbitmap("Miracle_Capsule.ico")

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True)

    tab = tk.Frame(notebook)
    notebook.add(tab, text="PAL")

    num_rows = 10  # Number of rows
    num_columns = 3  # Number of columns

    for i in range(num_rows):
        for j in range(num_columns):
            index = i * num_columns + j

            if index < len(button_texts):
                var = tk.IntVar()
                button_vars.append(var)
                entry_var = tk.StringVar()
                entry_var.set('0')  # Set default value to "0"
                # Registering validation command
                vcmd = root.register(limit_size)

                entry = tk.Entry(tab, width=4, textvariable=entry_var, validate='key', validatecommand=(vcmd, '%P'))
                entry_boxes.append(entry)

                checkbutton = tk.Checkbutton(tab, text=button_texts[index], variable=var, fg='grey', command=lambda i=index: on_checkbutton_change(i))
                check_buttons.append(checkbutton)  # Store the check button

                entry.grid(row=i, column=j*2, padx=5, pady=5, sticky="e")
                checkbutton.grid(row=i, column=j*2+1, padx=5, pady=5, sticky="w")

    generate_button = tk.Button(root, text="Generate Gecko Code", command=on_generate_code)
    generate_button.pack()

    help_button = tk.Button(root, text="Help", command=open_help_window)
    help_button.pack()

    root.mainloop()

def validate_input(value):
    if len(value) > 3:  # Limit input to 3 characters
        return False
    if not value.isdigit():  # Only allow numeric input
        return False
    return True

if __name__ == "__main__":
    create_gui()