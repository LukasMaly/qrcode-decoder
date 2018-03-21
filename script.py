import cv2
from pyzbar.pyzbar import decode, ZBarSymbol

cv2.namedWindow('QR Code Decoder')
cap = cv2.VideoCapture(0)

# capture frames from the camera
while True:
    ret, output = cap.read()
    if not ret:
        continue
    gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY, dstCn=0)
    
    # look for just QR Codes
    decoded = decode(gray, symbols=[ZBarSymbol.QRCODE])
    for symbol in decoded:
        print(symbol)
	
    cv2.imshow('QR Code Decoder', output)

    # wait for the 'q' key
    keypress = cv2.waitKey(1) & 0xFF
    if keypress == ord('q'):
    	break

# when everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
