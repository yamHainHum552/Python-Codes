import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def openFile(window, textEdit):
    filePath = askopenfilename(filetypes=[("Text Files","*.txt")])
    if not filePath:
        return
    with open(filePath,"r") as f:
        content = f.read()
        textEdit.insert(tk.END,content)



def saveFile(window,textEdit):
    filePath = asksaveasfilename(filetypes=[("Text Files","*.txt")])
    if not filePath:
        return
    
    with open(filePath,"w") as f:
        content = textEdit.get(1.0,tk.END)
        f.write(content)
        

def main():
    window = tk.Tk()
    window.title("Text Editor")
    window.rowconfigure(0,minsize=400)
    window.columnconfigure(1,minsize=500)
    textEdit = tk.Text(window,font="Helvetica 18")
    textEdit.grid(row=0, column=1)
    frame = tk.Frame(window, relief="raised", bd=4)
    frame.grid(row=0,column=0,sticky="ns")
    saveButton = tk.Button(frame,text="Save")
    openButton = tk.Button(frame,text="Open", command=lambda:openFile(window,textEdit))
    saveButton.grid(row=0,column=0,sticky="ew")
    openButton.grid(row=1,column=0, sticky="ew")

    window.mainloop()

main()