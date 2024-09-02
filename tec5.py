def inverter_string(string):
    nova_string = ""
    for i in range(len(string) - 1, -1, -1):
        nova_string += string[i]
    return nova_string


string = "Olá, eu sou o Wellington!"
print(inverter_string(string))