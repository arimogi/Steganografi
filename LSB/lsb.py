# ================================= #
#    Contoh Stegano Metode LSB      #
#    jalankan dengan python3        #
# ================================= #

from PIL import Image

def genData(data):
	newd = []
	for i in data:
		newd.append(format(ord(i), '08b'))
	return newd
 
def modPix(pix, data): 
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)
 
    for i in range(lendata):
 
        pix = [value for value in imdata.__next__()[:3] +
                                imdata.__next__()[:3] +
                                imdata.__next__()[:3]]
 
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j]% 2 != 0):
                pix[j] -= 1
 
            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if(pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
 
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if(pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1
 
        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1
 
        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]
 
def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)
 
    for pixel in modPix(newimg.getdata(), data):
 
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1

def encode():
    img = input("Enter image name(with extension): ")
    #
    # You can use either short path or full path
    # short path: fruits.jpeg
    # full path: /home/arimogi/Projects/Python/Steganografi/Tugas-1/fruits.jpeg
    #
    print("Open file: " + img)
    image = Image.open(img, 'r')
 
    data = input("Enter data to be encoded: ")
    if (len(data) == 0):
        raise ValueError('Data is empty')
 
    newimg = image.copy()
    encode_enc(newimg, data)
        
    new_img_name = str(img.split(".")[0]) + "_encoded." + str(img.split(".")[1])
    print("\nSaving to: " + new_img_name + "\n")
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

def decode():
    img = input("Enter image name(with extension): ")
    image = Image.open(img, 'r')
 
    data = ''
    imgdata = iter(image.getdata())
 
    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                                imgdata.__next__()[:3] +
                                imgdata.__next__()[:3]]
 
        binstr = ''
 
        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'
 
        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data
            
def imgProp():
    img = input("Enter image name(with extension): ")
    #
    # You can use either short path or full path
    # short path: fruits.jpeg
    # full path: /home/arimogi/Projects/Python/Steganografi/Tugas-1/fruits.jpeg
    #
    print("Open file: " + img)
    image = Image.open(img, 'r')
    
    print("Width : ", image.width, "")
    print("Height: ", image.height, "")
    print("Pixel : ", image.width * image.height, " pixels")
    print("----------------------")
 
def main():	
    inMenu = int(input(":: Steganography ::\n"
                        "1. Encode\n2. Decode\n3. Image properties\n4. Exit\nSelect: "))
    isContinue = 1
    
    if (inMenu == 1):
        encode()
        
    elif (inMenu == 2):
        print("Decoded Word :  " + decode())
        
    elif(inMenu == 3):
        print("Image properties:\n")
        imgProp()
		
    elif(inMenu == 4):
        isContinue = 0
        print("End program.")        
		
    else:
        raise Exception("Enter correct input")
        
    return isContinue

if __name__ == '__main__' :
	
	isRun = 1
	
	while(isRun == 1):
		isRun = main()
