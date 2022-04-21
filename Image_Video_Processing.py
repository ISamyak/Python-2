from email.mime import image
import cv2
import glob

images=glob.glob("sample_images/*.jpg")

for image in images:
    img=cv2.imread(image,1)
    resized_image=cv2.resize(img,(int(img.shape[0]/2),int(img.shape[1]/2)))
    cv2.imshow("Galaxy",resized_image)
    #cv2.imwrite("Galaxy_resized.jpg",resized_image)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
