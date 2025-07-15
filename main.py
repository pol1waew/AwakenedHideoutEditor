from application import Application


app = Application()




app.load_hideout("test.hideout")

print(app.hideout.decorations_data)

#app.hideout.set_decoration_x(1, -9999)
#app.hideout.set_decoration_y(0, 999)

#print(app.hideout.decorations_data)
