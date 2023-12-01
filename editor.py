import os.path
import tkinter as tk
from tkinter import filedialog, ttk, messagebox


TITLE = "文本编辑"

class FileEdit:
    """文件编辑"""
    def __init__(self, root):
        self.root = root
        # 一级菜单
        self.menu_bar = tk.Menu(self.root)

        # 添加到窗口中
        self.root.config(menu=self.menu_bar)
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(fill=tk.BOTH, expand=1)

        # 文件选项的菜单
        self.filemenu = tk.Menu(self.menu_bar, tearoff=0, relief=tk.RAISED)
        self.filemenu.add_command(label='新建', command=self.create_file, activebackground='green')
        self.filemenu.add_command(label='打开', command=self.open_file)
        self.filemenu.add_command(label='保存', command=self.save_file, accelerator='Ctrl+S')
        self.filemenu.add_separator()
        self.filemenu.add_command(label='退出', command=self.root.quit, accelerator='Ctrl+Q')
        # 添加到菜单栏中
        self.menu_bar.add_cascade(label='文件', menu=self.filemenu)

        # 帮助菜单
        self.helpmenu = tk.Menu(self.menu_bar, tearoff=0)
        self.helpmenu.add_command(label="帮助1")
        self.menu_bar.add_cascade(label='帮助', menu=self.helpmenu)

        # 关闭
        self.menu_bar.add_command(label='关闭文件', command=self.close_file)
        self.text_area = None

    def create_file(self):
        file_path = filedialog.asksaveasfilename(title='Save As', filetypes=[('Text files', '*.txt'), ('Python files', '*.py')], defaultextension='.txt')
        if os.path.exists(file_path):
            messagebox.showinfo('创建', '创建失败，文件已存在！')
        else:
            with open(file_path, 'w') as f: pass
            self.open_file(file_path)

    def open_file(self, path=None):
        if not path:
            filepath = filedialog.askopenfilename()
        else:
            filepath = path
        try:
            if filepath:
                with open(filepath, 'r') as f:
                    content = f.read()
                    filename = os.path.basename(filepath)
                self.text_area = self.text_area_create(filename, filepath)
                self.text_area.insert('1.0', content)
        except Exception as e:
            messagebox.showerror('打开文件错误', str(e))

    def save_file(self):
        try:
            if not self.text_area: return
            content = self.text_area.get("1.0", tk.END)
            with open(self.text_area.filepath, 'w') as f:
                f.write(content)
        except Exception as e:
            messagebox.showerror('保存错误', str(e))

    def save(self, event):
        self.save_file()

    def text_area_create(self, t, path):
        """创建文本框并添加到选项卡中"""
        area = MyText(self.tab_control)
        area.filepath = path
        area.pack(fill='both', expand=1)
        area.bind('<Control-s>', self.save)
        self.tab_control.add(area, text=t)
        self.tab_control.bind("<<NotebookTabChanged>>", self.show_nowfile)
        return area
    
    def show_nowfile(self, event):
        select = self.tab_control.select()
        textobj = self.tab_control.nametowidget(select)
        if not textobj or not isinstance(textobj, tk.Text):
            nowpath = TITLE
        else:
            nowpath = textobj.filepath
        if nowpath:
            self.root.title(nowpath)
            self.root.update()

    def close_file(self):
        try:
            if self.text_area:
                current_tab = self.tab_control.select()
                self.tab_control.forget(current_tab)
                self.text_area.destroy()
            return
        except Exception as e:
            messagebox.showerror('关闭错误', str(e))


class MyText(tk.Text):
    filepath = None


def main():
    root = tk.Tk()
    root.geometry('500x300')
    root.title(TITLE)
    # root.iconbitmap('./icon/smile.ico')
    editer = FileEdit(root)
    root.mainloop()


if __name__ == '__main__':
    main()



