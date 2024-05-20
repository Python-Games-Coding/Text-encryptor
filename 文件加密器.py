from tkinter import messagebox, simpledialog, Tk, Button

def IsEven(number):
    return number % 2 == 0

def GetEvenLetters(message):
    EvenLetters = []
    for counter in range(0, len(message)):
        if IsEven(counter):
            EvenLetters.append(message[counter])
    return EvenLetters

def GetOddLetters(message):
    OddLetters = []
    for counter in range(0, len(message)):
        if not IsEven(counter):
            OddLetters.append(message[counter])
    return OddLetters

def SwapLetters(message):
    LetterList = []
    if not IsEven(len(message)):
        message = message + 'X'
    EvenLetters = GetEvenLetters(message)
    OddLetters = GetOddLetters(message)
    for counter in range(0, int(len(message)/2)):
        LetterList.append(OddLetters[counter])
        LetterList.append(EvenLetters[counter])
    NewMessage = ''.join(LetterList)
    return NewMessage

def GetTask():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?\n 1. encrypt\n 2. decrypt')
    return task

def GetMessage():
    message = simpledialog.askstring('Message', 'Enter the secret message:')
    return message

root = Tk()

while True:
    task = GetTask()
    if task == '1':
        message = GetMessage()
        encrypted = SwapLetters(message)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
    elif task == '2':
        message = GetMessage()
        decrypted = SwapLetters(message)
        messagebox.showinfo('Ciphertext of the secret message is:', decrypted)
    else:
        break
root.mainloop()