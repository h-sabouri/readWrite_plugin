#in menu.py we import or modules
import nuke
import readWrite

# we want to extend our menu bar in nuke to add new commands to nuke's menu bar we can use built-in function addCommand():
# first we need to address the menu bar by nuke.menu()in the parenthesis we have to write the section that we like to call
#to add new command to menu bar we can use function addCommand(),
# it expects some parameters, 1- the location we want to add the command 2- the name

nuke.menu("Nuke").addCommand("utilities/create read from write", "readWrite.create_read_from_write()", "alt+j")
# which function called when we click this menu entry,
# this is the function(create_read_from_write) we define it in readWrite module.
