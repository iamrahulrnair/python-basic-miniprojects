import tkinter as tk


def main(title):
    '''
    target: 3 label (red: +1 /counter/blue: stop counter)
    '''

    def if_finish():
        print(count)
        if count == 100:
            import tkinter.messagebox as mb
            title = "You WIN!"
            massage = "Congratulations!"
            mb.showwarning(title, massage)
            window.destroy()

    def add_one():
        global count
        count = count + 1
        if_finish()
        try:
            And['text'] = f'{count}'
        except BaseException as ex:
            print(f'Window is closed: {ex}')

    def stop_add():
        global count
        count = count - 2
        status = 'disabled' if Red['state'] == 'normal' else 'normal'
        Red['state'] = status


    window = tk.Tk()

    window.geometry(f'250x101+800+450')
    window.resizable(False, False)
    window.title(title)
    window.grid()

    Red = tk.Button(window, text='RED', bg='red', height=6, width=11, command=add_one)
    And = tk.Label(window, text=f'{count}', bg='white', height=6, width=10)
    Blue = tk.Button(window, text='BLUE', bg='#1E90FF', height=6, width=11, command=stop_add)

    Red.grid(row=0, column=0, sticky='NSEW')
    Blue.grid(row=0, column=3)
    And.grid(row=0, column=2)

    return window


if __name__ == '__main__':
    count = 0
    main('red_and_blue').mainloop()
