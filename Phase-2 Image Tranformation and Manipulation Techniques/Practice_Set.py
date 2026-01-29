# **********************************************************
# *** Engr. Muhammad Javed ***
# **********************************************************


# Simple OpenCV Drawing Tool:
# - Draw Line, Rectangle, Circle, or Add Text on an Image
# - User inputs coordinates, color (BGR), radius (for circle), or text
# - Option to save the edited image

import cv2

def save_image(image, path):
    cv2.imwrite(path, image)
    print(f"Image saved to {path}")




image = input("Enter image path: ")
print("1. Draw line"
      "\n2. Draw Rectangle"
      "\n3. Draw Circle"
      "\n4. Add Text")

choice = int(input("Enter your choice : " ))

if image is None:
    print("Image not found, please check the path.")

else:
    image = cv2.imread(image)

    if choice == 1:
        # Point 1
        print("Enter first point (x y):")
        plt1 = tuple(map(int, input().split()))

        # Point 2
        print("Enter second point (x y):")
        plt2 = tuple(map(int, input().split()))

        # Color input (B G R)
        print("Enter color (B G R):")
        color = tuple(map(int, input().split()))

        thickness = 4

        cv2.line(image, plt1, plt2, color, thickness)

        cv2.imshow("Line on Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        boolean = input("Do you want to save the image? (y/n): ")
        if boolean.lower() == 'y':
            save_image = input("Enter path to save the image: ")
            save_image(image, save_image)

        else:
            print("Image not saved.")



    elif choice == 2:
         # Point 1
        print("Enter first point (x y):")
        plt1 = tuple(map(int, input().split()))

        # Point 2
        print("Enter second point (x y):")
        plt2 = tuple(map(int, input().split()))

        # Color input (B G R)
        print("Enter color (B G R):")
        color = tuple(map(int, input().split()))

        thickness = 4

        cv2.rectangle(image , plt1 , plt2 , color , thickness)

        cv2.imshow("Draw rectangle on Image", image)

    elif choice == 3:
        # Center input (x y)
        print("Enter center of circle (x y):")
        center = tuple(map(int, input().split()))

        # Radius input
        radius = int(input("Enter radius: "))

        # Color input (B G R)
        print("Enter color (B G R):")
        color = tuple(map(int, input().split()))    

        thickness = -1

        cv2.circle(image , center , radius , color , thickness  )

        cv2.imshow("Draw Circle on Image", image)
        boolean = input("Do you want to save the image? (y/n): ")
        if boolean.lower() == 'y':
            save_image = input("Enter path to save the image: ")
            save_image(image, save_image)

        else:
            print("Image not saved.")

    elif choice == 4:
        # Point 1
        print("Enter first point (x y):")
        plt1 = tuple(map(int, input().split()))
        # Color input (B G R)
        print("Enter color (B G R):")
        color = tuple(map(int, input().split())) 
        text = input("Enter the text to add: ")
        thickness = 4

        cv2.putText(image , text , plt1 , cv2.FONT_HERSHEY_SIMPLEX , 0.7 , color , thickness)

        cv2.imshow("Text on Image", image)
        boolean = input("Do you want to save the image? (y/n): ")
        if boolean.lower() == 'y':
            image_path = input("Enter path to save the image: ")
            save_image(image, image_path)

        else:
            print("Image not saved.")

    else:
        print("Invalid choice")

    cv2.waitKey(0)
    cv2.destroyAllWindows()



