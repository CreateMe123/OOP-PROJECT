from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


def compute_total():
    try:
        order_total = float(order_entry.get())
        shipping_fee = shipping_var.get()

        if order_total < 0:
            raise ValueError("Order amount cannot be negative.")
        if shipping_fee == 0.0:
            raise ValueError("Please select a shipping option.")
        elif shipping_fee == 5.95 and order_total >= 75:
            shipping_fee = 0.0

        total = 1.12 * (order_total + shipping_fee)

        result_entry.delete(0, END)
        result_entry.insert(0, f"{total:.2f}")

    except ValueError as e:
        messagebox.showerror("Error", str(e))


def clear_fields():
    order_entry.delete(0, END)
    result_entry.delete(0, END)
    shipping_var.set(0.0)


root = Tk()
root.geometry("1000x500")

# --- Images ---
img_urs = ImageTk.PhotoImage(Image.open("University_of_Rizal.png").resize((50, 50)))
img_cert = ImageTk.PhotoImage(Image.open("Screenshot 2026-03-20 221441.png").resize((80, 50)))
img_py = ImageTk.PhotoImage(Image.open("images.jpg").resize((85, 60)))
img_bg = ImageTk.PhotoImage(Image.open("many-jars-of-candles-are-on-shelves-in-a-room-photo.jpg").resize((1000, 500)))


# --- Frames ---
main_frame = Frame(root, bg="#f0f0e6")
main_frame.place(relx=0.5, rely=0.22, anchor=CENTER)

overlay_frame = Frame(root, width=1, height=1)
overlay_frame.place(relx=0.5, rely=0.25, anchor=CENTER)

# --- Title & Input ---
title_label = Label(root, text="CandleLine Corporation", bg="#f0f0e6",
                    font=("Times New Roman", 20, "underline", "bold"))
title_label.place(relx=0.52, rely=0.18, anchor=CENTER)

order_label = Label(root, text="Total amount of your order",
                    font=("Times New Roman", 10))
order_label.place(relx=0.5, rely=0.25, anchor=CENTER)

order_entry = Entry(root, width=20, font=("Times New Roman", 10))
order_entry.place(relx=0.5, rely=0.29, anchor=CENTER)

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
shipping_var = DoubleVar(value=0.0)
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

result_entry = Entry(root, width=20, font=("Times New Roman", 10), bg="#DBDBD0")
result_entry.place(x=556, y=300)

# --- Lines ---
Frame(root, width=500, height=1, bg="black").place(x=520, rely=0.75, anchor=CENTER)
Frame(root, width=500, height=1, bg="black").place(x=520, rely=0.66, anchor=CENTER)

# --- Buttons ---
Button(root, text="Clear", command=clear_fields).place(x=446, y=340)
Button(root, text="Compute", command=compute_total).place(x=486, y=340)

root.mainloop()
