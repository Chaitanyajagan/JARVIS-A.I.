import pywhatkit
import pyttsx3
import datetime as dt

# Initialize TTS (with cross-platform fallback)
try:
    engine = pyttsx3.init("sapi5")  # Windows SAPI5
except Exception:
    engine = pyttsx3.init()         # Fallback for macOS/Linux

voices = engine.getProperty("voices")
if voices:
    engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(text: str):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception:
        pass  # Do not crash if TTS fails

def get_phone_number() -> str | None:
    print("Enter the recipient's phone number in international format (e.g., +911234567890):")
    speak("Please enter the recipient phone number.")
    number = input("Phone number: ").strip()
    if not number.startswith("+") or not number[1:].isdigit():
        print("Invalid number format. Use E.164 format like +911234567890.")
        return None
    if len(number) < 8 or len(number) > 16:
        print("Number length seems invalid. Check the country code and digits.")
        return None
    return number

def schedule_time(minutes_ahead: int = 2) -> tuple[int, int]:
    now = dt.datetime.now()
    t = now + dt.timedelta(minutes=minutes_ahead)
    return t.hour, t.minute

def send_message():
    number = get_phone_number()
    if not number:
        return

    speak("What is the message?")
    message = input("Enter the message: ").strip()
    if not message:
        print("Empty message. Aborting.")
        return

    print(f"Sending message to {number} in ~2 seconds...")
    speak("Sending your message.")

    try:
        # Instant send with minimal wait buffer
        pywhatkit.sendwhatmsg_instantly(number, message, wait_time=2, tab_close=True)
        print("Message sent (or attempted). Ensure WhatsApp Web is logged in and visible.")
    except Exception as e:
        print(f"Failed to send message instantly: {e}")

if __name__ == "__main__":
    send_message()
