import cv2


images = ["1.png", "2.png", "4.png"]
for name in images:
    img = cv2.imread('./alpha_images/' + name, cv2.IMREAD_UNCHANGED)

    width = 100
    height = 100
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(f"./images_100/{name}", resized)

    width = 32
    height = 32
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(f"./images_32/{name}", resized)

    width = 16
    height = 16
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(f"./images_16/{name}", resized)
