import tkinter as tk

class Group:
  """provide a component like this
  input:
  _______
  confirm button
  _result__
  """
  class Group:
    def __init__(self, input_prompt, button_text, button_command=None):
        self.label = tk.Label(root, text=input_prompt)
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        if nnot button_command:
            funct = self.func
        else:
            funct = button_command

        self.btn = tk.Button(root, text=button_text, command=funct)
        self.btn.pack()

        self.show = tk.Label(root, text='')
        self.show.pack()
        
  
    if __name__ == '__main__':
    root = tk.Tk()
    root.title = 'time parser'
    label = tk.Label(root, text='请输入ULID：')
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    btn = tk.Button(root, text='解析', command=paser_ulid)
    btn.pack()

    show = tk.Label(root, text='')
    show.pack()
    root.mainloop()
