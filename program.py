import csv
import pandas as pd
from tkinter import *
import KNN
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import numpy as np
from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import Tk, Frame

def toggle_fullscreen(event=None):
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

def end_fullscreen(event=None):
    root.attributes("-fullscreen", False)
root = Tk()
root.title('No.1 APP')
root.attributes("-fullscreen", True)
root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", end_fullscreen)
frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="white", width=960, height=560)
canvas.pack()

header = Label(canvas, text="ตารางเปรียบเทียบ สัดส่วนของร่างกาย", bg="white", fg="black", font="Inter 20 bold").place(x=450, y=20)

body = PhotoImage(file="assets/pic/form.png")
canvas.create_image(200, 260, image=body)
form_header = canvas.create_text(200, 55, text="ใส่ข้อมูล", font="Inter 30 bold", fill="black")
K = canvas.create_text(130, 115, text="เพศ", font="Inter 30 bold", fill="black")
SEX = canvas.create_text(130, 185, text="อายุ", font="Inter 30 bold", fill="black")
WEIGHT = canvas.create_text(105, 255, text="น้ำหนัก", font="Inter 30 bold", fill="black")
HEIGHT = canvas.create_text(105, 325, text="ส่วนสูง", font="Inter 30 bold", fill="black")

table = PhotoImage(file="assets/pic/table.png")
canvas.create_image(665, 235, image=table)

Input_image_box = PhotoImage(file="assets/pic/input.png")
k = StringVar()
canvas.create_image(290, 120, image=Input_image_box)
input_k = Entry(canvas, width=5, font="Inter 24 bold", border=0, textvariable=k).place(x=220, y=100)

sex = IntVar()
canvas.create_image(290, 190, image=Input_image_box)
input_sex = Entry(canvas, width=5, font="Inter 24 bold", border=0, textvariable=sex).place(x=220, y=170)

weight = IntVar()
canvas.create_image(290, 260, image=Input_image_box)
input_weight = Entry(canvas, width=5, font="Inter 24 bold", border=0, textvariable=weight).place(x=220, y=240)

height = IntVar()
canvas.create_image(290, 330, image=Input_image_box)
input_height = Entry(canvas, width=5, font="Inter 24 bold", border=0, textvariable=height).place(x=220, y=310)


under = PhotoImage(file="assets/pic/mother_result.png")
canvas.create_image(485, 470, image=under)
result = PhotoImage(file="assets/pic/under_result.png")
canvas.create_image(485, 500, image=result)

output = PhotoImage(file="assets/pic/result.png")
canvas.create_image(650, 495, image=output)

txt = StringVar()
out_put = Label(canvas, width=10, font="Inter 15 bold", background="#ffffff", border=0, textvariable=txt).place(x=660, y=480)

def linear_regression_predict(person):
    # ข้อมูลเพศ, อายุ, น้ำหนัก, ส่วนสูง
    x = np.array([
        [1, 27, 60, 170],
        [1, 18, 70, 180],
        [0, 19, 64, 174],
        [0, 25, 80, 167],
        [1, 40, 56, 172],
        [0, 32, 45, 156],
        [1, 24, 52, 170],
        [1, 28, 70, 180],
        [0, 19, 45, 165],
        [1, 20, 120, 165],
        [1, 30, 49, 160],
        [0, 14, 50, 155],
        [1, 35, 39, 166],
        [1, 29, 89, 180],
        [0, 45, 60, 148],
        [1, 57, 77, 171],
        [0, 77, 55, 159],
        [0, 67, 43, 158],
        [1, 89, 47, 168],
        [0, 78, 30, 145],
        [1, 89, 66, 166],
        [1, 80, 77, 189],
        [0, 12, 26, 89],
        [1, 24, 67, 189],
        [0, 22, 29, 134],
        [1, 51, 55, 170],
        [1, 78, 99, 189],
        [1, 67, 88, 190],
        [0, 8, 12, 40],
        [1, 7, 11, 67],
        [1, 27, 45, 155],
        [0, 7, 14, 100],
        [0, 56, 57, 130],
        [1, 48, 78, 189],
        [1, 39, 70, 181],
        [1, 22, 45, 167],
        [0, 18, 39, 167],
        [1, 44, 67, 157],
        [0, 48, 67, 157],
        [1, 56, 63, 172],
        [1, 18, 80, 178],
        [0, 18, 40, 165],
        [1, 44, 70, 170],
        [0, 48, 70, 155],
        [1, 14, 45, 145],
        [1, 18, 75, 180],
        [0, 18, 55, 160],
        [1, 30, 70, 160],
        [0, 44, 66, 155],
        [1, 13, 45, 158],
        [0, 20, 78, 190],
        [1, 23, 56, 170],
        [0, 20, 66, 166],
        [1, 25, 70, 179],
        [0, 35, 66, 165],
        [1, 19, 43, 168],
        [1, 20, 66, 154],
        [0, 18, 40, 144],
        [1, 108, 60, 160],
        [0, 89, 66, 155],
        [1, 20, 78, 180],
        [1, 18, 55, 165],
        [0, 10, 40, 144],
        [1, 42, 65, 166],
        [0, 9, 66, 155],
        [1, 40, 78, 178],
        [1, 30, 65, 165],
        [0, 23, 45, 178],
        [1, 55, 60, 168],
        [0, 90, 67, 155],
        [1, 22, 80, 181],
        [1, 19, 56, 166],
        [0, 11, 43, 150],
        [1, 43, 66, 169],
        [0, 10, 70, 166],
        [1, 35, 68, 180],
        [1, 33, 69, 169],
        [0, 25, 65, 180],
        [1, 59, 67, 165],
        [0, 92, 45, 155],
        [1, 30, 81, 189],
        [1, 23, 54, 178],
        [0, 12, 45, 140],
        [1, 40, 55, 167],
        [0, 17, 65, 177],
        [1, 45, 77, 198],
        [1, 36, 70, 170],
        [0, 29, 60, 185],
        [1, 45, 55, 179],
        [0, 88, 47, 165],
        [1, 27, 86, 178],
        [1, 25, 55, 170],
        [0, 30, 46, 155],
        [1, 45, 77, 167],
        [0, 23, 105, 189],
        [1, 49, 52, 169],
        [1, 35, 65, 167],
        [0, 34, 62, 170],
        [1, 21, 56, 168],
        [0, 88, 47, 165],
        [1, 30, 89, 180],
        [1, 24, 66, 189],
        [0, 45, 66, 198],
        [1, 14, 75, 165],
        [0, 25, 88, 170],
        [1, 45, 52, 150]


    ])

    # ตัวอย่างนี้ทำนายดัชนีมวลกาย (BMI) ซึ่งเป็นตัวเลข
    y = np.array([21.5, 22.0, 20.1, 24.3, 19.2, 23.4, 21.8, 25.0, 18.5, 22.2, 
                      20.3, 21.6, 24.1, 19.9, 23.7, 22.4, 20.6, 24.8, 18.7, 22.9,
                      21.1, 21.4, 20.8, 19.5, 23.2, 22.7, 20.9, 24.6, 19.0, 23.9,
                      21.3, 22.1, 20.4, 24.2, 19.1, 23.5, 22.3, 20.7, 24.7, 18.8,
                      23.0, 21.2, 21.7, 20.2, 24.4, 19.3, 23.6, 22.5, 20.5, 24.9,
                      18.9, 23.1, 21.0, 21.9, 20.0, 19.4, 23.3, 22.6, 20.3, 24.5,
                      19.7, 22.8, 21.8, 22.2, 21.5, 19.8, 23.8, 22.9, 21.6, 25.0,
                      18.6, 23.2, 21.4, 21.1, 21.9, 20.4, 24.0, 19.6, 23.7, 22.7,
                      21.2, 24.3, 18.4, 23.4, 21.3, 22.0, 21.7, 19.9, 24.1, 22.8,
                      20.7, 24.6, 18.3, 23.5, 21.0, 22.1, 21.8, 20.2, 24.2, 22.9,
                      20.8, 24.7, 18.2, 23.6, 21.9, 22.4]) # ตัวอย่างข้อมูล BMI

    # สร้างและฝึกโมเดล Linear Regression
    model = LinearRegression().fit(x, y)

    # ทำนายด้วยข้อมูลใหม่
    predicted_bmi = model.predict([person])
    return predicted_bmi[0]

# ทดสอบฟังก์ชัน
person_info = [1, 30, 80, 175] # [เพศชาย, อายุ 30, น้ำหนัก 80, ส่วนสูง 175]
predicted_bmi = linear_regression_predict(person_info)
print("ดัชนีมวลกายที่ทำนายได้:", predicted_bmi)

def calling_linear_regression():
    # รับค่าจากผู้ใช้
    try:
        K = 1 if k.get().lower() == "male" else 0  # เปลี่ยนเป็น 1 สำหรับ 'male' และ 0 สำหรับ 'female'
        SEX = sex.get()
        WEIGHT = weight.get()
        HEIGHT = height.get()
        
        # ทำนายด้วย Linear Regression
        predicted_bmi = linear_regression_predict([K, SEX, WEIGHT, HEIGHT])
        txt.set(f"BMI : {predicted_bmi:.2f}")
    except ValueError as e:
        txt.set("Error in input")


def open_image():
    file_path = filedialog.askopenfilename(initialdir="/", title="Select Image",
                                           filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.gif"), ("all files", "*.*")))

    if file_path:
        image = Image.open(file_path)
        image = image.resize((300, 300))
        tk_image = ImageTk.PhotoImage(image)

        image_window = Toplevel(root)
        image_window.title("รูปภาพ")

        image_label = Label(image_window, image=tk_image)
        image_label.image = tk_image
        image_label.pack()


def open_csv():
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select CSV File",
        filetypes=(("CSV files", "*.csv"), ("all files", "*.*"))
    )

    if file_path:
        try:
            df = pd.read_csv(file_path)
            show_table(df)
        except pd.errors.EmptyDataError:
            print("The selected CSV file is empty.")


def show_table(dataframe):
    table_window = Toplevel(root)
    table_window.title("CSV Table")

    tree = ttk.Treeview(table_window, columns=list(dataframe.columns), show='headings')
    for col in dataframe.columns:
        tree.heading(col, text=col)
    tree.pack()

    for i, row in dataframe.iterrows():
        tree.insert("", "end", values=list(row))


button_image = PhotoImage(file="assets/pic/button.PNG")
click_label = Label(canvas, image=button_image)
button = Button(canvas, image=button_image, command=calling_linear_regression, border=0, background="white", cursor="hand2")
button.place(x=250, y=460)

CSVButton = Button(canvas, text="เปิดไฟล์ CSV", command=open_csv, border=1, background="white", cursor="hand2")
CSVButton.place(x=890, y=100)

ImageButton = Button(canvas, text="เปิดรูป", command=open_image, border=1, background="white", cursor="hand2")
ImageButton.place(x=890, y=50)

root.mainloop()
