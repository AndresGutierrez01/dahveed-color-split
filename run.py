from PIL import Image
import os

directory = './pics/'
for filename in os.listdir(directory):
    if filename == '.DS_Store': 
        continue

    print('Splitting '+filename+'...')
    img = Image.open(directory+filename)
    data = img.getdata()

    # Suppress specific bands (e.g. (255, 120, 65) -> (0, 120, 0) for g)
    r = [(d[0], 0, 0) for d in data]
    g = [(0, d[1], 0) for d in data]
    b = [(0, 0, d[2]) for d in data]

    channelFilename = './rgb-channels/'+filename+'_'

    img.putdata(r)
    img.save(channelFilename+'_'+'r.png')
    img.putdata(g)
    img.save(channelFilename+'_'+'g.png')
    img.putdata(b)
    img.save(channelFilename+'b.png')



