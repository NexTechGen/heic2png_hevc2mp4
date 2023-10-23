from heic2png import HEIC2PNG
import os
from tqdm import tqdm

# heic_img = HEIC2PNG('20220620_155225.heic', quality=90)  # Specify the quality of the converted image
# heic_img.save("test.png")  # The converted image will be saved as `test.png`


dir = "C:\\Users\WELCOME\heic2png\chan"

dir_list = os.listdir(dir)


for name in tqdm(dir_list):
    #print(name)
    l = dir+"\\"+name
    save_name = name.split(".")[0]
    #print(l)
    #print(save_name)

    heic_img = HEIC2PNG(l, quality=90)
    heic_img.save("C:\\Users\WELCOME\heic2png\chan1\\"+save_name+".png")
    print(f"{save_name} Saved!")