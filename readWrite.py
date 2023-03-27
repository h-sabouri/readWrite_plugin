import nuke

'''
THIS MODULE CONTAINS FUNCTIONALITY  TO CREATE A READ NODE FROM A SELECTED WRITE NODE
'''



def create_read_from_write():


# '''
# create a read node from a selected write node
# '''

#first  store our select write node which we like to create read node from.
# second, we want to our script only to run when our selected node is write node.
# ask selected node in class python only do some action if it is write node.
    sel = nuke.selectedNode()

# if selected node is Write node , then create Read node:
    if sel.Class() == "Write":
        read = nuke.createNode("Read")
# let's set the correct location. Depending on the location of our selected Write node
# so we can use our variable read read["xpos"].setValue
        read.setXpos(int(sel["xpos"].getValue()))
        read.setYpos(int(sel["ypos"].getValue()+50))
        read["file"].setValue(sel["file"].getValue())
        read["first"].setValue(int(nuke.Root()["first_frame"].getValue()))
        read["last"].setValue(int(nuke.Root()["last_frame"].getValue()))
        read["origfirst"].setValue(int(nuke.Root()["first_frame"].getValue()))
        read["origlast"].setValue(int(nuke.Root()["last_frame"].getValue()))
        read["colorspace"].setValue(int(sel["colorspace"].getValue()))


