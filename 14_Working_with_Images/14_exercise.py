from PIL import Image

words = Image.open("word_matrix.png")

#words.show()

mask = Image.open("mask.png")

#mask.show()

print(words.size)
words_height, words_width = words.size
print(words_height)
print(words_width)
print(mask.size)
new_mask = mask.resize((words_height,words_width))

new_mask.putalpha(200)
words.paste(im=new_mask,box=(0,0))
words.show()