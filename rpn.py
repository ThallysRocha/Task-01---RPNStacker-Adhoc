stack = []
f = open("Calc1.stk", "r")

for line in [l.rstrip() for l in f.readlines()]:
    if(line.isalnum()):
        stack.append(int(line))
    elif(len(stack)>=2):
        if(line == '*' ):
            stack.append(stack.pop()*stack.pop())
        elif(line == '/'):
            stack.append(int(1/stack.pop()*stack.pop()))
        elif(line == '-'):
            stack.append((-stack.pop()) + stack.pop())
        elif(line == '+'):
            stack.append(stack.pop()+stack.pop())
    else:
        print("Não há números o suficiente para executar as operações, o último valor calculado foi: "+str(stack.pop()))
        break

if(len(stack) == 1):
    print(stack.pop())
elif(len(stack) > 1):
    print("Sobraram estes números na pilha: "+str(stack))