############WORKING
from gimpfu import *
import gtk

def python_fu_test(image, drawable):
    with open("C:\\Users\\thore\\Documents\\Paradox Interactive\\Crusader Kings III\\mod\\alagasia\\map_data\\definition.csv", "r") as f:
        content = f.read().splitlines()
        f.close()
    names = []
    used_rgb_values = []
    for line in content:
        if(line!=""):
            current_line = line.split(";")
            old_rgb = (current_line[1],current_line[2],current_line[3])
            used_rgb_values.append(old_rgb)
            names.append(current_line[4])

    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_title("Test Window")
    window.connect("delete_event", gtk.main_quit)

    # Maximize the window
    window.set_default_size(500, 400)  # Width, Height
    window.maximize()

    listbox = gtk.ListStore(str)
    for i in range(len(names)):
        listbox.append([names.pop()])


    view = gtk.TreeView(listbox)
    renderer = gtk.CellRendererText()
    column = gtk.TreeViewColumn("Items", renderer, text=0)

    view.append_column(column)
    view.get_selection().connect("changed", on_selection_changed)

    scrolled_window = gtk.ScrolledWindow()
    scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
    scrolled_window.add(view)

    window.add(scrolled_window)
    window.show_all()

    gtk.main()


def on_selection_changed(selection):
    with open("C:\\Users\\thore\\Documents\\Paradox Interactive\\Crusader Kings III\\mod\\alagasia\\map_data\\definition.csv", "r") as f:
        content = f.read().splitlines()
        f.close()
    names = []
    used_rgb_values = []
    for line in content:
        if(line!=""):
            current_line = line.split(";")
            old_rgb = (current_line[1],current_line[2],current_line[3])
            used_rgb_values.append(old_rgb)
            names.append(current_line[4])

    ######
    # Get the selected item
    model, treeiter = selection.get_selected()
    if treeiter != None:
        color = model[treeiter][0]
        if color in names:
            index = names.index(color)
            gimp.set_foreground(gimpcolor.RGB(int(used_rgb_values[index][0]), int(used_rgb_values[index][1]), int(used_rgb_values[index][2])))

register(
    "python_fu_test",
    "Test Plugin",
    "Opens a new window with a listbox",
    "Your Name",
    "Your Name",
    "2024",
    "<Image>/Filters/Test/Test...",
    "*",
    [],
    [],
    python_fu_test)

main()

######Working HELLO WORLD
# #!/usr/bin/env python
#
# import gtk
# import tkinter
# from gimpfu import *
#
# def helloWorldFn() :
#     # Using gtk to display an info type message see -> http://www.gtk.org/api/2.6/gtk/GtkMessageDialog.html#GtkMessageType
#     message = gtk.MessageDialog(type=gtk.MESSAGE_INFO, buttons=gtk.BUTTONS_OK)
#     message.set_markup("Hello World \nThis Dialog Will Cause Unexpected Issues During Batch Procedures")
#     message.run()
#     message.destroy()
#
#     # Using GIMP's interal procedure database see -> http://docs.gimp.org/en/glossary.html#glossary-pdb
#     pdb.gimp_message("Hello World, This Message Looks Like An Error And/Or Warning")
#
#     # Using stdout see -> https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29
#     print "Hello World \nThis message does not show in the GUI."
#     # (Unix Terminal Output) Will not work on Windows Based Systems.
#     return
#
# # see -> http://www.gimp.org/docs/python/
# register(
#     #name
#     "helloWorldPlugin",
#
#     #blurb
#     "Saying Hello World",
#
#     #help
#     "Saying Hello to the World",
#
#     #author
#     "William Crandell <william@crandell.ws>",
#
#     #copyright
#     "William Crandell <william@crandell.ws>",
#
#     #date
#     "2015",
#
#     #menupath
#     "Hello World",
#
#     #imagetypes (use * for all, leave blank for none)
#     "",
#
#     #params
#     [],
#
#     #results
#     [],
#
#     #function (to call)
#     helloWorldFn,
#
#     #this can be included this way or the menu value can be directly prepended to the menupath
#     menu = "<Toolbox>/Hello/")
#
# main()
