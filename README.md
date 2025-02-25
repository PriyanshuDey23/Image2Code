# Design to Website Generator

![](1.png)
![](2.png)

## 🚀 Overview
The **Design to Website Generator** allows users to upload a design image (e.g., JPG, PNG, JPEG) and converts it into a functional HTML representation. It leverages **Optical Character Recognition (OCR)** to extract the layout and **Google's Generative AI** to generate structured HTML code using **LangChain**.

## 🔥 Features

- **OCR Processing**: Extracts layout details from uploaded images using **EasyOCR**.
- **AI-Powered HTML Generation**: Converts extracted layouts into structured **HTML code**.
- **Streamlit UI**: User-friendly interface for seamless image uploading and HTML previewing.
- **Google Generative AI**: Utilizes **gemini-2.0-flash** model for generating high-quality HTML.
- **Custom Prompting**: A tailored prompt template enhances HTML generation accuracy.

## 📌 Prerequisites
Before running the application, ensure you have the following installed:

- **Python 3.9 or higher**
- **Google API Key** (required for Generative AI)
- **Required Python packages**:
  - `streamlit`
  - `langchain`
  - `PIL`
  - `dotenv`
  - `Image2Code`

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/PriyanshuDey23/Image2Code.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Image2Code
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables by creating a `.env` file in the root directory:
   ```
   GOOGLE_API_KEY=<your_google_api_key>
   ```

## 🚀 Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser (usually at `http://localhost:8501`).

3. Upload your **design image** (JPG, PNG, or JPEG).

4. Click on the **"Generate HTML"** button to process the image.

5. View the **generated HTML code** or its **live preview** in the app.

## 🏗️ Components
- **OCR Processor**: Extracts layout from the uploaded image using **EasyOCR**.
- **LangChain**: Handles AI prompting and HTML generation.
- **Streamlit**: Provides the interactive web interface.
- **Google Generative AI**: Powers HTML code generation.

## 🎨 Customization
You can modify the **custom prompt template (`CUSTOM_PROMPT_TEMPLATE`)** in the code to adjust the HTML generation logic according to your specific requirements.

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.



