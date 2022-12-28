from Users.models import Users
from BMR.models import BMR
from tkinter import *
from PIL import ImageTk,Image 

def main():
    root = Tk()
    b = BMR
    u = Users
    choice = 'yes'
    lst_food_exist = []
    lst_food_none = []
    lst_index = []
    # u.setName()
    # while (choice != 'no'): 
    #     u.setHobby()
    #     choice = u.setChoice()
        
    # get hobby to list
    f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\hobby.txt", "r")
    a = f.read()
    lst_hobby = list(a.split("\n"))
    f.close()

    # get food to list
    f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\food.txt", "r")
    a = f.read()
    lst_food = list(a.split("\n"))
    f.close()

    # get price to list
    f = open("C:\\Users\\kenny\\Downloads\\cs3310_AI-main\\cs3310_AI-main\\AI folder\\master\\price.txt", "r")
    a = f.read()
    lst_price = list(a.split("\n"))
    f.close()

    for i in range(len(lst_hobby)):
        if lst_hobby[i] in lst_food:
            lst_food_exist.append(lst_hobby[i])
            index = lst_food.index(lst_hobby[i])
            lst_index.append(index)
        else:
            lst_food_none.append(lst_hobby[i])

    root.title('Your choice')
    root.iconbitmap('C:\\Users\\kenny\\Downloads\\images\\title.jpg')
    space_label = Label(text="""
                        
                        """)
    
    # C:\\Users\\kenny\\Downloads\\***.jpg
    for i in range(0,len(lst_food_exist)):
        status = Label(root, text="Image of {}-()th food".format(i+1))
        my_img = ImageTk.PhotoImage(Image.open("C:\\Users\\kenny\\Downloads\\images\\{}.jpg".format(lst_food_exist[i])))
        food_label = Label(text=lst_food_exist[i])
        price_label = Label(text=lst_price[i])
        my_label = Label(image=my_img)
        food_label.pack()
        price_label.pack()
        my_label.pack()
        space_label.pack()
        
    root.mainloop()
        
        
main()
    