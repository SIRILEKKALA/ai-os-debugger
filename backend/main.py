from ocr.screen_reader import capture_and_read
from analyzer.error_classifier import clean_ocr_text, extract_error

def run():
    raw_text = capture_and_read()
    cleaned = clean_ocr_text(raw_text)
    error = extract_error(cleaned)

    if error:
        print("🚨 ERROR DETECTED:")
        print(error)
    else:
        print("✅ No recognizable error detected")

if __name__ == "__main__":
    run()
