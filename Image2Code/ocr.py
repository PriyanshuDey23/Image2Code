import easyocr

class OCRProcessor:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def extract_layout(self, img):
        result = self.reader.readtext(img)
        layout_data = []
        
        for (bbox, text, _confidence) in result:
            x_min, y_min = bbox[0]
            x_max, y_max = bbox[2]
            layout_data.append({
                "text": text,
                "coordinates": {
                    "x": (x_min + x_max) / 2,  # Approximate center
                    "y": (y_min + y_max) / 2
                }
            })
        
        return layout_data