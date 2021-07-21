#계산기 by 장연식
import tkinter as tk

window = tk.Tk()
window.title('YS')
window.geometry('190x270')
window.resizable(False, False)
window.wm_attributes('-topmost', 1)

calc = ""
disp = tk.StringVar()

def b_click(num):
    global calc
    calc = calc + str(num)
    disp.set(calc)
    
def equal_click():
    global calc
    try:    
        result = eval(calc)
        if str(type(result)) == "<class 'float'>":
            result = round(result, 6) 
        result_str = str(result)
        disp.set(result_str)
        calc = result_str
    except:
        calc = '계산할 수 없습니다'
        disp.set(calc)
        calc = ""
    
def clear_click():
    global calc
    calc = ""
    disp.set(calc)

def back_click():
    global calc
    calc = calc[:-1]
    disp.set(calc)

def exit():
    window.quit()
    window.destroy()
    
l1 = tk.Label(window, width=15, height=2, bd=5, anchor='e', bg='white', font='helvetica 16',textvariable=disp).grid(row=0, column=0, columnspan=4)

b_exit = tk.Button(window, text='X', width=3, height=1, font='helvetica 16', command=exit).grid(row=1, column=0)
b_clear = tk.Button(window, text='C', width=3, height=1, font='helvetica 16', command=clear_click).grid(row=1, column=1)
b_back = tk.Button(window, text='<-', width=7, height=1, font='helvetica 16', command=back_click).grid(row=1, column=2, columnspan=2)
b_plus = tk.Button(window, text='+', width=3, height=1, font='helvetica 16', command=lambda:b_click('+')).grid(row=2, column=3)
b_minus = tk.Button(window, text='-', width=3, height=1, font='helvetica 16', command=lambda:b_click('-')).grid(row=3, column=3)
b_multi = tk.Button(window, text='*', width=3, height=1, font='helvetica 16', command=lambda:b_click('*')).grid(row=4, column=3)
b_divide = tk.Button(window, text='/', width=3, height=1, font='helvetica 16', command=lambda:b_click('/')).grid(row=5, column=3)
b_equal = tk.Button(window, text='=', width=3, height=1, font='helvetica 16', command=equal_click).grid(row=5, column=2)
b_point = tk.Button(window, text='.', width=3, height=1, font='helvetica 16', command=lambda:b_click('.')).grid(row=5, column=1)
b_0 = tk.Button(window, text='0', width=3, height=1, font='helvetica 16', command=lambda:b_click('0')).grid(row=5, column=0)
b_1 = tk.Button(window, text='1', width=3, height=1, font='helvetica 16', command=lambda:b_click('1')).grid(row=4, column=0)
b_2 = tk.Button(window, text='2', width=3, height=1, font='helvetica 16', command=lambda:b_click('2')).grid(row=4, column=1)
b_3 = tk.Button(window, text='3', width=3, height=1, font='helvetica 16', command=lambda:b_click('3')).grid(row=4, column=2)
b_4 = tk.Button(window, text='4', width=3, height=1, font='helvetica 16', command=lambda:b_click('4')).grid(row=3, column=0)
b_5 = tk.Button(window, text='5', width=3, height=1, font='helvetica 16', command=lambda:b_click('5')).grid(row=3, column=1)
b_6 = tk.Button(window, text='6', width=3, height=1, font='helvetica 16', command=lambda:b_click('6')).grid(row=3, column=2)
b_7 = tk.Button(window, text='7', width=3, height=1, font='helvetica 16', command=lambda:b_click('7')).grid(row=2, column=0)
b_8 = tk.Button(window, text='8', width=3, height=1, font='helvetica 16', command=lambda:b_click('8')).grid(row=2, column=1)
b_9 = tk.Button(window, text='9', width=3, height=1, font='helvetica 16', command=lambda:b_click('9')).grid(row=2, column=2)

window.mainloop()
