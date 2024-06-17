customer = {
  "name": 'John Smith',
  "age" : 20,
  "is_verified" : True
}
for item in customer:
  print(f"{item}:{customer[item]}")


message = input('>')
words = message.split(' ')
emojis = {
  ":)" : "😀",
  ":(" : "😠",
  ":o":"😮"
}
output = ""
for word in words:
  output += emojis.get(word, word) + ' '

print(output)