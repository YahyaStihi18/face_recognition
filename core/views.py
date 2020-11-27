from django.shortcuts import render,HttpResponse,redirect
from .models import *
import face_recognition
import cv2
import numpy as np
import winsound
from django.db.models import Q



last_face = 'no_face'

def index(request):
    last_face = LastFace.objects.last()
    context ={
        'last_face':last_face
    }
    return render(request, 'core/index.html',context)

def ajax(request):
    last_face = LastFace.objects.last()
    context ={
        'last_face':last_face
    }
    return render(request, 'core/ajax.html',context)

def scan(request):

    global last_face
    video_capture = cv2.VideoCapture(0)

    image_of_yahya = face_recognition.load_image_file('media/yahya_stihi.jpg')
    yahya_face_encoding = face_recognition.face_encodings(image_of_yahya)[0]


    image_of_ahmed = face_recognition.load_image_file('media/ahmed_bouchfirat.jpg')
    ahmed_face_encoding = face_recognition.face_encodings(image_of_ahmed)[0]

    known_face_encodings = [

        yahya_face_encoding,
        ahmed_face_encoding,

    ]
    known_face_names = [

        "yahya_stihi",
        "ahmed_bouchfirat"
    ]



    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        ret, frame = video_capture.read()

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding)
                name = "Unknown"


                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                    if  last_face != name:
                        print(f'new face request sent for: {name}')
                        last_face = LastFace(last_face=name)
                        last_face.save()
                        last_face = name
                    else:
                        pass

                face_names.append(name)

        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 35),
                        (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return HttpResponse('scaner closed',last_face)


def profile(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'core/profile.html', context)


def details(request):
    try:
        last_face = LastFace.objects.last()
        profile = Profile.objects.get(Q(image__icontains=last_face))
        print(profile)
    except:
        last_face = None
        profile = None
    
    context = {
        'profile': profile,
        'last_face':last_face
    }
    return render(request, 'core/details.html', context)
