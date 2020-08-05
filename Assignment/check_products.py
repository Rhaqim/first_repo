journals_found = []

file = open("products.csv", "r")

for line in file.readlines():
    product_name, product_des, product_size, date = line.split(",")
                
    

    journals_found.append({
                            "product_name":product_name,
                            "product_des":product_des,
                            "product_size":product_size,
                             })
    print()
    for index, journal in enumerate(journals_found):
        print(index+1, journal["product_name"])
    print()
    selected_option = int(input("Above are your products pick one \n> "))

    print("\n###########################")
    print(journals_found[selected_option-1]["product_name"].upper())
    print("###########################\n")
    print(journals_found[selected_option-1]["product_des"])
    print("\n###########################")
    print("###########################\n")
    print(journals_found[selected_option-1]["product_size"])
    print("\n###########################")
    print("###########################\n")

