# Ollama OCR

A Python-based OCR tool leveraging the **Llama 3.2-Vision** model for highly accurate text recognition from images, preserving original formatting and structure.

## Features
- 🚀 **High Accuracy**: Text recognition powered by the **Llama 3.2-Vision** model.
- 📝 **Preserves Formatting**: Maintains the original structure and layout of the recognized text.
- 🖼️ **Wide Format Support**: Works with image formats such as `.jpg`, `.jpeg`, and `.png`.
- ⚡️ **Customizable Output**: Returns results in either **Markdown** or **JSON** format.
- 💪 **Robust Error Handling**: Ensures smooth processing with clear error messages for unsupported formats or invalid configurations.

---

## System Requirements
- **Python** 3.8 or higher
- **Ollama Server** running locally
- **Llama 3.2-Vision** model installed

### Prerequisites
1. Ensure the **Ollama server** is running before using the tool.
2. Download and configure the **Llama 3.2-Vision** model for OCR tasks.

---

## Instalation

```
pip install ollamaocr-python
```

---
## Usage
Basic Usage

```
from ollamaocr import OllamaOCR

# Initialize the OCR tool
ocr = OllamaOCR()

# Perform OCR in Markdown format
markdown_result = ocr.perform_ocr("path/to/image.jpg", output_format="markdown")
print(markdown_result)

# Perform OCR in JSON format
json_result = ocr.perform_ocr("path/to/image.jpg", output_format="json")
print(json_result)
```

## Error Handling
The class provides comprehensive error handling for unsupported formats or invalid configurations:

```
from ollamaocr import OllamaOCR

ocr = OllamaOCR()

try:
    result = ocr.perform_ocr("invalid_file.bmp", output_format="markdown")
except ValueError as e:
    print(f"Error: {e}")
```

## Customizable Prompts
Modify the prompts used for OCR to suit specific requirements:

- Markdown Prompt: Preserves formatting in Markdown structure.
- JSON Prompt: Outputs results in JSON format.


## Limitations
Currently supports only .jpg, .jpeg, and .png image formats.
Requires the Ollama server to be running locally with the Llama 3.2-Vision model installed.

## License
This project is licensed under the MIT License.