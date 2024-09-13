# bounding_box_tools

Here are some helpful tools to enhance your experience while managing label files in YOLO format.

When certain objects remain stationary and appear consistently in the same position, it becomes necessary to repeatedly crop the bounding box. Here's a simple code to streamline this process.

> NOTE: The tool is designed for fixed camera scenarios, where the camera remains stationary and does not move.

## Manual

1. tool1_clean_specific_center.py

Remove bounding boxes based on their center position. When `SET_MODE=True`, the configuration result will be displayed in the window without modifying the document. When `SET_MODE=False`, any bounding box with its center falling within the specified range (marked by a red rectangle) will be deleted.

> note: green grid for coordinate reference. bboxes center in the red boxes will be removed.

![image](https://github.com/tsaiJay/bounding_box_tools/blob/main/example_files/img_filter_area.png)

2. tool2_add_specific_bboxes.py
You must prepare a `.txt` file containing labels in YOLO format. When `SET_MODE=True`, the configuration result will be displayed in the window without modifying the document. When `SET_MODE=False`, these labels will then be added to all label files in the folder.

![image](https://github.com/tsaiJay/bounding_box_tools/blob/main/example_files/img_fix_bbox.png)

4. tool3_class_check.py
Check for any undefined classes that appear in the label.txt files.

## thank for labelImg

## ToDo
- [ ] use prcedure
- [ ] simple example
