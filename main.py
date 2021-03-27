import cv2
import face_recognition
import sys


def take_picture():
    print("Scanning Face...")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite('Picture.jpg', frame)
    cv2.destroyAllWindows()
    cap.release()
    print("Face scan complete")


def analyze_user():
    print("Analyzing Face...")
    #Моя фотка\эталон
    baseimg = face_recognition.load_image_file("Me.jpg")
    baseimg = cv2.cvtColor(baseimg, cv2.COLOR_BGR2RGB)

    myface = face_recognition.face_locations(baseimg)[0]
    encodemyface = face_recognition.face_encodings(baseimg)[0]
    cv2.rectangle(baseimg, (myface[3], myface[0]), (myface[1], myface[2]), (255, 0, 255), 2)

    #cv2.imshow("Test", baseimg)
    #cv2.waitKey(0)

    #с чем будем сравнивать
    sampleimg = face_recognition.load_image_file("Picture.jpg")
    sampleimg = cv2.cvtColor(sampleimg, cv2.COLOR_BGR2RGB)

    samplefacetest = face_recognition.face_locations(sampleimg)[0]
    try:
        encodesamplefacetest = face_recognition.face_encodings(sampleimg)[0]
    except IndexError as e:
        print("Index Error. Authentication failed")
        sys.exit()
    #cv2.rectangle(sampleimg, (samplefacetest[3], samplefacetest[0]), (samplefacetest[1], samplefacetest[2]),
    # (255, 0 ,255), 2)

    #cv2.imshow("TEST", sampleimg)
    #cv2.waitKey(0)

    result = face_recognition.compare_faces([encodemyface], encodesamplefacetest)
    resultstring = str(result)
    #print(resultString)

    if resultstring == "[True]":
        print("User Authenticated. Welcome back")
    else:
        print("Authentication Failed")

#take_picture()
analyze_user()
