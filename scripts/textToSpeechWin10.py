import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
hebrew = "אלף בית עברית"
speak.Speak("Hallå där världen")
