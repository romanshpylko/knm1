while True:
    word = input("Введіть своє слово: ")
    new_word = ""
    for i in word:
        new_word += chr(ord(i)+1)
        l = new_word.replace("{","a")
    print(l)

