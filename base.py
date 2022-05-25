from appJar import gui

#event function
def press(button):
    if button == "Cancel":
        app.stop()
    elif button == "PS5s":
        greeting()
    elif button == "GPUs":
        print('GPU function here')
    else:
        print('Pick a valid option')

#creating GUI variable, appearance 
app = gui("Storefront", "400x200")
app.setBg("blue") #background
app.setFont(18)

# add & configure widgets - 
app.addLabel("title", "Welcome to Bottom Feeders Emporium")
app.setLabelBg("title", "Black") #title background color
app.setLabelFg("title", "white") #letter color

# link the buttons to the function called press
app.addButtons(["PS5s", "GPUs"], press)
app.addButton('Cancel', press)
# start the GUI
#app.go()
