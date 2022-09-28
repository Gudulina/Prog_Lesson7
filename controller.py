import input
import ctrlv
import export
import edit

def start():
    data = input.choice()
    if data == '1':
        ctrlv.into(input.insert())
    elif data == '2':
        export.show(input.inp_show())
    elif data == '3':
        edit.change(input.inp_edit(), input.exp_edit())
    else:
        print('Такие операции я делать ещё не умею :(')
        print()
        start()