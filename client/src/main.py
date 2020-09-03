from tkinter import *
from pymongo import MongoClient
import webbrowser

def callback(url):
    webbrowser.open_new(url)

root = Tk()
root.title('PriceTracker')
root.geometry('400x600')

client = MongoClient('localhost', 27017)
db = client['price-tracker']
collection = db['logentries']

results = collection.find({})

def add_to_db():
    window = Toplevel(root)
    window.title('PriceTracker | Add')
    window.geometry('200x420')
    title_label = Label(window, text='Title', font='Helvetica 12', pady=10)
    title_label.pack()
    title = Entry(window)
    title.pack()
    link_label = Label(window, text='Link', font='Helvetica 12', pady=5)
    link_label.pack()
    link = Text(window, height=3)
    link.pack(padx=15)
    description_label = Label(window, text='Description', font='Helvetica 12', pady=5)
    description_label.pack()
    description = Text(window, height=3)
    description.pack(padx=15)
    image_label = Label(window, text='Image', font='Helvetica 12', pady=5)
    image_label.pack()
    image = Text(window, height=3)
    image.pack(padx=15)
    add_button = Button(window, text='Add', fg='green')
    add_button.pack(pady=10)
    cancel_button = Button(window, text='Cancel', fg='red', command=window.destroy)
    cancel_button.pack()

db_button = Button(root, text='Add', fg='green', command=add_to_db)
db_button.pack(pady=10)
heading_label = Label(root, text='Trackings', font='Helvetica 16 bold', pady=10, padx=10)
heading_label.pack()

for result in results:
    result_title = Label(root, text=result['title'], font=('Helvetica', 12), pady=10, padx=10, wraplength=350)
    result_title.pack(pady=10)
    result_price = Label(root, text=result['price'], font=('Helvetica', 12), fg="red")
    result_price.pack()
    result_button = Button(root, text="Click to view", fg="blue")
    result_button.pack(pady=10)
    result_button.bind('<Button-1>', lambda e: callback(result['link']))

quit = Button(root, text='Exit', fg="red", command=root.destroy)
quit.pack(side='bottom', pady=10)

root.mainloop()
