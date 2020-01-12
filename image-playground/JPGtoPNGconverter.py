import sys
import os
from PIL import Image

# grab first and second argument
path = sys.argv[1]
directory = sys.argv[2]

print(os.path.exists(directory))
# check if new/ exists, if not create
if not os.path.exists(directory):
    os.makedirs(directory)
# loop through Pokedex
for filename in os.listdir(path):
    img = Image.open(f'{path}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{directory}{clean_name}.png', 'png')
    print('All done!')
