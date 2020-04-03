import xml.dom.minidom
import pyperclip
pyperclip.copy(json.dumps(json.loads(pyperclip.paste()), indent=4, sort_keys=True))