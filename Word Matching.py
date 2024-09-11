def match_words(words):
    count = 0
    lst = []
    
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            count = count + 1
            lst.append(word)
            
    print("List of words with first and last character same\n",lst)
    return count

li = ['abc', 'cfc', 'xyz', 'aba', '1221', "racecar", "Racist", "911","asama"]
cnt = match_words(li)

print("Number of words having first and last character same:",cnt)
