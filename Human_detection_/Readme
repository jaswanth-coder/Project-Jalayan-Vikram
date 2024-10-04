# AI-Driven Flood Disaster Response with Jalayan Vikram Robot

## Project Overview

This project focuses on utilizing the **Jalayan Vikram Robot**, equipped with a **Raspberry Pi camera**, to enhance disaster response efforts during flood emergencies. By integrating advanced computer vision algorithms such as **YOLOv8**, **YOLOv9**, and **Detectron2**, we have developed a robust AI system for accurate and real-time detection of people and obstacles in flood scenarios. This system optimizes rescue operations, providing a crucial tool for effective disaster management.

## Key Features

- **Real-time Detection:** Our AI models accurately detect humans, vehicles, and other relevant objects using the Jalayan Vikram Robot's camera, enabling quick responses in flood-affected areas.
- **Optimized for Disaster Response:** Designed specifically to operate in harsh flood conditions where rapid detection of people and obstacles is critical.
- **Custom Dataset Collection:** A curated dataset compiled from open-source flood images ensures the relevance and adaptability of the model for real-world applications.

---

## Data Collection

The dataset for this project was curated from publicly available sources, focusing on major floods, including:

- **2018 Kerala Flood**
- **2022 Assam Floods**
- **2023 Himalayan Floods**
- **2023 Chennai Floods**
- **2023 Thoothukkudi-Tirunelveli Floods**

The images in the dataset specifically focus on human detection in flood scenarios, with angles ranging from **15 to 30 degrees** to simulate real-world conditions.

### Dataset Structure

- **Total Images:** 120 images
- **Categories:** People, Cars, Bikes, Boats
- **Annotations:**
  - **Humans:** 561 instances
  - **Cars:** 69 instances
  - **Bikes:** 65 instances
  - **Boats:** 24 instances
  - **Total Annotations:** 719
  - **Average Annotations per Image:** ~6.0

The dataset is structured for class balance and ensures accurate training for human and object detection in flood environments. The median image resolution is **770x488 pixels**, with an average size of **0.40 megapixels**.

---

## Data Preprocessing and Annotation

Data preprocessing and annotation were carried out using the **Roboflow** platform with the following steps:

1. **Auto-Orient:** Ensured uniform image orientation.
2. **Static Crop:** Focused on the **20-86% horizontal** and **21-70% vertical** regions to emphasize the critical areas.
3. **Resizing:** Images were resized to a standardized **640x640 pixels** resolution.

We used the **Dino Ground 3.0v** model for **automated labeling**, which was then reviewed manually to ensure precise annotations. This careful process resulted in a high-quality dataset ready for training our AI models.

### Data Augmentation

To improve the robustness of our models, we applied three key data augmentation techniques:

- **Rotations:** 90° rotations (clockwise and counterclockwise) and random rotations between **-14° and +14°**.
- **Shearing:** Applied horizontal shearing up to **±10°** and vertical shearing up to **±6°**.
- **Brightness Adjustments:** Adjusted brightness levels by **-25% to +25%** to simulate varied lighting conditions.

These augmentations increased data diversity, helping the model handle challenges such as camera misfocus and varying flood conditions.

---

## How to Build and Run the Package

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/flood-response-jalayan.git
   cd flood-response-jalayan
   ```

2. **Install Required Dependencies**

   This project requires ROS2 and OpenCV for image processing. To install the necessary dependencies, run:

   ```bash
   sudo apt update
   sudo apt install ros-<your_ros2_version>-cv-bridge ros-<your_ros2_version>-image-transport
   sudo apt install python3-opencv
   ```

3. **Build the Package**

   Build the ROS2 workspace:

   ```bash
   colcon build
   ```

4. **Run the AI Detection Node**

   After the build, source the workspace and run the detection node:

   ```bash
   source install/setup.bash
   ros2 launch flood_response_jalayan detection_launch.py
   ```

5. **Test the System**

   Use the provided dataset to test the AI detection system on the Jalayan Vikram Robot.

---

## Contributing

We welcome contributions from the community! If you’d like to contribute, check out our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to get involved.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

By integrating AI and the **Jalayan Vikram Robot**, this project offers a real-time solution for flood disaster response. With our custom dataset and advanced computer vision models, rescue operations can be significantly enhanced, potentially saving lives in critical flood scenarios.

---
