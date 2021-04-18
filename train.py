from imageai.Detection.Custom import DetectionModelTrainer

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="set")
trainer.setTrainConfig(object_names_array=["piwo"], batch_size=4, num_experiments=15,
                       train_from_pretrained_model="pretrained-yolov3.h5")
trainer.trainModel()
