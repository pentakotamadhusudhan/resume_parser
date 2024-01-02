from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
import time 
from rest_framework.response import Response 

from .face_rec import image_declaration

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') 
        

# Global variable to track the start time of the webcam stream
start_time = None
message = ''
@gzip.gzip_page
def Home2(request):
    global start_time
    
    try:
        cap = cam = VideoCamera()
        
        start_time = time.time()  # Record the start time
        return StreamingHttpResponse(gen(camera=cam,camee=None), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        # print(f"Error in Home view: {e}")
        message = "Call is terminated"
        
        # return render(request, "home.htm  l",)
        

    return render(request, 'app2.html',context={'foo':f"{message} "})

# to capture video class
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        cap = self.video
        if not self.video.isOpened():
            raise Exception("Failed to initialize the camera.")
        
        self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set your desired frame width
        self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set your desired frame height

       
        (self.grabbed, self.frame) = self.video.read()
        self.thread_stop = False
        threading.Thread(target=self.update, args=()).start()
        
        while 1:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
            print(len(faces))

            img_del = image_declaration(frame)
            print(img_del)
            if len(faces)!=1 or img_del['Match']==False :
                self.thread_stop=True
                break
        # threading.Thread(target=self.update, args=()).start()
        gen(camera=None,camee=len(faces ))
        print('--------------------------------')
        

        

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while not self.thread_stop:
            (self.grabbed, self.frame) = self.video.read()

    def stop_update_thread(self):
        self.thread_stop = True

cam = False

def camStatue(request):
    return render(request,'end.html')

def gen(camera=None,camee=None,message=message):
    if camee==0:
        # threading.Thread(target=VideoCamera().update, args=(lambda : False))
        message = "Interview as terminated because of Face is not detected"
        print(message)
    elif camee>1:
        message = "Interview as terminated because of Faces are detected"
        print(message)
        
    else: 
        if camera is not None:
            global start_time

            while time.time() - start_time < 1 * 60:                  # Run for 30 minutes
                frame = camera.get_frame()
                yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            print('gen function')
            # Stop the webcam stream after the specified duration
            camera.stop_update_thread()
            print("Webcam stream stopped.")
        else:
            VideoCamera().stop_update_thread()
            

from rest_framework.views import APIView
from rest_framework import status
class madhu(APIView):

    def post(self,request):
        try:
            x = Home2(request=request)
            print(x)
            ob = VideoCamera()
            ob.stop_update_thread()
            # return redirect('http://localhost:8000/interviewend',foo='completed')
            return Response({
                'status':status.HTTP_200_OK,
                'message':'Assement is completed successfully',
                'hash': False,
            })

        except: 
            print('excpetr')
            ob.stop_update_thread()
            # return redirect('http://localhost:8000/interviewend',foo='End')
            return Response({
                'status':status.HTTP_302_FOUND,
                'message':'Assement is Terminated',
                'hash':False,
            })

            

def interview(request):
        try:
            Home2(request=request)
            print('try')
            ob = VideoCamera()
            ob.stop_update_thread()
            return redirect('http://localhost:8000/interviewend',foo='completed')

        except: 
            print('excpetr')
            ob.stop_update_thread()
            return redirect('http://localhost:8000/interviewend',foo='End')
            
