import tkinter as tk
import PyPDF2
# pillow module
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

# Begining of the interface
root = tk.Tk()
# Objects inside the window


# Gives us the size of the canvus we want to work with
canvas = tk.Canvas(root, width=600, height=500)
# Gives us three idivudal colums to work with
canvas.grid(columnspan=3, rowspan=3)

# Gets the logo from the file directory
logo = Image.open('./starterFiles/logo.png')
# defines the logo as a Image that Tkinter can use
logo = ImageTk.PhotoImage(logo)
# assigns a label to that image
logo_label = tk.Label(image=logo)
# allows for that image to be added to the UI
logo_label.image = logo
# Adds the logo to the center as we have three colums 0,1,2
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
# Positions the instuctions
instructions.grid(columnspan=3, column=0, row=1)


# Open file command
def open_file():
    # Text changes when the button is clicked
    browse_text.set("loading...")
    # Searches for the file, we have defined here that it must be a PDF file
    file = askopenfile(parent=root, mode='rb', title="Choosea file", filetypes=[("Pdf file", "*.pdf")])
    # if the file is found
    if file:
        print("file was sucessfuly loaded")
        read_pdf = PyPDF2.PdfFileReader(file)
        # read the first page
        page = read_pdf.getPage(0)
        # extract the text from the page
        page_content = page.extractText()

        # print(page_content)
    text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
    # Text index, content
    text_box.insert(1.0, page_content)
    # location
    text_box.tag_configure("center", justify="center")
    text_box.tag_add("center", 1.0, "end")
    text_box.grid(column=1, row=3)

    browse_text.set("Browse")


# Browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font="Raleway", bg='#20bebe',
                       fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

# everything we create in the UImust be between root = tk.Tk() and root.mainloop()
root.mainloop()
