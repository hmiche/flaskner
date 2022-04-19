import layoutparser as lp 

import pandas as pd
import numpy as np
import cv2
import layoutparser as lp 
from pdf2image import convert_from_path
import functions
from ocr import ocrtext
def extractpic(name,Model):

    pdf_path = 'static/uploads/'+name
    # convert first page
    image = convert_from_path(pdf_path, dpi=200, thread_count=1)[0]
    image = image.convert('RGB') 
    document_image_first = np.array(image)
    document_image_first = cv2.cvtColor(document_image_first, cv2.COLOR_BGR2RGB)
    cv2.imwrite("static/uploads/page1.jpg",document_image_first)
    return ocrtext(Model)




