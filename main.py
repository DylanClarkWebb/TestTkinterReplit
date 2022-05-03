import tkinter as tk
import funs as f


def main():
    root = tk.Tk()
    
    ent_number = tk.Entry(
        master=root,
        font=("Segoe UI", 24),
    )
    ent_number.pack()
    
    btn_type = tk.Button(
        master=root,
        text="Check type",
        font=("Segoe UI", 12),
        command=lambda:
        f.check_type(ent_number.get(), lbl_type),
    )
    btn_type.pack()
    
    lbl_type = tk.Label(
        master=root,
        text="Click the button!",
        font=("Segoe UI", 18),
    )
    lbl_type.pack()
    
    root.mainloop()
    

if __name__ == "__main__":
    main()