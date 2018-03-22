import cv2
from pyzbar.pyzbar import decode, ZBarSymbol


def draw_text(img, text, org, fontFace, fontScale, color, thickness):
    """Write white text with colored background"""
    textSize = cv2.getTextSize(text, fontFace, fontScale, thickness)
    cv2.rectangle(img, (org[0] - 1, org[1] - textSize[0][1] - 2), (org[0] + textSize[0][0], org[1]), color, cv2.FILLED);
    cv2.putText(img, text, (org[0], org[1] - 1), fontFace, fontScale, (255, 255, 255), thickness)


def qrcode_decoder():
    cv2.namedWindow('QR Code Decoder')
    cap = cv2.VideoCapture(0)

    # capture frames from the camera
    while True:
        ret, img = cap.read()
        if not ret:
            continue
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY, dstCn=0)
        
        # look for just QR Codes
        decoded = decode(gray, symbols=[ZBarSymbol.QRCODE])
        for symbol in decoded:
            print(symbol)
            text = symbol.data.decode()
            cv2.rectangle(img, (symbol.rect.left, symbol.rect.top), (symbol.rect.left + symbol.rect.width, symbol.rect.top + symbol.rect.height), (0, 255, 0), 2)
            draw_text(img, text, (symbol.rect.left, symbol.rect.top), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('QR Code Decoder', img)

        # wait for the 'q' key
        keypress = cv2.waitKey(1) & 0xFF
        if keypress == ord('q'):
            break

    # when everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    qrcode_decoder()
