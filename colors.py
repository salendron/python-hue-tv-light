import  Image, ImageFilter
from rgbxy import Converter, GamutC

converter = Converter(GamutC)

def frameToColorMapImage(frame):
    im = Image.fromarray(frame)
    #im = im.resize((150,150))
    im = im.filter(ImageFilter.GaussianBlur(5))
    im = im.resize((3,3))
    return im

def getRGBXYBri(im,idx):
        r, g, b = im.getpixel((idx[0], idx[1]))
        
        x,y = converter.rgb_to_xy(r,g,b)
        
        bri = (0.299*float(r) + 0.587*float(g) + 0.114*float(b))
        
        bri = bri if bri > 100 else ((bri / 100) * bri)
        bri = bri if bri > 30 else bri / 2
        bri = bri if bri > 7 else 0
        
        return (r,g,b,x,y,bri)
