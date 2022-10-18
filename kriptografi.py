import string


res = ""
plainteks = input("Masukan Plainteks\t: ")
key = int(input("Masukan kunci\t\t: "))

# for x in range(len(plainteks)):
#     if plainteks[x].isupper():
#       enc = (string.ascii_uppercase.index(plainteks[x]) + key) % 26
#       res += string.ascii_uppercase[enc]
#     elif plainteks[x].islower():
#       enc = (string.ascii_lowercase.index(plainteks[x]) + key) % 26
#       res += string.ascii_lowercase[enc]
#     else:
#       res += plainteks[x]

# print(res)

for x in range(len(plainteks)):
    if plainteks[x].isupper():
      enc = (string.ascii_uppercase.index(plainteks[x]) - key) % 26
      res += string.ascii_uppercase[enc]
    elif plainteks[x].islower():
      enc = (string.ascii_lowercase.index(plainteks[x]) - key) % 26
      res += string.ascii_lowercase[enc]
    else:
      res += plainteks[x]

print(res)



