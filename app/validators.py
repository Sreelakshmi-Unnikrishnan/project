from django.core.exceptions import ValidationError

# def validate_image(value):
#     filesize= value.size
    
#     if filesize > 1048576:
#         raise ValidationError("The maximum file size that can be uploaded is 1MB")
#     else:
#         return value

# def validate_video(value):
#     filesize= value.size
    
#     if filesize > 10485760:
#         raise ValidationError("The maximum file size that can be uploaded is 10MB")
#     else:
#         return value
def validate_image(image):
        # 12MB
        MAX_FILE_SIZE = 1048576
        print(image.name)
        if image.size > MAX_FILE_SIZE:
            print(image.size)
            raise ValidationError("File size too big!")

def validate_video(video):
        # 12MB
        MAX_FILE_SIZE = 10485760
        print(video.name)
        if video.size > MAX_FILE_SIZE:
            print(video.size)
            raise ValidationError("File size too big!")
