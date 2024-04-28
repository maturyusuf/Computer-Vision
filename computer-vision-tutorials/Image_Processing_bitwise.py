import cv2

img_1 = cv2.imread("images/bit_1.png")
img_2 = cv2.imread("images/bit_2.png")

and_op = cv2.bitwise_and(img_1, img_2, mask=None)
or_op = cv2.bitwise_or(img_1, img_2, mask=None)
xor_op = cv2.bitwise_xor(img_1, img_2, mask=None)
not_op = cv2.bitwise_not(img_2, mask=None)

cv2.imshow("AND",and_op)
cv2.imshow("OR",or_op)
cv2.imshow("XOR", xor_op)
cv2.imshow("NOT",not_op)


if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()