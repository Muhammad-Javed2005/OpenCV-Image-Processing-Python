# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************

import cv2 
import os 
from datetime import datetime


# ==============================
# Function 1: Display Video File
# ==============================


def play_vedio_from_path ():

    path = input("Enter vedio file path :")

    if not os.path.isfile(path):
        print("File not found , Please check the path.")
        return
    
    cap = cv2.VideoCapture(path)

    while True:
        ret , frame = cap.read()
        if not ret :
            print("Reached end of vedio or failed to grab frame.")
            break

        cv2.imshow("Vedio Playback" , frame)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            print("Quitting vedio playback...")
            break 

    cap.release()
    cv2.destroyAllWindows()


# ==============================
# Function 2: Live Webcam Feed
# ==============================


def show_webcam():
    cap = cv2.VedioCapture(0 , cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Cannot access webcam.")
        return 
    
    while True:
        ret , frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow("Webcam Feed" , frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Quitting Webcam Feed...")
            break 

    cap.release()
    cv2.destroyAllWindows()


# ==============================
# Function 3: Record Webcam Video
# ==============================

def record_webcam_video():
    cap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Cannot access webcam.")
        return 

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f'webcam_recording_{timestamp}.avi'
    out = cv2.VideoWriter(output_filename, fourcc, 20.0, (frame_width, frame_height))

    print(f"Recording started. Press 'q' to stop. Video will be saved as {output_filename}")

    while True:
        ret , frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break

        out.write(frame)
        cv2.imshow("Recording Webcam Video" , frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Stopping recording...")
            break 

    cap.release()
    out.release()
    cv2.destroyAllWindows()



# ==============================
# Main Menu
# ==============================


def Main_menu():
    while True:
        print("\n=== Video and Webcam Operations Menu ===")
        print("1. Play Video from File")
        print("2. Show Live Webcam Feed")
        print("3. Record Webcam Video")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            play_vedio_from_path()
        elif choice == '2':
            show_webcam()
        elif choice == '3':
            record_webcam_video()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# ==============================
# Program Start
# ==============================
Main_menu()

