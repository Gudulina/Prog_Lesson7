import input
import ctrlv
import export

def start():
    if input.choice() == '1':
        ctrlv.into(input.insert())
    elif input.choice() == '2':
        export.show(input.inp_show)
    else:
        print('Такие операции я делать ещё не умею :(')