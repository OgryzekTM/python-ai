from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="set")
metrics = trainer.evaluateModel(model_path="set/models", json_path="set/json/detection_config.json",
                                iou_threshold=0.5, object_threshold=0.3, nms_threshold=0.5)
print(metrics)