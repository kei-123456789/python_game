import tkinter

pnum = 0
def photograph():
    global pnum
    canvas.delete('PH')
    canvas.create_image(400, 300, image=photo[pnum], tag='PH')
    pnum += 1
    if pnum >= len(photo):
        pnum = 0
    root.after(2000, photograph)

root = tkinter.Tk()
root.title('デジタルフォトフレーム')
canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()
photo = [
tkinter.PhotoImage(file="D:\python_game\Lesson8\cat00.png"),
tkinter.PhotoImage(file="D:\python_game\Lesson8\cat01.png"),
tkinter.PhotoImage(file="D:\python_game\Lesson8\cat02.png"),
tkinter.PhotoImage(file="D:\python_game\Lesson8\cat03.png")
]
photograph()
root.mainloop()