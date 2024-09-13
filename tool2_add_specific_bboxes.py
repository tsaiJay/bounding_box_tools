import os
import cv2


def show_fix_box(image, label_path, wh):
    with open(label_path, 'r') as f:
        lines = f.readlines()
        label = []
        for ln in lines:
            cla = ln.split()[0]
            x, y, w, h = float(ln.split()[1]), float(ln.split()[2]), float(ln.split()[3]), float(ln.split()[4])
            label.append([cla, x, y, w, h])
    for b in label:
        x, y, w, h = b[1] * wh[0], b[2] * wh[1], b[3] * wh[0], b[4] * wh[1]
        x0 = int(x - w/2)
        y0 = int(y - h/2)
        x1 = int(x + w/2)
        y1 = int(y + h/2)
        cv2.rectangle(image, (x0, y0), (x1, y1), (0, 255, 0), 1)


def add_bbox_from_file(label_paths: list, fix_label: str, save_path):
    def get_label_file_to_list(path):
        with open(path, 'r') as f:
            lines = f.readlines()
            return lines

    fix = get_label_file_to_list(fix_label)

    for path in label_paths:
        print('current ===>', path)
        temp = get_label_file_to_list(path)

        with open(path, 'a') as f:
            for ln in fix:
                if ln in temp:
                    print('already added, pass!')
                    break
                f.write(ln)


if __name__ == "__main__":
    SET_MODE = True
    ROOT = "./fix_camera_images"
    IMG_SIZE = (1280, 720)

    ''' box path '''
    FIX_BOX = './example_files/fix_box_n.txt'
    ''' end '''

    img_paths = [os.path.join(ROOT, p) for p in os.listdir(ROOT) if p.endswith(".jpg")]
    label_paths = [os.path.join(ROOT, p) for p in os.listdir(ROOT) if p.endswith(".txt") and 'classe' not in p]

    if SET_MODE:
        img = cv2.imread(img_paths[0])
        print(f'image size (w, h): ({img.shape[1]}, {img.shape[0]})')

        show_fix_box(img, FIX_BOX, IMG_SIZE)
        cv2.imshow('window', img)
        cv2.waitKey(0)

    else:
        add_bbox_from_file(label_paths, FIX_BOX, ROOT)


