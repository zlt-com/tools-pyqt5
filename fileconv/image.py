import cv2


def image_h_concat(file_name, files):
    images = []
    for f in files:
        img = cv2.imread(f)
        images.append(img)
    cv2.imwrite(file_name, cv2.hconcat(images))


def image_v_concat(file_name, files):
    images = []
    for f in files:
        img = cv2.imread(f)
        images.append(img)
    cv2.imwrite(file_name, cv2.vconcat(images))
