print("#36 Reusable Function")
message=input(">")
def emoji_converter(message):
    words=message.split(" ")
    emoji={
        ":)":"😃",
        ":(":"😌"
    }
    output=""
    for word in words:
        output+=emoji.get(word,word)+" "
    return output


print(emoji_converter(message))
# print(output)



