# importing librarys
import cv2
from django.shortcuts import redirect
# from .cam2 import VideoCamera
import numpy as npy
import face_recognition as face_rec
import face_recognition

def resize(img, size) :
    width = int(img.shape[1]*size)
    height = int(img.shape[0] * size)
    dimension = (width, height)
    return cv2.resize(img, dimension, interpolation= cv2.INTER_AREA)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') 
        
# img declaration

def image_declaration(image_1):
    try:
        image_2 = face_rec.load_image_file(r"C:\Users\User\Downloads\passport copy.jpg")
        gray = cv2.cvtColor(image_2, cv2.COLOR_BGR2RGB)
                
        sizedbox = resize(image_2, 0.50)
        faceLocation_uday = face_rec.face_locations(image_2)[0]
        # print(faceLocation_uday)
        encode_image_2 = face_rec.face_encodings(image_2)[0]
        encode_image_1 = face_rec.face_encodings(image_1)[0]
        n = cv2.rectangle(gray, (faceLocation_uday[3], faceLocation_uday[0]), (faceLocation_uday[1], faceLocation_uday[2]), (255, 0, 255), 3)
        
        is_same = face_recognition.compare_faces([encode_image_1], encode_image_2)[0]
        
        if is_same:
            distance = face_recognition.face_distance([encode_image_1], encode_image_2)
            distance = round(distance[0] * 100)
            accuracy = 100 - round(distance)
        else:
            print("The images are not same")
        return {'Accuracy': accuracy,'Match':True}
    except Exception as e:
        print('face not found')
        return {'Accuracy':0,'Match':False}
        # return redirect('http://127.0.0.1:8000/interviewend',foo='End')

# def timestamp():
