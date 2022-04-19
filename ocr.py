import layoutparser as lp 
import cv2
import pytesseract
import functions
from predict import pridect
def ocrtext(Model):
    Result=[]
    img = cv2.imread("page1.jpg")
    img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    img = cv2.bilateralFilter(img,9,75,75)
    cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    ocr_agent = lp.TesseractAgent(languages='fra')
    res = ocr_agent.detect(img, return_response=True )

    text=res['text']
    text = res['text'].split("\n")  
    
    return pridect(Model,text)


