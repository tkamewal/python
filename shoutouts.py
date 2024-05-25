from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak

speak("tanmay kamewal")