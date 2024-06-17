def emojis_converter(message):
  words = message.split(' ')
  emojis = {
  ":)" : "😀",
  ":(" : "😠",
  ":o":"😮"
}
  output = ""
  for word in words:
    output += emojis.get(word, word) + ' '
  return output


message = input('>')
result = emojis_converter(message) 
print(result)
