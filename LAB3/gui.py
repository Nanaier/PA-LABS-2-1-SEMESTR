from tkinter import *
from AVL import AVLTree, deserialize
import os

root = Tk()
root.title("AVL Tree Visualisation")
root.geometry("1080x720")
filename = "tree_serialization.txt"


def sel():
    if var.get() == 1:
        button.config(text="Insert", font=("Arial", 15), width=17, height=2)
        e1.delete(0, "end")
        e2.config(state=NORMAL)
        e2.delete(0, "end")
        message.config(state=NORMAL)
        message.delete("1.0", "end")
        message.config(state=DISABLED)

    elif var.get() == 2:
        button.config(text="Delete", font=("Arial", 15), width=17, height=2)
        e1.delete(0, "end")
        e2.config(state=NORMAL)
        e2.delete(0, "end")
        e2.config(state=DISABLED)
        message.config(state=NORMAL)
        message.delete("1.0", "end")
        message.config(state=DISABLED)

    elif var.get() == 3:
        button.config(text="Search", font=("Arial", 15), width=17, height=2)
        e1.delete(0, "end")
        e2.config(state=NORMAL)
        e2.delete(0, "end")
        e2.config(state=DISABLED)
        message.config(state=NORMAL)
        message.delete("1.0", "end")
        message.config(state=DISABLED)

    elif var.get() == 4:
        button.config(text="Edit", font=("Arial", 15), width=17, height=2)
        e1.delete(0, "end")
        e2.config(state=NORMAL)
        e2.delete(0, "end")
        message.config(state=NORMAL)
        message.delete("1.0", "end")
        message.config(state=DISABLED)


myTree = AVLTree()
treeRoot = None


def button_clicked():
    global myTree
    global treeRoot
    message.config(state=NORMAL)
    message.delete("1.0", "end")
    if var.get() == 1:
        if len(e1.get()) > 0:
            if e1.get().isdigit():
                if not myTree.isInTheTree(treeRoot, int(e1.get())):
                    if len(e2.get()) > 0:
                        key = int(e1.get())
                        data = e2.get()
                        treeRoot = myTree.insert_node(treeRoot, key, data)
                        myTree.writeToFile(treeRoot, filename)
                        message.delete("1.0", "end")
                        message.insert(INSERT, "node with key " + str(key) + " was inserted")
                        message.config(state=DISABLED)
                    else:
                        message.delete("1.0", "end")
                        message.insert(INSERT, "enter the data")
                        message.config(state=DISABLED)
                else:
                    message.delete("1.0", "end")
                    message.insert(INSERT, "enter an unique key")
                    message.config(state=DISABLED)
            elif not e1.get().isdigit():
                message.delete("1.0", "end")
                message.insert(INSERT, "enter the digit for the key")
                message.config(state=DISABLED)
        else:
            message.delete("1.0", "end")
            message.insert(INSERT, "enter the key")
            message.config(state=DISABLED)

    elif var.get() == 2:
        if len(e1.get()) > 0:
            if e1.get().isdigit():
                key = int(e1.get())
                if myTree.isInTheTree(treeRoot, key):
                    treeRoot = myTree.delete_node(treeRoot, key)
                    myTree.writeToFile(treeRoot, filename)
                    message.delete("1.0", "end")
                    message.insert(INSERT, "node with key " + str(key) + " was deleted")
                    message.config(state=DISABLED)
                else:
                    message.delete("1.0", "end")
                    message.insert(INSERT, "enter a key that exists in the tree")
                    message.config(state=DISABLED)
            elif not e1.get().isdigit():
                message.delete("1.0", "end")
                message.insert(INSERT, "enter the digit for the key")
                message.config(state=DISABLED)
        else:
            message.delete("1.0", "end")
            message.insert(INSERT, "enter the key")
            message.config(state=DISABLED)

    elif var.get() == 3:
        if len(e1.get()) > 0:
            if e1.get().isdigit():
                key = int(e1.get())
                if myTree.isInTheTree(treeRoot, key):
                    data = myTree.search(treeRoot, key)
                    message.delete("1.0", "end")
                    message.insert(INSERT, "node with key " + str(key) + " was found.\nit has data "+ data)
                    message.config(state=DISABLED)
                    e2.config(state=NORMAL)
                    e2.insert(0, data)
                    e2.config(state=DISABLED)
                else:
                    message.delete("1.0", "end")
                    message.insert(INSERT, "enter a key that exists in the tree")
                    message.config(state=DISABLED)
            elif not e1.get().isdigit():
                message.delete("1.0", "end")
                message.insert(INSERT, "enter the digit for the key")
                message.config(state=DISABLED)
        else:
            message.delete("1.0", "end")
            message.insert(INSERT, "enter the key")
            message.config(state=DISABLED)

    elif var.get() == 4:
        if len(e1.get()) > 0:
            if e1.get().isdigit() and len(e2.get()) > 0:
                key = int(e1.get())
                data = e2.get()
                if myTree.isInTheTree(treeRoot, key):
                    myTree.edit(treeRoot, key, data)
                    myTree.writeToFile(treeRoot, filename)
                    message.delete("1.0", "end")
                    message.insert(INSERT, "node with key " + str(key) + " was edited.\nit has new data "+ data)
                    message.config(state=DISABLED)
                else:
                    message.delete("1.0", "end")
                    message.insert(INSERT, "enter a key that exists in the tree")
                    message.config(state=DISABLED)
            elif not e1.get().isdigit():
                message.delete("1.0", "end")
                message.insert(INSERT, "enter the digit for the key")
                message.config(state=DISABLED)
        else:
            message.delete("1.0", "end")
            message.insert(INSERT, "enter the key")
            message.config(state=DISABLED)
    tree.config(state=NORMAL)
    tree.delete("1.0", "end")
    tree.insert(INSERT, myTree.display(treeRoot))
    tree.config(state=DISABLED)

def deleteTree():
    global treeRoot
    file = open(filename, "w")
    file.truncate()
    file.close()
    tree.config(state=NORMAL)
    tree.delete("1.0", "end")
    tree.config(state=DISABLED)
    treeRoot = None

var = IntVar()

R1 = Radiobutton(root, text="Insert", variable=var, value=1, command=sel, font=("Arial", 20), padx=10)

R2 = Radiobutton(root, text="Delete", variable=var, value=2, command=sel, font=("Arial", 20), padx=10)

R3 = Radiobutton(root, text="Search", variable=var, value=3, command=sel, font=("Arial", 20), padx=10)

R4 = Radiobutton(root, text="Edit", variable=var, value=4, command=sel, font=("Arial", 20), padx=10)

R1.grid(row=0, column=0)
R2.grid(row=1, column=0)
R3.grid(row=2, column=0)
R4.grid(row=3, column=0)

label = Label(root, text="Enter key", font=("Arial", 15))
label.grid(row=0, column=1)

e1 = Entry(root, width=30, bd=4, font=("Arial", 15))
e1.grid(row=1, column=1)

label1 = Label(root, text="Enter data", font=("Arial", 15))
label1.grid(row=2, column=1)

e2 = Entry(root, width=30, bd=4, font=("Arial", 15))
e2.grid(row=3, column=1)

button = Button(root, text='', command=button_clicked, width=25, height=3)
button.grid(row=0, column=2, rowspan=2)

buttonDeleteTree = Button(root, text='Delete database', command=deleteTree, font=("Arial", 15), width=17, height=2)
buttonDeleteTree.grid(row=4, column=2, padx=10)

message = Text(root, width=28, height=3, font=("Arial", 10))
message.grid(row=2, column=2, rowspan=2)

tree = Text(root, font=("Arial", 13))
tree.grid(row=4, column=1, rowspan=2)
if os.stat(filename).st_size != 0:
    treeRoot = deserialize(filename)
    tree.config(state=NORMAL)
    tree.delete("1.0", "end")
    tree.insert(INSERT, myTree.display(treeRoot))
    tree.config(state=DISABLED)


def main():
    root.mainloop()


if __name__ == "__main__":
    main()
