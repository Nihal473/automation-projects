from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
pathOut = './imagesEdited'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    #editing the image
    enhancer = ImageEnhance.Sharpness(img)
    sharp_img = enhancer.enhance(2)
    filtered_img = sharp_img.filter(ImageFilter.BLUR)
    filtered_img.save(f"{pathOut}/{filename}")
    print(f"Edited {filename}")
    # resizing the image
    resized_img = filtered_img.resize((128, 128))
    resized_img.save(f"{pathOut}/{filename[:-4]}_resized.jpg")
    print(f"Resized {filename[:-4]}_resized.jpg")

print("All images processed")



