import tkinter as tk

def main(title):
    '''
    target: 3 label (red: +1 /counter/blue: stop counter)
    '''

    def add_one():
        global count
        count = count + 1
        print(count)
        And['text'] = f'{count}'

    window = tk.Tk()

    window.geometry(f'250x100+800+450')
    window.resizable(False, False)
    window.title(title)
    window.grid()

    Red = tk.Button(window, text='RED', bg='red', command=add_one)
    And = tk.Label(window, text=f'{count}', bg='white')
    Blue = tk.Button(window, text='BLUE', bg='blue',  command=add_one)

    Red.grid(row=0, column=0)
    Blue.grid(row=0, column=3)
    And.grid(row=0, column=2)

    return window


if __name__ == '__main__':
    count = 0
    main('red_and_blue').mainloop()
