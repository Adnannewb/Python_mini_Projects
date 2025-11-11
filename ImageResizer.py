import cv2
# print(cv2.__version__)
# image=cv2.imread("sunrong.jpeg",cv2.IMREAD_UNCHANGED)
# cv2.imshow("tittle",image)
# cv2.waitKey(0)



# Load the image
image = cv2.imread("sunrong.jpeg")

# Resize the image (e.g., 300x300 pixels)
resized_image = cv2.resize(image, (300, 300))

# Save the resized image
cv2.imwrite("resized_output.jpg", resized_image)

print("Image resized successfully!")
cv2.imshow("resized",resized_image)
cv2.waitKey(0)
