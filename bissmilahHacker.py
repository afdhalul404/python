import ascii_magic

try:
   my_art = ascii_magic.from_image_file('logo.jpg')
   ascii_magic.to_terminal(my_art)
except Exception as e:
   print('Error Bossq !!!!',e)
