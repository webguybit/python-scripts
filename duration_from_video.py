
"""
Source link:
https://stackoverflow.com/questions/3844430/how-to-get-the-duration-of-a-video-in-python
"""
def with_opencv(filename):
    import cv2
    video = cv2.VideoCapture(filename)

    duration = video.get(cv2.CAP_PROP_POS_MSEC)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

    return duration, frame_count
# Usage: print(with_opencv('my_video.webm'))