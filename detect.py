from imageai.Detection.Custom import CustomObjectDetection


def detect(filepath):
    detector = CustomObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath("set/models/detection_model-ex-013--loss-0016.700.h5")
    detector.setJsonPath("set/json/detection_config.json")
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=filepath, output_image_path="piwo2.png")
    for detection in detections:
        print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])
    if len(detections) > 0:
        return detections[0]["name"]
    else:
        return "piwo"


