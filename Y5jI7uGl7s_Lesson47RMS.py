from tkinter import *
import random
import time

root=Tk()
root.title("Restaurant Management System")
root.geometry("800x400+0+0")

font=('arial',10,'bold')
fg='steel blue'
fg2='black'

ref=StringVar()
fries=StringVar()
lunch=StringVar()
burger=StringVar()
pizza=StringVar()
cheese_burger=StringVar()
drinks=StringVar()
total_bill=StringVar()
cost=StringVar()

Tops = Frame(root, width = 1600,height=50, relief=SUNKEN) 
Tops.pack(side=TOP)
f1 = Frame(root, width = 900,height=700, relief=SUNKEN) 
f1.pack(side=LEFT)
f2 = Frame(root,width = 400,height=700,relief=SUNKEN) 
f2.pack(side=RIGHT)

title_label=Label(Tops, text='Restaurant Management System',fg='steel blue',font=("arial",30,"bold"))
title_label.grid(row=0,column=0)
localtime=time.asctime(time.localtime(time.time()))
time1=Label(Tops,font=("Arial",20),text=localtime,fg='steel blue')
time1.grid(row=1,column=0)

lbl_reference=Label(f1, font=font, fg=fg, bd=10, text="Order No.")
lbl_reference.grid(row=0,column=0)
txt_refernce=Entry(f1, font=font, fg=fg, bd=6, bg='powder blue', justify=CENTER, textvariable=ref)
txt_refernce.grid(row=0,column=1)

lbl_fries=Label(f1, font=font, fg=fg, bd=10, text="Fries Meal")
lbl_fries.grid(row=1,column=0)
txt_fries=Entry(f1, font=font, fg=fg, bd=6, bg='powder blue', justify=CENTER, textvariable=fries)
txt_fries.grid(row=1,column=1)

lbl_lunch=Label(f1, font=font, fg=fg, bd=10, text="Lunch Meal")
lbl_lunch.grid(row=2,column=0)
txt_lunch=Entry(f1, font=font, fg=fg, bd=6, bg='powder blue', justify=CENTER, textvariable=lunch)
txt_lunch.grid(row=2,column=1)

lbl_burger=Label(f1, font=font, fg=fg, bd=10, text="Burger Meal")
lbl_burger.grid(row=3,column=0)
txt_burger=Entry(f1, font=font, fg=fg, bd=6, bg='powder blue', justify=CENTER, textvariable=lunch)
txt_burger.grid(row=3,column=1)

lbl_pizza=Label(f1, font=font, fg=fg, bd=10, text="Pizza Meal")
lbl_burger.grid(row=3,column=0)
txt_pizza=Entry(f1, font=font, fg=fg, bd=6, bg='powder blue', justify=CENTER, textvariable=pizza)
txt_pizza.grid(row=3,column=1)

lbl_cheeseburger=Label(f1, font=font, fg=fg, bd=10, text="Cheese Burger")
lbl_cheeseburger.grid(row=4,column=0)
txt_cheeseburger=Entry(f1, font=font, fg=fg, bd=6, bg='powder blue', justify=CENTER, textvariable=cheese_burger)
txt_cheeseburger.grid(row=4,column=1)

lbl_drinks=Label(f1, font=font, fg=fg, bd=10, text="Drinks")
lbl_drinks.grid(row=0,column=3)
txt_drinks=Entry(f1, font=font, fg=fg, bd=6, bg='powder blue', justify=CENTER, textvariable=drinks)
txt_drinks.grid(row=0,column=4)

lbl_total=Label(f1, font=font, fg=fg, bd=10, text="Total")
lbl_total.grid(row=4,column=3)
txt_total=Entry(f1, font=font, fg=fg, bd=6, bg='powder blue', justify=CENTER, textvariable=total_bill)
txt_total.grid(row=4,column=4)

def price():
    price_window=Tk()
    price_window.geometry('600x200')
    price_window.title("Price List")

    lbl_info=Label(price_window, font=font, text="ITEM", fg=fg2, bd=5)
    lbl_info.grid(row=0,column=0)
    lbl_info=Label(price_window, font=font, text="_______", fg='white', bd=5)
    lbl_info.grid(row=0,column=2)
    lbl_info=Label(price_window, font=font, text="PRICE", fg=fg2, bd=5)
    lbl_info.grid(row=0,column=3)

    lbl_info=Label(price_window, font=font, fg=fg, text="Fries Meal")
    lbl_info.grid(row=1,column=0)
    lbl_info=Label(price_window, font=font, fg=fg, text="25")
    lbl_info.grid(row=1,column=3)

    lbl_info=Label(price_window, font=font, fg=fg, text="Lunch Meal")
    lbl_info.grid(row=2,column=0)
    lbl_info=Label(price_window, font=font, fg=fg, text="40")
    lbl_info.grid(row=2,column=3)

    lbl_info=Label(price_window, font=font, fg=fg, text="Burger Meal")
    lbl_info.grid(row=3,column=0)
    lbl_info=Label(price_window, font=font, fg=fg, text="35")
    lbl_info.grid(row=3,column=3)

    lbl_info=Label(price_window, font=font, fg=fg, text="Pizza Meal")
    lbl_info.grid(row=4,column=0)
    lbl_info=Label(price_window, font=font, fg=fg, text="50")
    lbl_info.grid(row=4,column=3)

    lbl_info=Label(price_window, font=font, fg=fg, text="Cheese Burger")
    lbl_info.grid(row=5,column=0)
    lbl_info=Label(price_window, font=font, fg=fg, text="30")
    lbl_info.grid(row=5,column=3)

    lbl_info=Label(price_window, font=font, fg=fg, text="Drinks")
    lbl_info.grid(row=6,column=0)
    lbl_info=Label(price_window, font=font, fg=fg, text="35")
    lbl_info.grid(row=6,column=3)

    price_window.mainloop()

def total():
    x=random.randint(1,5000)
    randomx=str(x)
    ref.set(randomx)
    cof=float(fries.get())
    col=float(lunch.get())
    cob=float(burger.get())
    cop=float(pizza.get())
    cocb=float(cheese_burger.get())
    cod=float(drinks.get())
    cost_of_fries=cof*25
    cost_of_lunch=col*40
    cost_of_burger=cob*35
    cost_of_pizza=cop*50
    cost_of_cheese_burger=cocb*30
    cost_of_drinks=cod*35
    cost_of_meal=("$",str("%.2f"%(cost_fries+cost_of_lunch+cost_of_burger+cost_of_pizza+cost_of_cheese_burger+cost_of_drinks)))
    pay_tax=((cost_fries+cost_of_lunch+cost_of_burger+cost_of_pizza+cost_of_cheese_burger+cost_of_drinks)*0.33)
    total_cost=(cost_fries+cost_of_lunch+cost_of_burger+cost_of_pizza+cost_of_cheese_burger+cost_of_drinks)
    overall_cost="$",str(pay_tax+total_cost)
    cost.set(cost_of_meal)
    total_bill.set(overall_cost)
def reset():
    ref.set('')
    fries.set('')
    lunch.set('')
    burger.set('')
    pizza.set('')
    cheese_burger.set('')
    drinks.set('')
    total_bill.set('')
    cost.set('')
def exit():
    root.destroy()
    
btn_price=Button(f1, font=font, fg=fg2, bd=10, text="Price", width=10, bg='powder blue', command=price)
btn_price.grid(row=7,column=0)

btn_total=Button(f1, font=font, fg=fg2, bd=10, text="Total", width=10, bg='powder blue', command=total)
btn_total.grid(row=7,column=1)

btn_reset=Button(f1, font=font, fg=fg2, bd=10, text="Reset", width=10, bg='powder blue', command=reset)
btn_reset.grid(row=7,column=2)

btn_exit=Button(f1, font=font, fg=fg2, bd=10, text="Exit", width=10, bg='powder blue', command=exit)
btn_exit.grid(row=7,column=3)

root.mainloop()
