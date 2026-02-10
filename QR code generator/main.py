import os
import tkinter as tk
import qrcode
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
from pyuiWidgets.imageLabel import ImageLabel


main = tk.Tk()
main.title("QR code generator")
main.config(bg="#E4E2E2")
main.geometry("853x500")
main.minsize(853, 500)
main.maxsize(853, 500)
main.resizable(False, False)
main.update_idletasks()

geometryX = 0
geometryY = 0

main.geometry("+%d+%d"%(geometryX, geometryY))

style = ttk.Style()
style.configure("entry.TEntry", fieldbackground="#fff", foreground="#000")

entry = ttk.Entry(master=main, style="entry.TEntry")
entry.place(x=184, y=205, width=130, height=40)

style.configure("label.TLabel", background="#E4E2E2", foreground="#000", font=("Times", 30, "bold"), anchor="center")
label = ttk.Label(master=main, text="QR Code Generator", style="label.TLabel")
label.configure(anchor="center")
label.place(x=193, y=14, width=510, height=75)

style.configure("entry1.TEntry", fieldbackground="#fff", foreground="#000")

entry1 = ttk.Entry(master=main, style="entry1.TEntry")
entry1.place(x=185, y=263, width=130, height=40)

style.configure("label1.TLabel", background="#E4E2E2", foreground="#000", font=("Arial", 16, "bold"), anchor="center")
label1 = ttk.Label(master=main, text="Box size", style="label1.TLabel")
label1.configure(anchor="center")
label1.place(x=32, y=206, width=121, height=37)

style.configure("label2.TLabel", background="#E4E2E2", foreground="#000", font=("Arial", 16, "bold"), anchor="center")
label2 = ttk.Label(master=main, text="Border size", style="label2.TLabel")
label2.configure(anchor="center")
label2.place(x=34, y=264, width=121, height=37)





text = tk.Text(master=main)
text.config(bg="#fff", fg="#000")
text.place(x=163, y=116, width=373, height=64)

style.configure("label4.TLabel", background="#E4E2E2", foreground="#000", font=("Arial", 16, "bold"), anchor="center")
label4 = ttk.Label(master=main, text="Text or URL", style="label4.TLabel")
label4.configure(anchor="center")
label4.place(x=25, y=134, width=121, height=37)

style.configure("label3.TLabel", background="#E4E2E2", foreground="#000", font=("Arial", 16, "bold"), anchor="center")
label3 = ImageLabel(master=main, image_path=("./QR_code.png"), text="", compound=tk.TOP, mode="fit")
label3.configure(anchor="center")
label3.place(x=548, y=174, width=272, height=235)

QR_IMAGE_SIZE = (272, 235)


def set_qr_image(image_path):
    if os.path.exists(image_path):
        base_img = Image.open(image_path)
    else:
        base_img = Image.new("RGB", QR_IMAGE_SIZE, "white")
    fitted = ImageOps.contain(base_img, QR_IMAGE_SIZE, Image.LANCZOS)
    canvas = Image.new("RGB", QR_IMAGE_SIZE, "white")
    offset = (
        (QR_IMAGE_SIZE[0] - fitted.size[0]) // 2,
        (QR_IMAGE_SIZE[1] - fitted.size[1]) // 2,
    )
    canvas.paste(fitted, offset)
    tkimg = ImageTk.PhotoImage(canvas)
    label3.configure(image=tkimg)
    label3.image = tkimg


set_qr_image("./QR_code.png")


def QR_code_generator():
    data=text.get("1.0",tk.END).strip()
    try:
        box=int(entry.get())
        brdr=int(entry1.get())
    except:
        box_size=10
        border_size=4
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=box,
    border=brdr
        )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save("./QR_code.png")
    set_qr_image("./QR_code.png")
    
    text.delete("1.0",tk.END)
    entry.delete(0,tk.END)
    entry1.delete(0,tk.END)
    
style.configure("button.TButton", background="#1a39c2", foreground="#000000")
style.map("button.TButton", background=[("active", "#0021db")], foreground=[("active", "#000")])

button = ttk.Button(master=main, text="Generate ", style="button.TButton", command=QR_code_generator)
button.place(x=241, y=338, width=80, height=40)



main.mainloop()