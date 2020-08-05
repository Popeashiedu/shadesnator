from django.shortcuts import render, redirect
import cv2, time
# import face_recognition

# # Create your views here.
# video = cv2.VideoCapture(0)
# # check, frame = video.read()
#
# video.release()


def index(request):
    return render(request, 'index.html')


def detectWithWebcam(request):
    video = cv2.VideoCapture(0)
    a = 0
    while True:
        a = a+1

        check, frame = video.read()
        color = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.imshow("Capturing", color)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    return redirect('/')


