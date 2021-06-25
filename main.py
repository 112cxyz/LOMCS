from colored import fore, back, style

#Made by TobyF#7888 & olli#9220.
i = 1

f = open('logo.txt', 'r')
file_contents = f.read()
print (fore.SKY_BLUE_2 + style.BOLD + file_contents + style.RESET)
f.close()

c = 1
while c < 4:
    print (" ")
    c += 1

print (fore.LIGHT_BLUE + style.BOLD + '[+] Welcome to' + style.RESET + fore.SKY_BLUE_2 + style.BOLD ' ' + 'LOMCS' + style.RESET)
i += 1

print (fore.)