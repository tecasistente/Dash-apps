
import PIL
from PIL import Image
from tkinter.filedialog import *
from gingerit.gingerit import GingerIt

'''

'''

def chage_image():
    fl=askopenfilenames()
    img = Image.open(fl[0])
    img.save("output.png", "PNG", optimize = True, quality = 10)


'''
Check if exist a looks for a grammatical error 
and if there is, fixes it
Arguments:
    text: string
Returns:
    corrected_text: string
'''
def check_text(text):
    corrected_text = GingerIt().parse(text)
    #check if the text no have an error
    if (len(corrected_text['corrections'])==0):
        return "No contiene errores"
    return corrected_text['result']