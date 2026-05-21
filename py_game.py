# print("hello ")
import addimages

addimages.init()
screen = addimages.display.set_mode((400,500))

done = False
while not done:
    for event in addimages.event.get():
        if event.type == addimages.QUIT:
            done = True
    addimages.display.flip()