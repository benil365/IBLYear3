import figlet
import sys

if len(sys.argv) == 1:
    font = figlet.Figlet(font='random')
elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
    font_name = sys.argv[2]
    try:
        font = figlet.Figlet(font=font_name)
    except figlet.FontNotFound:
        print(f"Font '{font_name}' not found")
        sys.exit(1)
else:
    print("Usage: python figlet.py [-f FONT_NAME]")
    sys.exit(1)

text = input("Enter text: ")
output = font.renderText(text)
print(output)