import cv2
import numpy as np

class Model:
    # Colors.
    BLACK = (0, 0, 0)
    BLUE = (255, 178, 50)
    GREEN = (0, 255, 0)
    YELLOW = (0, 255, 255)
    RED = (0, 0, 255)
    WHITE = (255, 255, 255)
    def __init__(self, weight_path, input_width=640, input_height=640, score_threshold=0.5,
                 nms_threshold=0.45, confidence_threshold=0.5):
        self.weight_path = weight_path

        self.input_width = input_width
        self.input_height = input_height
        self.score_threshold = score_threshold
        self.nms_threshold = nms_threshold
        self.confidence_threshold = confidence_threshold

        self.model = cv2.dnn.readNet(self.weight_path)
        self.classes = ['green apple', 'red apple', 'rotten apple']

    def pre_process(self, image):
        blob = cv2.dnn.blobFromImage(image, 1 / 255, (self.input_width, self.input_height), [0, 0, 0], 1, crop=False)
        self.model.setInput(blob)
        outputs = self.model.forward(self.model.getUnconnectedOutLayersNames())
        return outputs

    def post_process(self, image, outputs):
        class_ids = []
        confidences = []
        boxes = []

        # Rows.
        rows = outputs[0].shape[1]
        image_height, image_width = image.shape[:2]
        # Resizing factor.
        x_factor = image_width / self.input_width
        y_factor = image_height / self.input_height
        for r in range(rows):
            row = outputs[0][0][r]
            confidence = row[4]
            # Discard bad detections and continue.
            if confidence >= self.confidence_threshold:
                classes_scores = row[5:]
                # Get the index of max class score.
                class_id = np.argmax(classes_scores)
                #  Continue if the class score is above threshold.
                if classes_scores[class_id] >= self.score_threshold:
                    confidences.append(confidence)
                    class_ids.append(class_id)
                    cx, cy, w, h = row[0], row[1], row[2], row[3]
                    left = int((cx - w / 2) * x_factor)
                    top = int((cy - h / 2) * y_factor)
                    width = int(w * x_factor)
                    height = int(h * y_factor)
                    box = np.array([left, top, width, height])
                    boxes.append(box)

        # Perform non maximum suppression to eliminate redundant, overlapping boxes with lower confidences.
        indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence_threshold, self.nms_threshold)

        # const font
        self.lw = max(round(sum(image.shape) / 2 * 0.003), 2)
        self.tf = max(self.lw - 1, 1)

        num_red_apple = 0
        num_green_apple = 0
        num_rotten_apple = 0
        for i in indices:
            box = boxes[i]
            left = box[0]
            top = box[1]
            width = box[2]
            height = box[3]

            x_cen = int(width / 2 + left)
            y_cen = int(height / 2 + top)

            # Draw bounding box.
            # cv2.rectangle(input_image, (left, top), (left + width, top + height), BLUE, 3*THICKNESS)
            cv2.circle(image, (x_cen, y_cen), self.lw * 2, self.YELLOW, -1)
            cv2.rectangle(image, (left, top), (left + width, top + height), self.BLUE, thickness=self.lw,
                          lineType=cv2.LINE_AA)
            # Class label.
            # label = "{}:{:.2f}".format('Vehicle', confidences[i])
            label = "{}:{:.2f}".format(self.classes[class_ids[i]], confidences[i])
            # Draw label.
            self.draw_label(image, label, left, top)
            # count apple
            if self.classes[class_ids[i]] == 'green apple':
                num_green_apple += 1
            elif self.classes[class_ids[i]] == 'red apple':
                num_red_apple += 1
            elif self.classes[class_ids[i]] == 'rotten apple':
                num_rotten_apple += 1

        return image, num_red_apple, num_green_apple, num_rotten_apple

    def draw_label(self, im, label, x, y):
        """Draw text onto image at location."""
        # Get text size.
        text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, fontScale=self.lw / 3, thickness=self.tf)
        dim, baseline = text_size[0], text_size[1]
        # Use text size to create a BLACK rectangle.
        cv2.rectangle(im, (x, y), (x + dim[0], y + dim[1] + baseline), (0, 0, 0), -1, lineType=cv2.LINE_AA)
        # Display text inside the rectangle.
        cv2.putText(im, label, (x, y + dim[1]), cv2.FONT_HERSHEY_SIMPLEX, self.lw / 3, self.YELLOW, thickness=self.tf,
                    lineType=cv2.LINE_AA)