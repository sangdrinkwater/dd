from tkinter import *
from PIL import ImageTk,Image 


root =Tk()

# Create list containing food from hobby.txt file
# lst = ["rau", "thit"]

# # Contain database entries
# str = read(food.txt)
# lst2 = "/n".join(str)
# join, map, .. string => list
# lst2 = []

# for val in lst:
#     if val in lst2:
#         #Create image
#     else:
#         print("deo co" + val)


space_label = Label(root, text="""
                    
                    """)
myLabel1 = Label(root, text ="This is your favorite food chicken ")
myLabel2 = Label(root, text ="This is your  favorite rau!")
# myLabel1.grid(row=5,column=0)
# myLabel2.grid(row=5,column=1)

root.title('This is my favorite food')
root.iconbitmap('c:/gui/thit.jpg')
my_img = ImageTk.PhotoImage(Image.open("c:/gui/{}.jpg".format(lst[0])))
my_img2 = ImageTk.PhotoImage(Image.open("c:/gui/{}.jpg".format(lst[1])))
my_label = Label(image=my_img)
my_label2 = Label(image=my_img2)

myLabel2.pack()
my_label.pack()
space_label.pack()
myLabel1.pack()
my_label2.pack()



root.mainloop()