def generate_wordlist_file(name, start, end, filename):
    with open(filename, 'w') as file:
        for i in range(start, end+1):
            word = f"{name}{i}\n"
            file.write(word)

name = "techyperry" #enter name of victim
start_index = 1
end_index = 100000 #enter Wordlist number
filename = "wordlist.txt"

generate_wordlist_file(name, start_index, end_index, filename)
print("Wordlist generated successfully! @techyperry_|Parth sharma")
