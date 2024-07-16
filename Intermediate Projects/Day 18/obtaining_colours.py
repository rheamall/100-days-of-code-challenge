import colorgram as cg

colours = cg.extract('hirst dot painting.png', 20)

def get_colours(index):
    r = colours[index].rgb[0]
    g = colours[index].rgb[1]
    b = colours[index].rgb[2]
    colour = (r, g, b)
    return colour

colours_list = []
for i in range(20):
    colour = get_colours(i)
    colours_list.append(colour)
#print(colours_list)

# deleting the white-ish colours from the list and only retaining other colours
final_colours = [(236, 225, 82), (202, 5, 71), (235, 50, 129), (199, 165, 9),
                 (208, 75, 11), (108, 179, 219), (220, 161, 102), (235, 225, 5),
                 (31, 189, 109), (23, 106, 173), (213, 135, 176), (18, 29, 172),
                 (14, 25, 66), (9, 186, 214), (229, 167, 197), (207, 28, 140)]
