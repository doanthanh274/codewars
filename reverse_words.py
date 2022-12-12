def reverse_words(text):
    text_space_split = text.replace(" ","* *").split('*')
    string_reversed = ""
    for i in range(len(text_space_split)):
        string_reversed+=text_space_split[i][::-1]
    return(string_reversed)

def community_solution(str):
    return ' '.join(s[::-1] for s in str.split(' '))

print(community_solution(input()))