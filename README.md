# ⚽ Football Highlights Generator 🎥  

This project automates the creation of football match highlights from a full-length game video. Using Optical Character Recognition (OCR) technology, it monitors the scoreboard for changes in goals and captures key moments around those changes to generate highlight clips.

---

## 📜 **Table of Contents**

1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
5. [How It Works](#how-it-works)
6. [Usage](#usage)
7. [Future Enhancements](#future-enhancements)
8. [License](#license)

---

## 🌟 **Introduction**

Manually creating football highlights can be tedious. This project streamlines the process by analyzing the scoreboard in a football match video. When a change in the score is detected (indicating a goal), the script automatically captures the surrounding moments (20 seconds before and 10 seconds after) and compiles them into separate highlight clips.

---

## 🚀 **Features**

- **Score Detection**: Uses OCR to detect changes in the scoreboard from video frames.
- **Automated Highlight Creation**: Captures and saves key moments when goals are scored.
- **Customizable Parameters**: Easily modify the timeframe for clips (e.g., duration before and after goals).
- **Efficient Processing**: Processes every 300th frame to optimize performance without losing accuracy.

---

## 💻 **Technologies Used**

- **Python**: Core programming language.
- **OpenCV**: For video frame processing and scoreboard extraction.
- **Pytesseract**: OCR library for detecting text (scores) in images.
- **NumPy**: For image transformations.
- **MoviePy**: For video editing and creating highlight clips.

---

## 🛠 **Setup Instructions**

Follow these steps to set up and run the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/football-highlights-generator.git
   cd football-highlights-generator
   ```

2. **Install Dependencies**:
   Make sure Python 3.8+ is installed, then install the required libraries:
   ```bash
   pip install opencv-python pytesseract moviepy numpy
   ```

3. **Install Tesseract-OCR**:
   Download and install Tesseract-OCR from [here](https://github.com/tesseract-ocr/tesseract).  
   Update the path to Tesseract in the script:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
   ```

4. **Prepare the Input Video**:
   - Place the full football match video in the project directory.
   - Set the video file path in the script:  
     ```python
     video = 'vid2.mp4'
     ```

5. **Run the Script**:
   Execute the script:
   ```bash
   python main.py
   ```

---

## 🔎 **How It Works**

1. **Video Frame Processing**:
   - Reads frames from the input video every 300 frames for efficiency.
   - Extracts a cropped region of the frame containing the scoreboard.  

2. **Score Detection**:
   - Uses Pytesseract OCR to detect changes in the score.
   - Filters and cleans the detected text to ensure accuracy.  

3. **Highlight Generation**:
   - Captures moments when the score changes.
   - Extracts a 30-second clip (20 seconds before and 10 seconds after the score change).
   - Saves the highlight clips with a filename indicating the new score.  

---

## 📖 **Usage**

1. Ensure the input video and `Dump` folder (for intermediate frames) exist in the directory.
2. Run the script to process the video.  
3. Retrieve the generated highlight clips named in the format `vid<Score>_edited.mp4`.

---

## 🌟 **Future Enhancements**

- Enhance scoreboard detection with deep learning-based OCR for higher accuracy.
- Add support for processing multiple videos in a batch.
- Implement a GUI for easier video upload and parameter customization.
- Include an option to combine all highlights into a single video.
