from tkinter import *
from pymongo import MongoClient

root = Tk()
root.title('PriceTracker')
root.geometry('400x400')

client = MongoClient('localhost', 27017)
db = client['price-tracker']
collection = db['logentries']

results = collection.find({})

heading_label = Label(root, text="Trackings", font='Helvetica 16 bold', pady=10, padx=10)
heading_label.pack()

for result in results:
    result_title = Label(root, text=result['title'], font=('Helvetica', 12), pady=10, padx=10, wraplength=350)
    result_title.pack()
    result_price = Label(root, text=result['price'], font=('Helvetica', 12), pady=10, padx=10, fg="red")
    result_price.pack()

quit = Button(root, text="Exit", fg="red", command=root.destroy)
quit.pack(side="bottom", pady=10)
quit = Button(root, text="Options")
quit.pack(side="bottom", pady=10)

root.mainloop()
