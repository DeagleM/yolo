from roboflow import Roboflow
rf = Roboflow(api_key="j9dTjF7QGW2BMLtpt84l")
project = rf.workspace("augmented-startups").project("vehicle-registration-plates-trudk")
dataset = project.version(2).download("yolov7")

#   C:/Users/DeagleM/AppData/Local/Microsoft/WindowsApps/python3.11.exe train.py --batch 16 --epochs 55 --data Vehicle-Registration-Plates-2/data.yaml --weights 'yolov7_training.pt' --device 'cpu'