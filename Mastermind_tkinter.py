import tkinter as tk
import random
#Create the window where the app will run
window = tk.Tk()

###
# 
# Add a reset button that allows you to start over with a new code, once you've cracked it
# 
###

welcome = '''Welcome to the C0de Crack3r! To crack the code, 
type in a three digit code, then press Check! 
X = correct number and placement 
O = correct number but wrong placement'''

#This was created so that when a reset button is pressed, the create_code may be run again, creating a new code
def create_code():
    global code
    code = str(random.randint(100,999))
    print(code)
#for testing
create_code()
print(code)

def check_int(event):
    try:
        int(entry_code_attempt.get())
        check()
    except ValueError:
        results_listbox.insert(tk.END, "Invalid Entry!")
        results_listbox.see(tk.END)
        entry_code_attempt.delete(0, tk.END)

def check(): #This will insert what is in the code_attempt Entry
    
    correct_placement = 0
    correct_number = 0
    code_attempt = entry_code_attempt.get()

    if len(code_attempt) > 3:
        results_listbox.insert(tk.END, "This code attempt was too long!")
        results_listbox.see(tk.END)
        entry_code_attempt.delete(0, tk.END)
        return

    elif len(code_attempt) < 3:
        results_listbox.insert(tk.END, "This code attempt was too short!")
        results_listbox.see(tk.END)
        entry_code_attempt.delete(0, tk.END)
        return

    temp_code_attempt = list(str(entry_code_attempt.get()))

    first_digit = 'not checked'
    second_digit = 'not checked'
    third_digit = 'not checked'

    
    if code_attempt == code:
        results_listbox.insert(tk.END, "{} is CORRECT! YOU WIN!".format(code_attempt))
        results_listbox.see(tk.END)
        entry_code_attempt.delete(0, tk.END)
        entry_code_attempt.config(state="disabled")
    
    else:

#Find out how many numbers are correct and in the correct place
#When a number is fully correct, it also puts a 'check' where it is in the temp code, so that it won't be recounted in the existance check

#FIRST digit test   
        if code[0] == code_attempt[0]:
            correct_placement += 1
            first_digit = 'check'
            temp_code_attempt[0] = 'check'
#SECOND digit test 
        if code[1] == code_attempt[1]:
            correct_placement += 1
            second_digit = 'check'
            temp_code_attempt[1] = 'check'
#THIRD digit test
        if code[2] == code_attempt[2]:
            correct_placement += 1
            third_digit = 'check'
            temp_code_attempt[2] = 'check'

# # # Existance check! # # # 
    
        #first check
        if first_digit != 'check':
            if code[0] == temp_code_attempt[0]:
                correct_number += 1
                temp_code_attempt[0] = 'check'
            if code[0] == temp_code_attempt[1]:
                correct_number += 1
                temp_code_attempt[1] = 'check'
            if code[0] == temp_code_attempt[2]:
                correct_number += 1
                temp_code_attempt[2] = 'check'
        #second check
        if second_digit != 'check':
            if code[1] == temp_code_attempt[0]:
                correct_number += 1
                temp_code_attempt[0] = 'check'
            if code[1] == temp_code_attempt[1]:
                correct_number += 1
                temp_code_attempt[1] = 'check'
            if code[1] == temp_code_attempt[2]:
                correct_number += 1
                temp_code_attempt[2] = 'check'
        #third check
        if third_digit != 'check':
            if code[2] == temp_code_attempt[0]:
                correct_number += 1
                temp_code_attempt[0] = 'check'
            if code[2] == temp_code_attempt[1]:
                correct_number += 1
                temp_code_attempt[1] = 'check'
            if code[2] == temp_code_attempt[2]:
                correct_number += 1
                temp_code_attempt[2] = 'check'

        results = []
        for num in range(correct_placement):
            results.append('X')
        for num in range(correct_number):
            results.append('O')

        results_for_listbox = ''.join(results)
        code_attempt_for_listbox = str(code_attempt)

        results_listbox.insert(tk.END, code_attempt_for_listbox+'   '+results_for_listbox) #this add our results to the box
        entry_code_attempt.delete(0, tk.END) #This empties out the Entry field
        results_listbox.see(tk.END) #This will 'show' the last item in the list, scrolling with the attempts through the list

def reset_game():
    entry_code_attempt.delete(0,tk.END)
    results_listbox.delete(0,tk.END)
    create_code()
    entry_code_attempt.config(state="normal")


#Create the greeting and instructions at the top of the window
greeting = tk.Label(window,text=welcome)
greeting.grid(row=0,column=0,columnspan=2,padx="120")

#Entry box where code will be attempted
entry_code_attempt = tk.Entry(window,width=15)
entry_code_attempt.grid(row=1,column=0,padx="60")

#This button goes in next to the code entry and will 'get' the information from the entry widget and executes the 'check_int' and then the 'check' function
b = tk.Button(window, text="Check!", width=15, command=check_int)
b.grid(row=1,column=1,padx="60")
window.bind('<Return>', check_int) #binds Return key to function 'check'
window.bind('Enter', check_int) 

#This creates the results 'listbox' and scrolling feature
scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL)
results_listbox = tk.Listbox(window, width=50, xscrollcommand=scrollbar.set) #add xscrollcommand
scrollbar.grid(row=2,column=1)
results_listbox.grid(row=2,column=0,columnspan=2)

#Reset button
reset_b = tk.Button(window, text="Reset",width=42, command=reset_game)
reset_b.grid(row=3,column=0,columnspan=2)

window.geometry("500x300")
window.title('C0de Crack3r!')
window.mainloop()
