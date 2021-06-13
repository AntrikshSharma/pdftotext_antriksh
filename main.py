import tkinter as tk
import PyPDF2 as pypd
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
import os


extracted = ""
filename = ""
path = ""

def message(title, msg):
    tk.messagebox.showinfo(title, msg)

def openFile():
    global extracted;
    global filename;
    global path;
    browse_txt.set("Choose...")
    file = askopenfile(parent = root, mode = "rb", title = "Chose a File: ", filetype = [("PDF File", "*.pdf")])
    pageContent = ""
    if file:
        mypdf = pypd.PdfFileReader(file)
        num = mypdf.getNumPages()
        for page in range(num):
            pgtext = mypdf.getPage(page)
            pageContent += "\n" + pgtext.extractText()
    extracted = pageContent
    textbox.insert(1.0, extracted)
    browse_txt.set("Browse")
    filename = os.path.basename(file.name)
    filename = filename[:filename.index(".")] 
    path = os.path.dirname(file.name) + "/"
    file.close()
    message("Converted", "The file has been converted succesfully.")
    
def saveFile():
    global extracted;
    global path;
    global filename;
    save_txt.set("Saving...")
    filepath = path +filename+"-converted"+".txt"
    file = open(filepath, "w")
    if file:
        file.write(extracted)
    
    file.close()
    save_txt.set("Save")
    message("Saved", "The file has been saved in the same directory successfully.")    
root = tk.Tk()
root.title("PDF TO TEXT")
root.resizable(False, False)
canvas = tk.Canvas(root, width=450, height=250)
canvas.grid(columnspan=3, rowspan = 3)

#logo
logo = Image.open('custom-logo.png')
logo = logo.resize((370, 183), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image = logo)
logo_label.image = logo
logo_label.grid(column = 1, row=0)

instr = "Click on browse to chose a PDF file and convert it into text format. You can find the text in the box below. Scroll if text overflows. Textbox is editable. Click on Save button to Save the file as txt file."
instructions = tk.Label(root, text = instr, font = ("Arial", 13), wraplength = 440, justify = "left")
instructions.grid(columnspan = 3, column = 0, row = 1)

browse_txt = tk.StringVar()
browse_btn = tk.Button(root, textvariable = browse_txt, font = ("Arial", 18), bg = "red", fg = "white", width = 31, height = 1, command = lambda:openFile())
browse_txt.set("Browse")
browse_btn.grid(column = 1, row = 2)

canvas = tk.Canvas(root, width=400, height=300)
canvas.grid(columnspan=3)

textbox = tk.Text(root, height= 15 , width = 50, padx = 20, pady = 20)
textbox.tag_configure("center", justify="left")
textbox.tag_add("center", 1.0, "end")
textbox.grid(column = 1, row = 3)

save_txt = tk.StringVar()
save_btn = tk.Button(root, textvariable = save_txt, font = ("Arial", 18), bg = "red", fg = "white", width = 31, height = 1, command = lambda:saveFile())
save_txt.set("Save")
save_btn.grid(column = 1, row = 4)

canvas = tk.Canvas(root, width=400, height=30)
canvas.grid(columnspan=3)

about = tk.Label(root, text = "Made by Antriksh Sharma", font = ("Arial", 12), wraplength = 440, justify = "center")
about.grid(column = 1, row = 5)

root.mainloop()