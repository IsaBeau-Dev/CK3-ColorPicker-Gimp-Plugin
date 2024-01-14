from gimpfu import *
import gtk

path = "C:\\Users\\thore\\Documents\\Paradox Interactive\\Crusader Kings III\\mod\\alagasia\\map_data\\definition.csv"
def isabeau_ck_3_plugin():
    #with open("C:\\Users\\thore\\Documents\\Paradox Interactive\\Crusader Kings III\\mod\\alagasia\\map_data\\definition.csv", "r") as f:
    with open(path, "r") as f:
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

    # # Using stdout see -> https://en.wikipedia.org/wiki/Standard_streams#Standard_output_.28stdout.29
    # print "Hello World \nThis message does not show in the GUI."
    # # (Unix Terminal Output) Will not work on Windows Based Systems.
    # return


def on_selection_changed(selection):
    #with open("C:\\Users\\thore\\Documents\\Paradox Interactive\\Crusader Kings III\\mod\\alagasia\\map_data\\definition.csv", "r") as f:
    with open(path, "r") as f:
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
    #name
    "CK3ColorPickerPlugin",

    #blurb
    "This plugin looks up the colors in your definition.csv and opens a window where you can select a province based on name. The Plugin then pastes the color defined for that province in your color tool, so you can draw the according province directly in your provinces.png.",


    #help
    "This plugin looks up the colors in your definition.csv and opens a window where you can select a province based on name. The Plugin then pastes the color defined for that province in your color tool, so you can draw the according province directly in your provinces.png.",


    #author
    "IsaBeau-Dev <https://github.com/IsaBeau-Dev>",

    #copyright
    "IsaBeau-Dev <https://github.com/IsaBeau-Dev>",

    #date
    "2024",

    #menupath
    "CK3 ColorPicker Plugin",

    #imagetypes (use * for all, leave blank for none)
    "",

    #params
    [],

    #results
    [],

    #function (to call)
    isabeau_ck_3_plugin,

    #this can be included this way or the menu value can be directly prepended to the menupath
    menu = "<Toolbox>/CK3/")

main()
