import os
import cv2


def show_grid(image):
    rows, cols = image.shape[:2]
    grid_size = 100

    for i in range(0, rows, grid_size):
        cv2.line(image, (0, i), (cols, i), (0, 255, 0), 1)  # 水平線
    for j in range(0, cols, grid_size):
        cv2.line(image, (j, 0), (j, rows), (0, 255, 0), 1)  # 垂直線

    for i in range(0, rows, grid_size):
        for j in range(0, cols, grid_size):
            cv2.putText(image, f'({j},{i})', (j, i-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)


def show_abandand_area(image, bboxs):
    for idx, b in enumerate(bboxs):
        cv2.rectangle(image, (b[0], b[1]), (b[2], b[3]), (0, 0, 255), 2)
        cv2.putText(image, f'{idx}', (b[0], b[1]-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1, cv2.LINE_AA)


def clean_procedure(label_paths: list, filter_area: list, wh: tuple, save_path):
    def get_label_file_to_list(path):
        with open(path, 'r') as f:
            lines = f.readlines()
            label = []
            for ln in lines:
                cla = ln.split()[0]
                x, y, w, h = float(ln.split()[1]), float(ln.split()[2]), float(ln.split()[3]), float(ln.split()[4])
                label.append([cla, x, y, w, h])
            return label
    def filter_label(labels):
        clean_result = []
        for label in labels:
            x, y = label[1] * wh[0], label[2] * wh[1]
            for filt in filter_area:
                if filt[0] < x < filt[2] and filt[1] < y < filt[3]:
                    break
            else:
                clean_result.append(label)
        return clean_result

    for path in label_paths:
        print('current ===>', path)
        labels = get_label_file_to_list(path)
        clean_result = filter_label(labels)

        with open(path, 'w') as f:
            for ln in clean_result:
                f.write(f"{ln[0]} {ln[1]} {ln[2]} {ln[3]} {ln[4]}\n")


if __name__ == "__main__":
    SET_MODE = True
    ROOT = "./fix_camera_images"
    IMG_SIZE = (1280, 720)

    ''' define abandanded areas, list of [x0, y0, x1, y1]'''
    AREAS_LIST = [
        (600, 30, 650, 60),
        (650, 20, 680, 40),
        (870, 30, 910, 70),
    ]
    ''' end define '''

    img_paths = [os.path.join(ROOT, p) for p in os.listdir(ROOT) if p.endswith(".jpg")]
    label_paths = [os.path.join(ROOT, p) for p in os.listdir(ROOT) if p.endswith(".txt") and 'classe' not in p]

    if SET_MODE:
        img = cv2.imread(img_paths[0])
        print(f'image size (w, h): ({img.shape[1]}, {img.shape[0]})')

        show_grid(img)
        show_abandand_area(img, AREAS_LIST)
        cv2.imshow('window', img)
        cv2.waitKey(0)

    else:
        clean_procedure(label_paths, AREAS_LIST, IMG_SIZE, ROOT)


