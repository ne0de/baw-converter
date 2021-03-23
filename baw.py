import cv2

image = cv2.imread('duck.jpg', -1)
shape = image.shape # height, width, channels -> 3 {red, green, blue}
height, width, channels = shape[0], shape[1], shape[2]

for row in range(height):
    for column in range(width):
        red, green, blue = image[row][column][0], image[row][column][1], image[row][column][2]
        gray = int(red) + int(green) + int(blue) / 3

        for i in range(channels): 
            image[row][column][i] = gray

cv2.imshow('Black and white', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
