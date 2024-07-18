


# Final Year Project By Rohit Prajapat(2020BITE052) 



## 0. Contents
1. Introduce
2. Motivation
   - Why do we detect falling down?
3. Solution
   - Technologies and Libraries Used
       - mediapipe
       - opencv
   - Establish hypotheses and explain basic logic
       - How do you measure falls?
   - Heinrich's law
       - If you almost fall more than 300 times, it becomes a major disaster in the future.
   - Perspective
       - A method for measuring the fall of distant and near objects.
       - How to Calculate Falls by Region.

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
I used [MediaPipe - Pose Estimation]. The MediaPipe Pose Landmarker task lets you detect landmarks of human bodies in an image or video.

#### OpenCV
It is used to draw a line, draw a dot, and decorate the user's UI.

### Establish hypotheses and explain basic logic
#### How do you measure falls?
To measure falls, the distance between the body center of gravity (C.G) and the foot C.G is checked. If the distance exceeds a threshold (90 pixels or tall * 0.75), it is considered a fall.

#### How to find body's center of gravity?
First, find the rectangle's center of gravity. By dividing the human body into segments and finding the C.G for each part, you can determine the overall body's center of gravity.

#### Finally, we can see an example based on the previous theory
By applying the theory of finding the C.G of body parts, you can determine the body's overall center of gravity.

#### Heinrich law (Reason for measuring count)
According to Heinrich's Law, when a person falls more than 300 times in the same place, it leads to one serious accident. Therefore, by counting the number of falls, we need to take action before the count exceeds 300.

Many people don't take falls seriously, and safety managers often have to manage too many areas. This often leads to installing safety devices only after a major accident.

### Perspective
#### A method for measuring the fall of distant and near objects
We know that near and far objects have different sizes. When measuring the fall, you can solve it by comparing the person's body C.G * 0.75 with the difference between the body C.G's X-axis and the center of the two feet X-axis.

#### How to Calculate Falls by Region
To recognize when the center point of the feet is in a specific region, check if it is within a predefined range. For example, the code checks if the point of action is within certain X and Y boundaries to determine a fall and updates the fall count accordingly.

```python
if Point_of_action_X < 320 and Point_of_action_X > 100 and Point_of_action_Y > 390 and Point_of_action_Y > y and standing and stage == 'falling':               
    cv2.putText(image, 'fall', (320, 240), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
    stage = "standing"
    counter_three += 1
```

This approach helps in determining falls by specific regions and ensuring accurate detection and counting.
```

