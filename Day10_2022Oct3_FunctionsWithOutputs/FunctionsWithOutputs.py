def format_name(f_name, l_name):
    lower_fname = f_name.title()
    lower_lname = l_name.title()
    full_name = lower_fname + " " + lower_lname
    # print(f"{full_name}")
    return f"{full_name}"

formatted_string = format_name("seDlieDsS", "seDlieDsS")
print(formatted_string)




