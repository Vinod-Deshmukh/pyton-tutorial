print("#31 Emoji Convertor Program")
message=input(">")
words=message.split(" ")
emoji={
    ":)":"😃",
    ":(":"😌"
}
output=""
for word in words:
    output+=emoji.get(word,word)+" "
print(output)



