import tkinter as tk
from tkinter import ttk

def main(title):
    '''
    target: 3 label (red: +1 /counter/blue: stop counter)
    '''

    def if_finish():
        print(count, end=',')
        if count % 100 == 0:
            import tkinter.messagebox as mb
            title = "You WIN!"
            massage = "Congratulations!"
            mb.showwarning(title, massage)
            window.destroy()

    def add_one():
        '''red button global_count add 3'''
        update_global_value(3)
        try:
            if_finish()
        except BaseException as ex:
            print(f'Window is closed: {ex}')

    def stop_add():
        '''red button is freeze and global_count add -7'''
        update_global_value(-7)
        status = 'disabled' if Red['state'] == 'normal' else 'normal'
        Red['state'] = status

    def update_global_value(value):
        global count
        count = count + (value)
        update_progress_bar()
        And['text'] = f'{count}'

    def update_progress_bar():
        if count > 100 or count < -100:
            bar['value'] = abs(count) - 100
        else:
            bar['value'] = abs(count)

    window = tk.Tk()

    window.geometry(f'250x101+800+450')
    window.resizable(False, False)
    window.title(title)
    window.grid()

    Red = tk.Button(window, text='RED', bg='red', height=5, width=11, command=add_one)
    And = tk.Label(window, text=f'{count}', bg='white', height=5, width=10)
    Blue = tk.Button(window, text='BLUE', bg='#1E90FF', height=5, width=11, command=stop_add)
    bar = ttk.Progressbar(window, orient="horizontal", mode="determinate", maximum=100)

    Red.grid(row=0, column=1, sticky='NSEW')
    Blue.grid(row=0, column=3)
    And.grid(row=0, column=2)
    bar.grid(row=1, column=0, columnspan=4, sticky='NEW')

    return window


if __name__ == '__main__':
    count = 0
    main('red_and_blue').mainloop()
