from tkinter import *
from PIL import Image, ImageTk


def compute_total():
    try:
        order_total = float(price_entry.get())

        if order_total < 0:
            raise ValueError

        shipping_fee = shipping_var.get()

        if shipping_fee == 0.0:
            result_entry.delete(0, END)
            result_entry.insert(0, "Select Shipping")
            return
        elif shipping_fee == 5.95 and order_total >= 75:
            shipping_fee = 0.0
        else:
            pass
        total = 1.12 * (order_total + shipping_fee)

        result_entry.delete(0, END)
        result_entry.insert(0, f"{total:.2f}")

    except ValueError:
        result_entry.delete(0, END)
        result_entry.insert(0, "Check Input")


def clear_fields():
    price_entry.delete(0, END)
    result_entry.delete(0, END)
    shipping_var.set(0.0) 


root = Tk()

# --- Images ---
img_urs = ImageTk.PhotoImage(Image.open("University_of_Rizal.png").resize((50, 50)))
img_cert = ImageTk.PhotoImage(Image.open("Screenshot 2026-03-20 221441.png").resize((80, 50)))
img_py = ImageTk.PhotoImage(Image.open("images.jpg").resize((85, 60)))
img_bg = ImageTk.PhotoImage(Image.open("many-jars-of-candles-are-on-shelves-in-a-room-photo.jpg").resize((1000, 500)))

root.geometry("1000x500")

# --- Frames ---
main_frame = Frame(root, bg="#f0f0e6")
main_frame.place(relx=0.5, rely=0.22, anchor=CENTER)

overlay_frame = Frame(root, width=1, height=1)
overlay_frame.place(relx=0.5, rely=0.25, anchor=CENTER)

# --- Title & Input ---
title_label = Label(main_frame, text="CandleLine Corporation",
                    font=("Times New Roman", 20, "underline", "bold"))
title_label.grid(pady=10)

order_label = Label(main_frame, text="Total amount of your order",
                    font=("Times New Roman", 10))
order_label.grid(pady=1)

price_entry = Entry(main_frame, width=20, font=("Times New Roman", 10))
price_entry.grid(pady=1)

# --- Shipping Frame ---
shipping_frame = Frame(root, bg="#f0f0e6", bd=1, relief="solid", width=450, height=120)
shipping_frame.place(x=280, y=170)
shipping_frame.lower(overlay_frame)

# --- Images placement ---
Label(root, image=img_urs).place(x=10, y=20)
Label(root, image=img_cert).place(x=70, y=20)
Label(root, image=img_py).place(x=890, y=17)

bg_label = Label(root, image=img_bg)
bg_label.place(relx=0, rely=0)
bg_label.lower(main_frame)

# --- Result Frame ---
result_frame = Frame(root, bg="#f0f0e6", bd=1, relief="solid", width=560, height=360)
result_frame.place(x=236, y=50)
result_frame.lower(main_frame)

# --- Shipping ---
shipping_var = DoubleVar(value=0.0)  # FIX 3: explicit default so unselected state is detectable

Label(root, bg="#f0f0e6", text="Shipping method",
      font=("Times New Roman", 10)).place(x=446, y=160)

Radiobutton(root, bg="#f0f0e6",
            text="Priority (overnight) @$14.95",
            value=14.95, variable=shipping_var,
            font=("Times New Roman", 10)).place(x=306, y=200)

Radiobutton(root, bg="#f0f0e6",
            text="Standard (5 to 7 working days) @$5.95 ($0.00 if order amt>$75.00)",
            wraplength=210, justify=LEFT,
            value=5.95, variable=shipping_var,
            font=("Times New Roman", 10)).place(x=306, y=230)

Radiobutton(root, bg="#f0f0e6",
            text="Express (2 days) @11.95",
            value=11.95, variable=shipping_var,
            font=("Times New Roman", 10)).place(x=546, y=200)

# --- Result ---
Label(root, bg="#f0f0e6",
      text="Amounts Payable (12% VAT included): ",
      font=("Times New Roman", 10)).place(x=336, y=300)

result_entry = Entry(root, width=20, font=("Times New Roman", 10))
result_entry.place(x=556, y=300)

# --- Lines ---
canvas_top = Canvas(root, bg="black", height=2, width=450)
canvas_top.place(x=286, y=330)
canvas_top.create_line(10, 75, 300, 75, fill="blue", width=3)

canvas_bottom = Canvas(root, bg="black", height=2, width=450)
canvas_bottom.place(x=286, y=380)
canvas_bottom.create_line(10, 75, 300, 75, width=3)

# --- Buttons ---
Button(root, text="Clear", command=clear_fields).place(x=446, y=340)
Button(root, text="Compute", command=compute_total).place(x=486, y=340)

root.mainloop()