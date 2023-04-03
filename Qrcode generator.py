from tkinter import *
import qrcode 

root = Tk()
root.geometry('860x550')
root.title('Qr generator')
root.config(bg = '#ae2321')
root.resizable(False,False)

def generate():
  name = entry_input_name.get()
  link = entry_input_link.get()
  qr = qrcode.make(link)
  qr.save('Qrcode/'+str(name)+'.png')
  global Image
  Image = PhotoImage(file='Qrcode/'+str(name)+'.png')
  Image_view.config(image = Image)


Image_view = Label(root,bg = '#AE2321')
Image_view.pack(padx = 50,pady = 10,side = RIGHT)


title_label = Label(root,text = 'Title',fg = 'white',bg = '#ae2321',font = ('bold',17))
title_label.place(x = 50 , y = 170)

entry_input_name = Entry(root,width = 13,font=('arial',15))
entry_input_name.place(x = 50, y = 200)

entry_input_link = Entry(root,width = 28,font =('arial',15))
entry_input_link.place(x = 50,y = 250)

generate_button = Button(root,text = 'Generate',width = 20,height = 2,bg = 'black',fg = 'white',command = generate)
generate_button.place(x = 50 ,y = 300)

  
root.mainloop()


