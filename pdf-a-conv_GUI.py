from tkinter import filedialog
from tkinter import *
import os
import ghostscript


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)

def conv():
    print("\n PDF to PDF/A Conversion \n")
    print("\n Developed by A Rajasekaran\n")
    print("\n Date: 20 April 2022 \n\n")
    #f1 = os.listdir(filename) 
    for fname in os.listdir(filename):
        print(fname)
        if not fname.endswith(".pdf"):
            continue
        path = os.path.join(filename, fname)
        value1 = filename + '/' + fname
        value2 = filename + '/'
        print(value1)
        ghostScriptExec = ['gs', '-dPDFA', '-dBATCH', '-dNOPAUSE', '-dUseCIEColor', '-sProcessColorModel=DeviceRGB',
                   '-sDEVICE=pdfwrite', '-dFastWebView', '-dAutoRotatePages=/None', '-sPDFACompatibilityPolicy=1',
                   '-sOutputFile='+ value2 + 'PDFA-' + fname, path]
        ghostscript.Ghostscript(*ghostScriptExec)
    messagebox.showinfo("PDF/A Conversion", "Completed")

root = Tk()
root.geometry("400x250")
root.config(bg='#ffcc00') 

folder_path = StringVar()
label_value = 'PDF to PDF/A Conversion'
lbl1 = Label(root, text='PDF to PDF/A Conversion', font='helvetica 15', bg='#ffcc00')
lbl1.pack(pady=10)
button2 = Button(text="Browse", command=browse_button, bg='royalblue', fg = 'white').pack(pady=25)
button3 = Button(text="Submit", command=conv, bg='royalblue', fg = 'white').pack(pady=25)
lbl2 = Label(root, textvariable=folder_path, font='helvetica 12', bg='#ffcc00')
lbl2.pack(pady=10)



mainloop()


