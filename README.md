Main Bottlenecks:

    The get_textbox function in easyocr\detection.py and the subsequent calls to PyTorch's convolution (torch.conv2d) are the most time-consuming parts of the application, taking about 33.699 seconds cumulatively. This is expected as OCR is computationally intensive, especially when processing images for text detection.
    The readtext function in EasyOCR, which is the high-level function call for reading text from images, cumulatively took about 33.710 seconds. This further highlights that the bulk of the execution time is spent on OCR operations.
    The capture_screen function, which likely captures the screen for OCR, took about 0.743 seconds in total. Compared to OCR operations, this is significantly less but could be optimized for frequent captures.
