import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from Lexer import lexer_action 

def on_content_changed(event=None):
    update_line_numbers()
    
def update_line_numbers():
    line_number_box.config(state="normal")
    line_number_box.delete("1.0", "end")
    
    content = text_box.get("1.0", "end-1c")
    
    if content:
        lines = content.split("\n")
        line_count = len(lines)
        
        line_numbers = '\n'.join(str(i) for i in range(1, line_count + 1))
        line_number_box.insert("1.0", line_numbers)
    
    line_number_box.config(state="disabled")

def lex_text():
    try:
        text = text_box.get("1.0", "end-1c")
        token_list = lexer_action(text)  
        display_tokens(token_list)
    except Exception as e:
        show_error_popup(str(e))

def display_tokens(token_list):
    new_window = tk.Toplevel(root)
    new_window.title("Tokens")
    new_window.configure(bg="#282a36")  
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="#f8f8f2", background="#282a36", font=('Helvetica', 13))

    tree = ttk.Treeview(new_window, columns=("Type", "Element", "Line"), show="headings", style="BW.TLabel")
    tree.heading("Type", text="Tipo")
    tree.heading("Element", text="Elemento")
    tree.heading("Line", text="Linea")



    for token in token_list:
        tree.insert("", "end", values=(token[0], token[1], token[2]))

    tree.pack(expand=True, fill="both")

def import_file():
    try:
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                text_box.delete("1.0", "end")
                text_box.insert("1.0", content)
                update_line_numbers()  
    except Exception as e:
        show_error_popup(str(e))

def clear_content():
    text_box.delete("1.0", "end")
    update_line_numbers()  

def exit_app():
    root.destroy()

def show_error_popup(message):
    error_popup = tk.Toplevel(root)
    error_popup.title("Error")
    error_popup.configure(bg="#282a36")  

    window_width = 600
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    error_popup.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    error_label = tk.Label(error_popup, text=message, bg="#282a36", fg="#f8f8f2", font=('Consolas', 12)) 
    error_label.pack(padx=10, pady=10)
    close_button = tk.Button(error_popup, text="De Acuerdo", command=error_popup.destroy, bg="#6272a4", fg="#f8f8f2", font=('Helvetica', 10))  
    close_button.pack(padx=10, pady=10)

root = tk.Tk()
root.title("LexLuaThor")
root.configure(bg="#282a36")  

window_width = 1280
window_height = 720
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

line_number_frame = tk.Frame(root, width=50, bg="#44475a")  
line_number_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

line_number_box = tk.Text(line_number_frame, width=4, padx=4, pady=4, wrap=tk.NONE, bg="#44475a", fg="#f8f8f2", font=('Consolas', 13))  # Match background color, text color, and font
line_number_box.pack(side=tk.LEFT, fill=tk.Y)
line_number_box.config(state="disabled")  

text_frame = tk.Frame(root, bg="#44475a")  
text_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

text_box = tk.Text(text_frame, height=40, width=100, bg="#44475a", fg="#f8f8f2", font=('Consolas', 13))  # Set text box background color, text color, and font
text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

text_box.bind("<Key>", on_content_changed)


button_frame = tk.Frame(root, bg="#282a36")  
button_frame.pack(side=tk.TOP, padx=10, pady=10)

lex_button = tk.Button(button_frame, text="Lex it!", command=lex_text, width=10, height=2, bg="#50fa7b", fg="#44475a", bd=0, font=('Helvetica', 12, 'bold'))  # Green button with white text
lex_button.pack(side=tk.TOP, padx=5, pady=5)

import_button = tk.Button(button_frame, text="Importar\nArchivo", command=import_file, width=10, height=2, bg="#bd93f9", fg="#44475a", bd=0, font=('Helvetica', 12, 'bold'))  # Blue button with white text
import_button.pack(side=tk.TOP, padx=5, pady=5)

clear_button = tk.Button(button_frame, text="Borrar\nContenido", command=clear_content, width=10, height=2, bg="#ffb86c", fg="#44475a", bd=0, font=('Helvetica', 12, 'bold'))  # Yellow button with white text
clear_button.pack(side=tk.TOP, padx=5, pady=5)

exit_button = tk.Button(root, text="Salir", command=exit_app, width=10, height=2, bg="#ff5555", fg="white", bd=0, font=('Helvetica', 12, 'bold'))  # Red button with white text
exit_button.pack(side=tk.BOTTOM, padx=10, pady=10)


root.mainloop()
