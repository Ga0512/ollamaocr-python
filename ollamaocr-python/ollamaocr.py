import ollama
import os

class OllamaOCR:
    """
    A class to perform OCR on images using the Llama 3.2-Vision model.
    Provides options to return results in Markdown or JSON format.
    """

    MARKDOWN = """Act as an OCR assistant. Analyze the provided image and:
    1. Recognize all visible text in the image as accurately as possible.
    2. Maintain the original structure and formatting of the text.
    3. If any words or phrases are unclear, indicate this with [unclear] in your transcription.
    Provide only the transcription without any additional comments.

    Requirements:
      - Output Only Markdown: Return solely the Markdown content without any additional explanations or comments.
      - No Delimiters: Do not use code fences or delimiters like ```markdown.
      - Complete Content: Do not omit any part of the page, including headers, footers, and subtext.
    """

    JSON = """Act as an OCR assistant. Analyze the provided image and:
    1. Recognize all visible text in the image as accurately as possible.
    2. Maintain the original structure and formatting of the text.
    3. If any words or phrases are unclear, indicate this with [unclear] in your transcription.
    Provide only the transcription without any additional comments.

    Requirements:
      - Output Only JSON: Return solely the JSON content without any additional explanations or comments.
      - No Delimiters: Do not use code fences or delimiters.
      - Complete Content: Do not omit any part of the page, including headers, footers, and subtext.
    """

    def __init__(self, model='llama3.2-vision'):
        """
        Initialize the OCR class with the specified model.

        :param model: The name of the model to use for OCR.
        """
        self.model = model

    def perform_ocr(self, image_path, output_format="markdown"):
        """
        Perform OCR on the given image and return the result in the specified format.

        :param image_path: Path to the image file.
        :param output_format: The desired output format ("markdown" or "json").
        :return: The OCR result in the specified format.
        """

        valid_extensions = {"jpg", "jpeg", "png"}
        extension = os.path.splitext(image_path)[1].lower().strip(".")
        
        if extension not in valid_extensions:
            raise ValueError(f"Invalid image format '{extension}'. Supported formats: {valid_extensions}")

        if output_format not in {"markdown", "json"}:
            raise ValueError("Invalid output format. Choose either 'markdown' or 'json'.")

        content = self.MARKDOWN if output_format == "markdown" else self.JSON

        result = ollama.chat(
            model=self.model,
            messages=[{
                'role': 'user',
                'content': content,
                'images': [image_path]
            }]
        )

        return result.message.content

# Example usage:
# ocr = OllamaOCR()
# markdown_result = ocr.perform_ocr("path/to/image.jpg", output_format="markdown")
# json_result = ocr.perform_ocr("path/to/image.jpg", output_format="json")
