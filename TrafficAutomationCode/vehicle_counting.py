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
        # Update total count
            self.vehicles_folder_count += self.vehicle_count

            for box in self.vehicle_boxes:
                x, y, w, h = box

                cv2.rectangle(self.img, (x, y), (x + w, y + h), (25, 0, 180), 3)

                cv2.putText(self.img, "Vehicles: " + str(self.vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

        #cv2.imshow("Cars", self.img)
        #cv2.waitKey(1)

        # print("Total current count", self.vehicles_folder_count)
    def lcount(self):
        return(self.count)