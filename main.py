import joblib
import tkinter
import numpy as np
from tkinter import messagebox
from PIL import ImageTk, Image
import os


iris_classifier_model = joblib.load("C:/Users/alfth/OneDrive/Documents/PYTHON/FINAL PROJECT ALPROG/Final/resources/iris_classifier_with_KNN.joblib")
spesies = ["Iris Setosa","Iris Versicolor","Iris Virginica"]


def click():
    data = getValue()
    if data is None: return
    hasil = predict(data)
    print(hasil)
    image = check_img(hasil)

    label_output.configure(text=hasil)
    output.configure(image=image)

def predict(data):
    result = iris_classifier_model.predict(data)
    hasil = [spesies[i] for i in result]
    return hasil[0]

def check_img(result):
    for i in range(0,len(spesies)):
        if result == spesies[i]:
            return image[i]

def getValue():
    try:
        data = [[input_sl.get(),input_sw.get(),input_pl.get(),input_pw.get()]]
        data_check = np.array(data)
        if np.all(data_check > 0):
            return data
        else:
            messagebox.showerror("Error", "Invalid input. silahkan masukan angka yang benar")
            return None
    except:
        messagebox.showerror("Error", "Invalid input. silahkan masukan angka yang benar")
        return None


if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Iris Classification")

    #FUNCTION
    


    #VARIABLES
    input_sw = tkinter.DoubleVar()
    input_sl = tkinter.DoubleVar()
    input_pw = tkinter.DoubleVar()
    input_pl = tkinter.DoubleVar()




    ## FRAME
    main_frame = tkinter.Frame(window)
    main_frame.pack()

    input_frame = tkinter.LabelFrame(main_frame,text="Input Data Iris",padx=20,pady=20)
    input_frame.grid(row=0,column=0)

    button_frame = tkinter.LabelFrame(main_frame,text="Button",padx=20,pady=20)
    button_frame.grid(row=1,column=0)

    output_frame = tkinter.LabelFrame(main_frame,text="Output",padx=10,pady=10)
    output_frame.grid(row=2,column=0)

    ##ISI FRAME
    input_sl_label = tkinter.Label(input_frame,text="Sepal Length (cm)")
    input_sl_label.grid(row=0,column=0)
    entry_sl = tkinter.Entry(input_frame,textvariable=input_sl)
    entry_sl.grid(row=1,column=0)
    
    input_sw_label = tkinter.Label(input_frame,text="Sepal Width (cm)")
    input_sw_label.grid(row=0,column=1)
    entry_sw = tkinter.Entry(input_frame,textvariable=input_sw)
    entry_sw.grid(row=1,column=1)

    input_pl_label = tkinter.Label(input_frame,text="Petal Length (cm)")
    input_pl_label.grid(row=0,column=2)
    entry_pl = tkinter.Entry(input_frame,textvariable=input_pl)
    entry_pl.grid(row=1,column=2)

    input_pw_label = tkinter.Label(input_frame,text="Petal Width (cm)")
    input_pw_label.grid(row=0,column=3)
    entry_pw = tkinter.Entry(input_frame,textvariable = input_pw)
    entry_pw.grid(row=1,column=3)

    
    
    #button
    button_input = tkinter.Button(button_frame,text="Predict!",width=70,command=click)
    button_input.grid(row=0,column=0)

    img_virginica = ImageTk.PhotoImage(Image.open("C:/Users/alfth/OneDrive/Documents/PYTHON/FINAL PROJECT ALPROG/Final/resources/img/virginica.jpg"))
    img_versicolor = ImageTk.PhotoImage(Image.open("C:/Users/alfth/OneDrive/Documents/PYTHON/FINAL PROJECT ALPROG/Final/resources/img/versicolor.jpg"))
    img_setosa = ImageTk.PhotoImage(Image.open("C:/Users/alfth/OneDrive/Documents/PYTHON/FINAL PROJECT ALPROG/Final/resources/img/setosa.jpg"))

    image = [img_setosa, img_versicolor, img_virginica]

    output = tkinter.Label(output_frame,image=img_virginica)
    output.grid(row=0,column=0)

    result = "example"
    label_output = tkinter.Label(output_frame,text=result)
    label_output.grid(row=1,column=0)
    
    window.mainloop()


