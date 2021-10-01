import cv2
import glob
from vehicle_detector import VehicleDetector

# Load Veichle Detector
class Vehicle():
    def __init__(self):
        self.vd = VehicleDetector()
        self.count=[]
    # Load images from a folder
        self.images_folder = glob.glob("images/*.jpeg")

        self.vehicles_folder_count = 0

    # Loop through all the images
        for img_path in self.images_folder:
            print("Img path", img_path)
            self.img = cv2.imread(img_path)

            self.vehicle_boxes = self.vd.detect_vehicles(self.img)
            self.vehicle_count = len(self.vehicle_boxes)
            self.count.append(self.vehicle_count)
       
    def lcount(self):
        return(self.count)
