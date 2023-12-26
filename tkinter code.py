Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import tkinter as tk
... 
... def on_button_click():
...     label.config(text="Hello, " + entry.get())
... 
... # Create the main window
... app = tk.Tk()
... app.title("Simple GUI Application")
... 
... # Create and add widgets to the window
... label = tk.Label(app, text="Enter your name:")
... label.pack(pady=10)
... 
... entry = tk.Entry(app)
... entry.pack(pady=10)
... 
... button = tk.Button(app, text="Say Hello", command=on_button_click)
... button.pack(pady=10)
... 
... # Start the main event loop
