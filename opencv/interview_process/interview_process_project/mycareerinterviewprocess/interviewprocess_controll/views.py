# from django.http.response import HttpResponse
# from django.shortcuts import render
# import cv2
# from .face_rec import image_declaration

# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') 
        

# # Create your views here.
# def CameraAccess(request):
#     if request.method =='POST':
#         cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#         cap.set(cv2.CAP_PROP_FRAME_WIDTH,600)
#         cap.set(cv2.CAP_PROP_FRAME_HEIGHT,400)
#         fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#         writer = cv2.VideoWriter("recorder.mp4",fourcc,15.0,(600,400))
#         recording = False
#         while 1:
#             ret, frame = cap.read()
#             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#             faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

#             print(len(faces))
#             for (x,y,w,h) in faces:  
#                 cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2) 
#                 roi_gray = gray[y:y+h, x:x+w] 
#                 roi_color = frame[y:y+h, x:x+w]
#                 eyes = eye_cascade.detectMultiScale(roi_gray) 

#                 #To draw a rectangle in eyes 
#                 for (ex,ey,ew,eh) in eyes: 
#                     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
#                 key = cv2.waitKey(1)
#                 if ret:
#                     cv2.imshow("video",frame)
#                     if recording:
#                         writer.write(frame)
#             print(ord('q'),0xFF)
#             if  cv2.waitKey(1) & 0xFF == 27:
#                 print("madhu")
#                 break
#             elif recording:
#                 recording = not recording
#                 print('recording:{recording}')
#         cap.release() 
#         writer.release()
#         # De-allocate any associated memory usage 
#         cv2.destroyAllWindows()
#         return HttpResponse("Call has ended")
#     return render(request,"Camera.html")


# # [x,y,width,height]


# from django.http import HttpResponse
# from django.shortcuts import render
# from django.views.decorators import gzip
# from django.http import StreamingHttpResponse
# import cv2
# import threading
# import time  # Import the time module for managing the duration

# # Global variable to track the start time of the webcam stream
# start_time = None

# @gzip.gzip_page
# def Home(request):
#     global start_time

#     try:
#         cam = VideoCamera()
#         image_declaration()
#         start_time = time.time()  # Record the start time
#         return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#     except Exception as e:
#         print(f"Error in Home view: {e}")
#         pass

#     return render(request, 'app1.html')

# # to capture video class
# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         frame,rect = self.video
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
#         # print(len(faces))
#         if not self.video.isOpened():
#             raise Exception("Failed to initialize the camera.")
        
#         self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set your desired frame width
#         self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set your desired frame height
        
#         (self.grabbed, self.frame) = self.video.read()
#         self.thread_stop = False
#         threading.Thread(target=self.update, args=()).start()

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()

#     def update(self):
#         while not self.thread_stop:
#             (self.grabbed, self.frame) = self.video.read()

#     def stop_update_thread(self):
#         self.thread_stop = True

# cam = False

# def camStatue(request):
#     return render()

# def gen(camera):
#     global start_time

#     while time.time() - start_time < 1 * 60:                  # Run for 30 minutes
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#         # print(start_time)
#         if cam:
#             camera.stop_update_thread()

#     # Stop the webcam stream after the specified duration
#     camera.stop_update_thread()
#     print("Webcam stream stopped.")



    