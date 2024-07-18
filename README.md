
# Final Year Project By Rohit Prajapat (2020BITE052)

## 0. Contents
1. Introduce
2. Motivation
   - Why do we detect falling down?
3. Solution
   - Technologies and Libraries Used
       - Mediapipe
       - OpenCV
       - YOLOv5
       - YOLOv8
       - Threading
   - Establish hypotheses and explain basic logic
       - How do you measure falls?
   - Heinrich's law
       - If you almost fall more than 300 times, it becomes a major disaster in the future.
   - Perspective
       - A method for measuring the fall of distant and near objects.
       - How to Calculate Falls by Region.
4. Training YOLO Models

## 1. Introduce
1. You can check the distance between foot C.G and body C.G.
2. It's the body center of gravity.
3. It's the foot center of gravity.
4. You can check the count of how many times he fell.
5. If the distance is over 90 pixels (tall * 0.75), it displays he is falling.
6. Body C.G and foot C.G are measured using only the X-axis, and this distance difference is used as the basis of judgment.
7. It indicates if he woke up (this only displays after falling).
8. A count of 1 goes up in the area where you fell (the count is determined by which area your feet are in).

## 2. Motivation

### Why do we detect falling down?

### According to WHO
- Falls are the second leading cause of unintentional injury deaths worldwide.
- Each year an estimated 684,000 individuals die from falls globally, of which over 80% are in low- and middle-income countries.
- Adults older than 60 years of age suffer the greatest number of fatal falls.
- 37.3 million falls that are severe enough to require medical attention occur each year.
- Prevention strategies should emphasize education, training, creating safer environments, prioritizing fall-related research, and establishing effective policies to reduce risk.

## 3. Solution

### Technologies and Libraries Used
#### Mediapipe
I used [MediaPipe - Pose Estimation](https://google.github.io/mediapipe/solutions/pose.html). The MediaPipe Pose Landmarker task lets you detect landmarks of human bodies in an image or video.

#### OpenCV
OpenCV is used to draw a line, draw a dot, and decorate the user's UI.

#### YOLOv5 and YOLOv8
YOLOv5 and YOLOv8 models were trained on fall detection datasets to improve the accuracy of fall detection. These models help in identifying falls in real-time video streams.

#### Threading
Threading was utilized to ensure smooth email notifications when a fall is detected without interrupting the real-time video processing.

### Establish hypotheses and explain basic logic
#### How do you measure falls?
To measure falls, the distance between the body center of gravity (C.G) and the foot C.G is checked. If the distance exceeds a threshold (90 pixels or tall * 0.75), it is considered a fall.

#### How to find body's center of gravity?
First, find the rectangle's center of gravity. By dividing the human body into segments and finding the C.G for each part, you can determine the overall body's center of gravity.

#### Finally, we can see an example based on the previous theory
By applying the theory of finding the C.G of body parts, you can determine the body's overall center of gravity.

#### Heinrich's law (Reason for measuring count)
According to Heinrich's Law, when a person falls more than 300 times in the same place, it leads to one serious accident. Therefore, by counting the number of falls, we need to take action before the count exceeds 300.

Many people don't take falls seriously, and safety managers often have to manage too many areas. This often leads to installing safety devices only after a major accident.

### Perspective
#### A method for measuring the fall of distant and near objects
We know that near and far objects have different sizes. When measuring the fall, you can solve it by comparing the person's body C.G * 0.75 with the difference between the body C.G's X-axis and the center of the two feet X-axis.

#### How to Calculate Falls by Region
To recognize when the center point of the feet is in a specific region, check if it is within a predefined range. For example, the code checks if the point of action is within certain X and Y boundaries to determine a fall and updates the fall count accordingly.



This approach helps in determining falls by specific regions and ensuring accurate detection and counting.

## 4. Training YOLO Models

### Steps to Train YOLOv5 and YOLOv8

1. **Prepare Dataset:**
   - Collect and annotate images with falls and non-falls.
   - Split the dataset into training and validation sets.

2. **Install Dependencies:**
   - Install necessary libraries such as `torch`, `opencv-python`, and `yolov5`/`yolov8`.

   ```sh
   pip install torch opencv-python
   ```

3. **Clone YOLO Repository:**
   - Clone the YOLOv5 or YOLOv8 repository from GitHub.

   ```sh
   git clone https://github.com/ultralytics/yolov5
   cd yolov5
   ```

4. **Organize Data:**
   - Place your images and labels in the appropriate directories as per YOLO's structure.
   - Update the dataset configuration file with paths to your training and validation data.

5. **Train the Model:**
   - Run the training script with appropriate parameters.

   ```sh
   python train.py --img 640 --batch 16 --epochs 100 --data data.yaml --weights yolov5s.pt
   ```

   - For YOLOv8, the command might vary slightly:

   ```sh
   python train.py --img 640 --batch 16 --epochs 100 --data data.yaml --weights yolov8s.pt
   ```

6. **Evaluate the Model:**
   - After training, evaluate the model performance on the validation set.

   ```sh
   python val.py --data data.yaml --weights runs/train/exp/weights/best.pt --img 640
   ```

7. **Deploy the Model:**
   - Use the trained model for inference on real-time video feeds or new images.

## 5. Demos and Photos

### OpenCV Implementation
- Demo Video: [OpenCV Fall Detection Demo](#)
- Photos:
- <img src="images/opencv_demo1.png" alt="OpenCV Demo 1" width="200"/><img src="images/opencv_demo2.png" alt="OpenCV Demo 2" width="200"/><img src="images/opencv_demo3.png" alt="OpenCV Demo 3" width="200"/>




### YOLOv8 Implementation
- Demo Video: [YOLOv8 Fall Detection Demo](#)
- Photos:- <img src="a.png" alt="YOLOv8 Demo 1" width="200"/><img src="b.png" alt="YOLOv8 Demo 2" width="200"/><img src="c.png" alt="YOLOv8 Demo 3" width="200"/>

