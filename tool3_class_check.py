import os
import cv2


def ckeck_class_valid(label_paths: list, valid_class_idx: list):
    def get_label_file_to_list(path):
        with open(path, 'r') as f:
            lines = f.readlines()
            label = []
            for ln in lines:
                cla = ln.split()[0]
                x, y, w, h = float(ln.split()[1]), float(ln.split()[2]), float(ln.split()[3]), float(ln.split()[4])
                label.append([cla, x, y, w, h])
            return label

    for path in label_paths:
        print('current ===>', path)
        labels = get_label_file_to_list(path)

        for la in labels:
            if int(la[0]) in valid_class_idx:
                pass
            else:
                print('err')
                exit()
    print('all pass')



if __name__ == "__main__":
    TARGET_DIR = "./label"
    valid_class_idx = [0]

    label_paths = [os.path.join(TARGET_DIR, p) for p in os.listdir(TARGET_DIR) if p.endswith(".txt") and 'class' not in p]
    # print(label_paths)
    ckeck_class_valid(label_paths, valid_class_idx)


