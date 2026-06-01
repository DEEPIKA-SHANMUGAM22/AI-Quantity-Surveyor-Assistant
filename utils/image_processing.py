import cv2

def load_image(path):
    return cv2.imread(path)

def preprocess_image(img):
    import cv2

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Threshold → removes text noise
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # Morphology → connect broken walls
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    return morph

def detect_edges(img):
    edges = cv2.Canny(img, 50, 150)
    return edges

def detect_lines(edges, original_img):
    import cv2

    line_img = original_img.copy()

    lines = cv2.HoughLinesP(
        edges,
        1,
        3.14 / 180,
        threshold=120,
        minLineLength=100,
        maxLineGap=5
    )

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(line_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return line_img

def detect_contours(processed_img):
    import cv2

    contours, _ = cv2.findContours(
        processed_img,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    return contours