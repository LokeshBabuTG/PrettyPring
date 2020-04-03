import xml.dom.minidom
import pyperclip
pyperclip.copy(xml.dom.minidom.parseString(pyperclip.paste()).toprettyxml())