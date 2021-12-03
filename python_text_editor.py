import random

def show():
    print("=================")
    for i in range(len(notes)):
        print(notes[i])
    print("=================")

notes = []

def write():
    print("Write in English.")
    print("To exit write(add) mode, input \"::break\" at final line.")
    while True:
        word = input()
        if word == "::break":
            return
        notes.append(word)

write()

while True:
    show()

    cmd = input("Use command to edit : ")
    if cmd == "::finish":
        print("\n")
        show()
        file_name = input("File name : ")
        f = open(file_name, 'a')
        for i in notes:
            f.write(i)
            f.write('\n')
        f.close()
        print("Text file saved as '{0}'.\nAll tasks finished." .format(file_name))
        break
    
    elif cmd == "cutLine":
        print("-------------------")
        print("input range to cut (follow below)")
        print("[target Y axis]")
        target = int(input("--> "))
        notes.pop(target)
        
    elif cmd == "add":
        print("-------------------")
        write()
        
    elif cmd == "replace":
        print("-------------------")
        print("input to replace (follow below)")
        print("[target alphabet] [to switch]")
        before, after = input().split()
        print(before)
        print(after)
        for i in range(len(notes)):
            notes[i] = notes[i].replace(before, after)
            
    elif cmd == "random":
        print("-------------------")
        print("input to draw amount (follow below)")
        print("[draw amount]")
        draw_amount = int(input())
        draw_list = []
        for i in range(draw_amount):
            rand_index = random.randrange(0, len(notes))
            draw_list.append(notes[rand_index])
        print("Random Draw Result:")
        for i in range(draw_amount):
            print("%s. %s" % (i+1, draw_list[i]))
            
    else:
        print(cmd, ": Error command.")






