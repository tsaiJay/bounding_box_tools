# tool_for_labelImg
Here are some helpful tools to enhance your experience while using labelIMG for labeling in YOLO format.

> NOTE: The tool is designed for fixed camera scenarios, where the camera remains stationary and does not move.

## Manual

1. label_clean_specific_center.py

Remove bounding boxes based on their center position. When `SET_MODE=False`, any bounding box with its center falling within the specified range (marked by a red rectangle) will be deleted.

2. label_add_specific_bboxes.py
You must prepare a `.txt` file containing labels in YOLO format. When `SET_MODE=False`, These labels will then be added to all label files in the folder.

3. label_class_check.py
Check for any undefined classes that appear in the label.txt files.

## thank for labelImg

## ToDo
- [ ] use prcedure
- [ ] simple example
