import tkinter as tk
from tkinter import messagebox

def execute_selected_statements():
    selected_statement1 = statement_var1.get()
    selected_statement2 = statement_var2.get()
    user_input1 = input_entry1.get()
    user_input2 = input_entry2.get()

    messagebox.showinfo("提示", f"选择1: {selected_statement1}\n选择2: {selected_statement2}\n输入内容1: {user_input1}\n输入内容2: {user_input2}")

# 创建主窗口
root = tk.Tk()
root.title("多个选择和输入")

# 创建说明文字标签1
instruction_label1 = tk.Label(root, text="选择操作1:")
instruction_label1.pack(padx=20, pady=5, anchor="w")

# 创建下拉选择框1
statement_var1 = tk.StringVar()
statement_choices1 = ["语句1", "语句2", "语句3"]
statement_var1.set(statement_choices1[0])
statement_dropdown1 = tk.OptionMenu(root, statement_var1, *statement_choices1)
statement_dropdown1.pack(padx=20, pady=5, anchor="w")

# 创建说明文字标签2
instruction_label2 = tk.Label(root, text="选择操作2:")
instruction_label2.pack(padx=20, pady=5, anchor="w")

# 创建下拉选择框2
statement_var2 = tk.StringVar()
statement_choices2 = ["选项A", "选项B", "选项C"]
statement_var2.set(statement_choices2[0])
statement_dropdown2 = tk.OptionMenu(root, statement_var2, *statement_choices2)
statement_dropdown2.pack(padx=20, pady=5, anchor="w")

# 创建输入框1
input_label1 = tk.Label(root, text="输入内容1:")
input_label1.pack(padx=20, pady=5, anchor="w")
input_entry1 = tk.Entry(root)
input_entry1.pack(padx=20, pady=5, anchor="w")

# 创建输入框2
input_label2 = tk.Label(root, text="输入内容2:")
input_label2.pack(padx=20, pady=5, anchor="w")
input_entry2 = tk.Entry(root)
input_entry2.pack(padx=20, pady=5, anchor="w")

# 创建执行按钮
execute_button = tk.Button(root, text="执行选中操作", command=execute_selected_statements)
execute_button.pack(padx=20, pady=10)

# 启动主循环
root.mainloop()
