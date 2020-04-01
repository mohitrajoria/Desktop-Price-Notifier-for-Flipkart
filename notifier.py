#!/usr/bin/python
import tkinter as tk
import Notification

quit = 0

def fun():
    a = web_value.get()
    b = freq_value.get()
    c = t_value.get()
    Notification.noti(a,b,c)
    app.destroy()

def quit():
    quit=1
    app.destroy()

app = tk.Tk()
app.title('Flipkart Price Change Notifier')
# f = tk.Frame().grid(padx=100, pady=50)
welcome =tk.Label(app, text = "Welcome to Notifier System",font = 'Helvetica 18 bold')
welcome.grid(row = 0,column = 0,columnspan = 2,padx=20, pady=20)
web = tk.Label(app, text="URL of the product")
web.grid(row = 1,column = 0,padx=20, pady=20)
web_value = tk.Entry(app)
web_value.grid(row = 1,column = 1,padx=20, pady=20)
freq = tk.Label(app, text="Frequency of Notifications (in sec)")
freq.grid(row = 2,column = 0,padx=20, pady=20)
freq_value = tk.Entry(app)
freq_value.grid(row = 2,column = 1,padx=20, pady=20)
t = tk.Label(app, text="Time Range")
t.grid(row = 3,column = 0,padx=20, pady=20)
t_value = tk.Entry(app)
t_value.grid(row = 3,column = 1,padx=20, pady=20)
add_notification = tk.Button(app, text="Add Notification", command = fun)
add_notification.grid(row = 4,column = 0, padx=20, pady=20)
q = tk.Button(app,text="Quit", command=quit)
q.grid(row=4,column=2,padx=20,pady=20)
app.mainloop()
