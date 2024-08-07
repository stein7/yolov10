from ultralytics import YOLOv10
model = YOLOv10('./weights/yolov10n.pt')

# model.train(data='../datasets/football-players-detection-10/data.yaml', epochs=25, batch=32)

# model.val(data='../datasets/football-players-detection-10/data.yaml')
import sys
sys.argv = ["path/to/your/script/yolo", "predict"]
# model.predict('../datasets/football-players-detection-10/valid/images/a9f16c_8_10_png.rf.9835e230bebd2303d07d0147fe441dfa.jpg')

model.predict("/users2/dataset/replica/vmap/room_0/imap/00/rgb/")


def tojson_DH(self, save_dir, count):
        
    obj_dict = {}
    for idx in range(self.boxes.shape[0]):
        obj_dict[str(idx+10000)] = {
            "name": self.names[int(self.boxes.cls[idx])],
            "x": round(self.boxes.xyxy[idx][0].item()),
            "y": round(self.boxes.xyxy[idx][1].item()),
            "w": round(self.boxes.xywh[idx][2].item()),
            "h": round(self.boxes.xywh[idx][3].item()),
            "attributes": [],
            "relations": []
        }
    image_dict = {
        f"image {count}": {
            "width": self.boxes.orig_shape[1],
            "height": self.boxes.orig_shape[0],
            "objects": obj_dict
        }
    }

    import json
    import os
    save_path = os.path.join(save_dir, f'image_dict{count}.json')

    total_dict = {}
    for idx in range(save_path number):
        with open(save_path idx, 'r') as f:
            total_dict = {
                f
            }
        
    with open(save_path, 'w') as f:
        json.dump(total_dict, f, indent=4)

    save_path = "/home/sslunder0/project/Object-Detector/yolov10/runs/detect/predict24"
    total_dict = {}
    for filename in os.listdir(save_path):
        if filename.endswith(".json"):
            file_path = os.path.join(save_path, filename)
            with open(file_path, 'r') as f:
                data = json.load(f)
                total_dict.update(data)

    new_save_path = os.path.join(save_path, "combined.json")
    with open(new_save_path, 'w') as f:
        json.dump(total_dict, f, indent=4)
