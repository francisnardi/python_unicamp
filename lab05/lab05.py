import sys
x = []
z = sys.stdin.readlines()

for item in z[1:]:
    x.append(item.strip())

    
def find_num_word(y):
    for item in y:
        if item.isdigit() or ((item[0] == "-" and item[1:].isdigit())) or item.isalpha():
            print(item)

            
def find_hashtag(y):
    hashtag = 0
    for item in y:
        if item[0] == "#":
            if item[1:].isalpha() or item[1:].isdigit():
                #print(item)
                hashtag = hashtag + 1
    if hashtag == 1:
        print("1 hashtag foi removida.")
    elif hashtag > 1:
        print(hashtag, "hashtags foram removidas.")

def find_emoticon(y):
    emoticon = 0
    for item in y:
        if not item.isdigit() and not item.isalpha() and not ((item[0] == "#" and (item[1:].isalpha() or item[1:].isdigit()))) and not ((item[0] == "-" and item[1:].isdigit())):
                #print(item)
                emoticon = emoticon + 1          
    if emoticon == 1:
        print("1 emoticon foi removido.")
    elif emoticon > 1:
        print(emoticon, "emoticons foram removidos.")

        
find_num_word(x)
find_hashtag(x)
find_emoticon(x)