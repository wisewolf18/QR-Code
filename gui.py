import segno
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def generate_qr():
    link = url_entry.get()
    if link:
        try:
            qr = segno.make_qr(link)
            qr.save("output.png", scale=20)
            messagebox.showinfo("Success", "QR Code generated successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error generating QR Code: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter a URL.")
root = tk.Tk()
root.title("QR Code Generator")
frame = ttk.Frame(root)
frame.grid(column=0, row=0, padx=10, pady=10)
url_label = ttk.Label(frame, text="Enter the URL link:")
url_label.grid(column=0, row=0, padx=10, pady=5)

url_entry = ttk.Entry(frame, width=40)
url_entry.grid(column=1, row=0, padx=10, pady=5)
generate_button = ttk.Button(frame, text="Generate QR Code", command=generate_qr)
generate_button.grid(column=0, row=1, columnspan=2, padx=10, pady=10)
root.update()
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.mainloop()
