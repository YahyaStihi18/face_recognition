import face_recognition




image_of_yahya = face_recognition.load_image_file('../media/yahya_stihi.jpg')
yahya_face_encoding = face_recognition.face_encodings(image_of_yahya)[0]

image_of_ahmed = face_recognition.load_image_file('../media/ahmed_bouchfirat.jpg')
ahmed_face_encoding = face_recognition.face_encodings(image_of_ahmed)[0]

# Create arrays of known face encodings and their names

known_face_encodings = [

    yahya_face_encoding,
    ahmed_face_encoding,

]
known_face_names = [

    "yahya stihi",
    "ahmed bouchfirat",
]