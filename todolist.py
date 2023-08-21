import tkinter as tk

def append():
    new_note = entry_box.get()
    list_box.insert(tk.END, new_note)

def edit():
    selected_index = list_box.curselection()
    if selected_index:
        index_edit = selected_index[0]
        item_edit = list_box.get(index_edit)

        list_box.pack_forget()
        entry_box.delete(0, tk.END)
        entry_box.insert(0, item_edit)
        entry_box.pack()
   
def delete():
    selected_index = list_box.curselection()
    if selected_index:
        index_delete = selected_index[0]
        list_box.delete(index_delete)

def save():
    updated_text = entry_box.get()
    selected_index = list_box.curselection()
    if selected_index:
        index_edit = selected_index[0]
        list_box.delete(index_edit)
        list_box.insert(index_edit, updated_text)
        list_box.pack()

def clear():
    entry_box.delete(0,tk.END)

window = tk.Tk()
window.geometry("675x640")
window.title("Own-To-do-list")

frame = tk.Frame(window)
frame.pack()

label = tk.Label(frame, text=" Own To Do List", font=("Century",30), bg="Grey", fg="black", width=25, height=2)
label.pack()

list_box = tk.Listbox(frame, font=("Century",18),width=56,height=15,selectbackground="LightSteelBlue",highlightthickness=0,selectforeground="Black",background="White")
list_box.pack(side="left",fill="both")

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right",fill="both")

list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)

entry_box = tk.Entry(window,font=("Century",16),width=43,background="Lavender")
entry_box.pack(pady=5)

frame2 = tk.Frame(window)
frame2.pack()

button_append = tk.Button(frame2,text="ADD",font=("Century",11),background="LightSeaGreen",width=7,command=append)
button_append.pack(side="right",padx=6,pady=7)

button_delete = tk.Button(frame2,text="EDIT",font=("Century",11),background="Yellow",width=7,command=edit)
button_delete.pack(side="right",padx=6,pady=7)

button_edit = tk.Button(frame2,text="SAVE",font=("Century",11),background="Blue",width=7,command=save)
button_edit.pack(side="left",padx=6,pady=7)

button_save = tk.Button(frame2,text="CLEAR",font=("Century",11),background="Green",width=7,command=clear)
button_save.pack(side="left",padx=6,pady=7)

button_clear= tk.Button(frame2,text="DELETE",font=("Century",11),background="Steelblue",width=7,command=delete)
button_clear.pack(side="left",padx=6,pady=7)

window.mainloop()