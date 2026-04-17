import pywhatkit
import datetime

choice = int(input("Enter your choice \n(1.🄷🄴🄻🄻🄾)\n(2.🅷🅴🅻🅻🅾)\n(3.ⓗⓔⓛⓛⓞ)\n(4.🅗🅔🅛🅛🅞)\n(5.¡ɐᴉdɐԀ ollǝH)\n(6.ℍ𝕖𝕝𝕝𝕠)\n(7.ＨＥＬＬＯ)\n(8.ʜᴇʟʟᴏ)\n(9.𝙷𝙴𝙻𝙻𝙾 𝙿𝙰𝙿𝙸𝙰)\n(10.♓🎗️👢👢⚽)\n(11.olleH): "))
main_text=input("Enter your text: ")
    
if(choice==1 or choice=="🄷🄴🄻🄻🄾"):
    # 🄷🄴🄻🄻🄾
    # box text
    def text(text):
        box = {
            'A': '🄰', 'B': '🄱', 'C': '🄲', 'D': '🄳', 'E': '🄴', 'F': '🄵',
            'G': '🄶', 'H': '🄷', 'I': '🄸', 'J': '🄹', 'K': '🄺', 'L': '🄻',
            'M': '🄼', 'N': '🄽', 'O': '🄾', 'P': '🄿', 'Q': '🅀', 'R': '🅁',
            'S': '🅂', 'T': '🅃', 'U': '🅄', 'V': '🅅', 'W': '🅆', 'X': '🅇',
            'Y': '🅈', 'Z': '🅉'
        }
        return ''.join(box.get(c.upper(), c) for c in text)
    msg=text(main_text)

if(choice==2 or choice=="🅷🅴🅻🅻🅾"):
    # 🅷🅴🅻🅻🅾
    # solid box text
    def text(text):
        styled = ''
        for char in text:
            if char.isalpha():
                styled += chr(0x1F130 + (ord(char.upper()) - ord('A')))
            else:
                styled += char
        return styled
    msg=text(main_text)

if(choice==3 or choice=="ⓗⓔⓛⓛⓞ"):
    # ⓗⓔⓛⓛⓞ
    # Bubble text
    def text(text):
        normal = 'abcdefghijklmnopqrstuvwxyz'
        bubble =  'ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ'
        result = ''
        for char in text.lower():
            if char in normal:
                result += bubble[normal.index(char)]
            else:
                result += char  # keep spaces, punctuation etc.
        return result
    msg=text(main_text)

if(choice==4 or choice=="🅗🅔🅛🅛🅞"):
    # 🅗🅔🅛🅛🅞
    # solid bubble text
    def text(text):
        bubble = { 
            'A':'🅐','B':'🅑','C':'🅒','D':'🅓','E':'🅔','F':'🅕','G':'🅖',
            'H':'🅗','I':'🅘','J':'🅙','K':'🅚','L':'🅛','M':'🅜','N':'🅝',
            'O':'🅞','P':'🅟','Q':'🅠','R':'🅡','S':'🅢','T':'🅣','U':'🅤',
            'V':'🅥','W':'🅦','X':'🅧','Y':'🅨','Z':'🅩'
        }
        return ''.join(bubble.get(c.upper(), c) for c in text)
    msg=text(main_text)
    
if(choice==5 or choice=="¡ɐᴉdɐԀ ollǝH"):
    # ¡ɐᴉdɐԀ ollǝH 
    # (flipped) text
    def text(text):
        flipped = {
            'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ',
            'g': 'ƃ', 'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'ʃ',
            'm': 'ɯ', 'n': 'u', 'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ',
            's': 's', 't': 'ʇ', 'u': 'n', 'v': 'ʌ', 'w': 'ʍ', 'x': 'x',
            'y': 'ʎ', 'z': 'z',
            'A': '∀', 'B': '𐐒', 'C': 'Ɔ', 'D': 'p', 'E': 'Ǝ', 'F': 'Ⅎ',
            'G': 'פ', 'H': 'H', 'I': 'I', 'J': 'ſ', 'K': 'ʞ', 'L': '˥',
            'M': 'W', 'N': 'N', 'O': 'O', 'P': 'Ԁ', 'Q': 'Q', 'R': 'ɹ',
            'S': 'S', 'T': '⊥', 'U': '∩', 'V': 'Λ', 'W': 'M', 'X': 'X',
            'Y': '⅄', 'Z': 'Z',
            '1': '⇂', '2': 'ᔭ', '3': 'Ɛ', '4': 'ㄣ', '5': 'ϛ', '6': '9',
            '7': 'ㄥ', '8': '8', '9': '6', '0': '0',
            '.': '˙', ',': "'", "'": ',', '"': '„', '_': '‾',
            '?': '¿', '!': '¡', '(': ')', ')': '(', '[': ']', ']': '[',
            '{': '}', '}': '{', '<': '>', '>': '<'
        }
        return ''.join(flipped.get(c, c) for c in text[::-1])
    msg = text(main_text)

if(choice==6 or choice=="ℍ𝕖𝕝𝕝𝕠"):
    # ℍ𝕖𝕝𝕝𝕠
    #double stucked style
    def text(text):
        a, z = ord('a'), ord('z')
        A, Z = ord('A'), ord('Z')
        result = ''
        for c in text:
            if c.islower():
                result += chr(0x1D552 + ord(c) - a)
            elif c.isupper():
                result += chr(0x1D538 + ord(c) - A)
            else:
                result += c
        return result
    msg=text(main_text)
    
if(choice==7 or choice=="ＨＥＬＬＯ"):
    # ＨＥＬＬＯ
    # full width text
    def text(text):
        return ''.join(chr(ord(c) + 65248) if c != ' ' else ' ' for c in text)
    msg=text(main_text)
    
if(choice==8 or choice=="ʜᴇʟʟᴏ"):
    # ʜᴇʟʟᴏ
    # small caps letter
    def text(text):
        mapping = {
            'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ꜰ',
            'g': 'ɢ', 'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ',
            'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ',
            's': 's', 't': 'ᴛ', 'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x',
            'y': 'ʏ', 'z': 'ᴢ'
        }
        return ''.join(mapping.get(c.lower(), c) for c in text)
    msg=text(main_text)
    
if(choice==9 or choice=="𝙷𝙴𝙻𝙻𝙾"):
    # 𝙷𝙴𝙻𝙻𝙾 𝙿𝙰𝙿𝙸𝙰
    # mono space text
    def text(text):
        base = ord('A')
        mapping = {chr(i): chr(0x1D670 + i - base) for i in range(base, base + 26)}
        mapping.update({chr(i + 32): chr(0x1D68A + i) for i in range(26)})
        return ''.join(mapping.get(c, c) for c in text)
    msg=text(main_text)
    
if(choice==10 or choice=="♓🎗️👢👢⚽"):
    # ♓🎗️👢👢⚽
    # emoji text 
    def text(text):
        emoji_map = {
            'a': '🅰️', 'b': '🅱️', 'c': '🌜', 'd': '🌛', 'e': '🎗️', 'f': '🎏',
            'g': '🌀', 'h': '♓', 'i': '🎐', 'j': '🎷', 'k': '🎋', 'l': '👢',
            'm': '〽️', 'n': '🎶', 'o': '⚽', 'p': '🅿️', 'q': '🍳', 'r': '🌱',
            's': '💲', 't': '🌴', 'u': '⛎', 'v': '✅', 'w': '🔱', 'x': '❌',
            'y': '🍸', 'z': '💤'
        }
        result = ''
        for c in text.lower():
            if c in emoji_map:
                result += emoji_map[c]
            else:
                result += c  # Keep spaces, punctuation
        return result
    msg=text(main_text)

if(choice==11 or choice=="olleH"):
    # olleH
    # reverse text
    def text(text):
        return text[::-1]
    msg=text(main_text)

# Final messaging case
print("\n✨ Final Message Preview:")
print(msg)

reply = input("\nWant to send it via WhatsApp? (Y/N): ")

if reply.lower() == "y":
    country_code = input("Enter country code (e.g., +91): ")
    number = input("Enter WhatsApp number(only number, e.g., 7897654328): ")
    ph = country_code + number

    # Time setup (add 1 minute, handle overflow)
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute + 1
    if minute >= 60:
        hour = (hour + 1) % 24
        minute = minute % 60

    print(f"\n⏳ Sending message to {ph} at {hour}:{minute:02d}...")
    pywhatkit.sendwhatmsg(ph, msg, hour, minute)
    print("✅ Message scheduled successfully!")

else:
    print("✅ Style created. Not sending on WhatsApp.")