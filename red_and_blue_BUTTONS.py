import tkinter as tk


def main(title):
    '''
    target: 3 label (red: +1 /counter/blue: stop counter)
    '''
    window = tk.Tk()
    window.geometry(f'250x100+800+150')
    window.title(title)
    window.mainloop()


if __name__ == '__main__':
    main('red_and_blue')
