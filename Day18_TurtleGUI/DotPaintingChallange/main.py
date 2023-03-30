import colorgram

colors = colorgram.extract("rainbow.jpeg", 10)
print(colors)

all_colors = []
for i in range(10):
    # get colors from "Color" object : sample - [<colorgram.py Color: Rgb(r=254, g=254, b=254), 45.22913051544817%>, <colorgram.py Color: Rgb(r=220, g=157, b=39), 10.092874526623667%> ]
    store_iteration_rgb = colors[i]
    # get Rgb
    get_color_rgb = store_iteration_rgb.rgb
    print(f"get color variable : {get_color_rgb}\n")
    # get r, g, b
    r = get_color_rgb.r
    g = get_color_rgb.g
    b = get_color_rgb.b
    final_colors = (r, g, b)
    all_colors.append(final_colors)

print(all_colors)


