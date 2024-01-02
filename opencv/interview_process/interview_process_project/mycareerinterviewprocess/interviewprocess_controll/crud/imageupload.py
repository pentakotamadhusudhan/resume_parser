from rest_framework.generics import GenericAPIView
from interviewprocess_controll.serializer import *
from rest_framework.response import Response

class ImageUploader(GenericAPIView):
    serializer_class = ImageSeralizer

    def post(self,request):
        img =request.data.get('image')
        print(img)
        ser = ImageSeralizer(data=request.data)
        ser.is_valid()
        ser.save()
        return Response(
            {'status':200,
             'image':ser.data
             }
        )