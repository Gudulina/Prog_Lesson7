import input
import ctrlv
import export

choice = input.choice

if choice == '1':
    str = input.insert()
    ctrlv.into(str)
elif choice == '2':
    export.show()
else:
    print('Такие операции я делать ещё не умею :(')