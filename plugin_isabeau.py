# from gimpfu import *
# import gtk
# import csv
#
# def python_fu_test(image, drawable):
#     names = []
#     with open("C:\\Users\\thore\\Documents\\Paradox Interactive\\Crusader Kings III\\mod\\alagasia\\map_data\\definition.csv", "r") as f:
#         reader = csv.reader(f, delimiter=';')
#         for row in reader:
#             if row:
#                 names.append(int(row[4]))
#
#     window = gtk.Window(gtk.WINDOW_TOPLEVEL)
#     window.set_title("Test Window")
#     window.connect("delete_event", gtk.main_quit)
#
#     liststore = gtk.ListStore(str)
#     for name in names:
#         liststore.append([str(name)])
#
#     view = gtk.TreeView(liststore)
#     renderer = gtk.CellRendererText()
#     column = gtk.TreeViewColumn("Names", renderer, text=0)
#     view.append_column(column)
#
#     window.add(view)
#     window.show_all()
#
#     gtk.main()
#
# register(
#     "python_fu_test",
#     "Test Plugin",
#     "Opens a new window with a listbox",
#     "Your Name",
#     "Your Name",
#     "2024",
#     "<Image>/Filters/Test/Test...",
#     "*",
#     [],
#     [],
#     python_fu_test)
#
# main()


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

    #names = ["Item1","Green"]
    # names.append("Green")

    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_title("Test Window")
    window.connect("delete_event", gtk.main_quit)

    # Maximize the window
    window.set_default_size(300, 200)  # Width, Height
    window.maximize()
    # # Set the default size of the window
    # window.set_default_size(300, 200)  # Width, Height


    listbox = gtk.ListStore(str)
    for i in range(len(names)):
        listbox.append([names.pop()])
    # for i in range(10):
    #     listbox.append(["Item %d" % i])
    # for name in names:
    #     liststore.append(["%s" % name])


    view = gtk.TreeView(listbox)
    renderer = gtk.CellRendererText()
    column = gtk.TreeViewColumn("Items", renderer, text=0)
    ###added v2
    # Set a cell data function for the column
    column.set_cell_data_func(renderer, colorize)
    #######


    view.append_column(column)

    view.get_selection().connect("changed", on_selection_changed)

    scrolled_window = gtk.ScrolledWindow()
    scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
    scrolled_window.add(view)

    window.add(scrolled_window)


    #window.add(view)
    window.show_all()

    gtk.main()


def on_selection_changed(selection):

    ######added v3
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

        # # Set the foreground color based on the selected item
        # if color == "Item 1":
        #     #pdb.gimp_context_set_foreground(gimpcolor.RGB(0, 0, 255))
        #     gimp.set_foreground(gimpcolor.RGB(0, 0, 255))
        # elif color == "Green":
        #     #pdb.gimp_context_set_foreground(gimpcolor.RGB(0, 255, 0))
        #     gimp.set_foreground(gimpcolor.RGB(0, 255, 0))
        # elif color == "Red":
        #     #pdb.gimp_context_set_foreground(gimpcolor.RGB(255, 0, 0))
        #     gimp.set_foreground(gimpcolor.RGB(255, 0, 0))

        ######added v2
        if color in names:
            index = names.index(color)
            gimp.set_foreground(gimpcolor.RGB(int(used_rgb_values[index][0]), int(used_rgb_values[index][1]), int(used_rgb_values[index][2])))
        #######


####added v2
# Cell data function to colorize the items
def colorize(column, cell, model, iter):
    item = model.get_value(iter, 0)
    if item == "b_test_107":
        cell.set_property('background', 'blue')
    elif item == "Green":
        cell.set_property('background', 'green')
    elif item == "Red":
        cell.set_property('background', 'red')
    else:
        cell.set_property('background', 'white')
########
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
#
#

#####################
# # Import the modules
# import tkinter
# from gimpfu import *
#
# # Define the plugin function
# def new_window_with_listbox():
#     # Create a root window
#     root = tkinter.Tk()
#     # Hide the root window
#     root.withdraw()
#     # Create a Toplevel window
#     top = tkinter.Toplevel(root)
#     # Set the title of the window
#     top.title("New Window with Listbox")
#     # Create a frame to hold the widgets
#     frame = tkinter.Frame(top)
#     frame.pack()
#     # Create a listbox widget
#     listbox = tkinter.Listbox(frame)
#     # Insert some items to the listbox
#     listbox.insert("end", "Item 1")
#     listbox.insert("end", "Item 2")
#     listbox.insert("end", "Item 3")
#     # Create a scrollbar widget
#     scrollbar = tkinter.Scrollbar(frame)
#     # Configure the scrollbar to scroll the listbox
#     scrollbar.config(command=listbox.yview)
#     listbox.config(yscrollcommand=scrollbar.set)
#     # Grid the widgets
#     listbox.grid(row=0, column=0, sticky="nsew")
#     scrollbar.grid(row=0, column=1, sticky="ns")
#     # Make the window modal
#     top.grab_set()
#     # Start the main loop
#     root.mainloop()
#
# # Register the plugin
# register(
#     "new_window_with_listbox", # Name of the plugin
#     "Open a new window with listbox inside GIMP plugin", # Description of the plugin
#     "Open a new window with listbox inside GIMP plugin", # Help text of the plugin
#     "Your Name", # Author of the plugin
#     "Your Name", # Copyright holder of the plugin
#     "2024", # Date of the plugin
#     "Hello World", # Menu path of the plugin
#     "", # Image types that the plugin works on
#     [], # Input parameters of the plugin
#     [], # Output parameters of the plugin
#     new_window_with_listbox, # Function to call when the plugin is executed
#      #this can be included this way or the menu value can be directly prepended to the menupath
#     menu = "<Toolbox>/Hello/"
# )
#
# # Run the plugin
# main()




############
# from gimpfu import *
# import gtk
# import gimpcolor
# import pdb
#
# def create_listbox():
#     # Create a new window
#     window = gtk.Window()
#     window.set_title("Listbox Example")
#     window.connect("destroy", gtk.main_quit)
#
#     # Create a list store
#     liststore = gtk.ListStore(str)
#
#     # Add some items to the list store
#     liststore.append(["Blue"])
#     liststore.append(["Green"])
#     liststore.append(["Red"])
#
#     # Create a tree view
#     treeview = gtk.TreeView(liststore)
#
#     # Create a column for the list items
#     column = gtk.TreeViewColumn("Items")
#
#     # Add the column to the tree view
#     treeview.append_column(column)
#
#     # Create a cell renderer for the column
#     cell = gtk.CellRendererText()
#
#     # Add the cell renderer to the column
#     column.pack_start(cell, True)
#     column.add_attribute(cell, "text", 0)
#
#     # Add a selection changed callback function
#     #treeview.get_selection().connect("changed", on_selection_changed)
#
#     # Add the tree view to the window
#     window.add(treeview)
#
#     # Show the window
#     window.show_all()
#
# def on_selection_changed(selection):
#     # Get the selected item
#     model, treeiter = selection.get_selected()
#     if treeiter != None:
#         color = model[treeiter][0]
#
#         # Set the foreground color based on the selected item
#         if color == "Blue":
#             #pdb.gimp_context_set_foreground(gimpcolor.RGB(0, 0, 255))
#             gimp.set_foreground(gimpcolor.RGB(0, 0, 255))
#         elif color == "Green":
#             #pdb.gimp_context_set_foreground(gimpcolor.RGB(0, 255, 0))
#             gimp.set_foreground(gimpcolor.RGB(0, 255, 0))
#         elif color == "Red":
#             #pdb.gimp_context_set_foreground(gimpcolor.RGB(255, 0, 0))
#             gimp.set_foreground(gimpcolor.RGB(255, 0, 0))
#
# # Call the create_listbox function to create the window
# create_listbox()
#
#
# register(
#     "python_fu_color_selector",
#     "Select foreground color based on user choice",
#     "Opens a window with color options",
#     "Your Name",
#     "Your Name",
#     "2024",
#     "<Image>/Filters/Colors/Color Selector",
#     "",
#     [],
#     [],
#     on_selection_changed
# )
#
# main()
