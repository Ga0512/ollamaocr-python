from ollamaocr import OllamaOCR

ocr = OllamaOCR()
markdown_result = ocr.perform_ocr("/content/handwriting.jpg", output_format="markdown")
json_result = ocr.perform_ocr("/content/handwriting.jpg", output_format="json")


print(markdown_result)
print(json_result)