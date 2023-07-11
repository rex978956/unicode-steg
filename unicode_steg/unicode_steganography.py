# Unicode Steganography with Zero-Width Characters
# rewrite according to http://330k.github.io/misc_tools/unicode_steganography.html

import random
import re
import math


chars = []
radix = 0
codelengthText = 0

def setUseChars(newchars):
    global chars, radix, codelengthText
    if len(newchars) >= 2:
        chars = list(newchars)
        radix = len(chars)
        codelengthText = math.ceil(math.log(65536) / math.log(radix))
    return None

def encode(original, hidden):
    return combine_shuffle_string(original, encode_to_zerowidth_characters(hidden), codelengthText)

def decode(text):
    splitted = split_zerowidth_characters(text)
    return {
        'originalText': splitted['originalText'],
        'hiddenText': decode_from_zero_width_characters(splitted['hiddenText'])
    }


def to_base(base, num):
    digits = []
    while num > 0:
        digits.append(str(num % base))
        num //= base
    digits.reverse()
    return ''.join(digits)

def encode_to_zerowidth_characters(str1):
    result = []
    base = '0' * codelengthText

    for i in range(len(str1)):
        c = ord(str1[i])
        d = base + to_base(radix, c)
        result.append(d[-codelengthText:])

    r = ''.join(result)

    for i in range(radix):
        r = r.replace(str(i), chars[i])

    return r

def combine_shuffle_string(str1, str2, codelength):
    result = []
    c0 = re.split(r'([\u0000-\u002F\u003A-\u0040\u005b-\u0060\u007b-\u007f])|([\u0030-\u0039]+)|([\u0041-\u005a\u0061-\u007a]+)|([\u0080-\u00FF]+)|([\u0100-\u017F]+)|([\u0180-\u024F]+)|([\u0250-\u02AF]+)|([\u02B0-\u02FF]+)|([\u0300-\u036F]+)|([\u0370-\u03FF]+)|([\u0400-\u04FF]+)|([\u0500-\u052F]+)|([\u0530-\u058F]+)|([\u0590-\u05FF]+)|([\u0600-\u06FF]+)|([\u0700-\u074F]+)|([\u0750-\u077F]+)|([\u0780-\u07BF]+)|([\u07C0-\u07FF]+)|([\u0800-\u083F]+)|([\u0840-\u085F]+)|([\u08A0-\u08FF]+)|([\u0900-\u097F]+)|([\u0980-\u09FF]+)|([\u0A00-\u0A7F]+)|([\u0A80-\u0AFF]+)|([\u0B00-\u0B7F]+)|([\u0B80-\u0BFF]+)|([\u0C00-\u0C7F]+)|([\u0C80-\u0CFF]+)|([\u0D00-\u0D7F]+)|([\u0D80-\u0DFF]+)|([\u0E00-\u0E7F]+)|([\u0E80-\u0EFF]+)|([\u0F00-\u0FFF]+)|([\u1000-\u109F]+)|([\u10A0-\u10FF]+)|([\u1100-\u11FF]+)|([\u1200-\u137F]+)|([\u1380-\u139F]+)|([\u13A0-\u13FF]+)|([\u1400-\u167F]+)|([\u1680-\u169F]+)|([\u16A0-\u16FF]+)|([\u1700-\u171F]+)|([\u1720-\u173F]+)|([\u1740-\u175F]+)|([\u1760-\u177F]+)|([\u1780-\u17FF]+)|([\u1800-\u18AF]+)|([\u18B0-\u18FF]+)|([\u1900-\u194F]+)|([\u1950-\u197F]+)|([\u1980-\u19DF]+)|([\u19E0-\u19FF]+)|([\u1A00-\u1A1F]+)|([\u1A20-\u1AAF]+)|([\u1AB0-\u1AFF]+)|([\u1B00-\u1B7F]+)|([\u1B80-\u1BBF]+)|([\u1BC0-\u1BFF]+)|([\u1C00-\u1C4F]+)|([\u1C50-\u1C7F]+)|([\u1CC0-\u1CCF]+)|([\u1CD0-\u1CFF]+)|([\u1D00-\u1D7F]+)|([\u1D80-\u1DBF]+)|([\u1DC0-\u1DFF]+)|([\u1E00-\u1EFF]+)|([\u1F00-\u1FFF]+)|([\u2000-\u206F]+)|([\u2070-\u209F]+)|([\u20A0-\u20CF]+)|([\u20D0-\u20FF]+)|([\u2100-\u214F]+)|([\u2150-\u218F]+)|([\u2190-\u21FF]+)|([\u2200-\u22FF]+)|([\u2300-\u23FF]+)|([\u2400-\u243F]+)|([\u2440-\u245F]+)|([\u2460-\u24FF]+)|([\u2500-\u257F]+)|([\u2580-\u259F]+)|([\u25A0-\u25FF]+)|([\u2600-\u26FF]+)|([\u2700-\u27BF]+)|([\u27C0-\u27EF]+)|([\u27F0-\u27FF]+)|([\u2800-\u28FF]+)|([\u2900-\u297F]+)|([\u2980-\u29FF]+)|([\u2A00-\u2AFF]+)|([\u2B00-\u2BFF]+)|([\u2C00-\u2C5F]+)|([\u2C60-\u2C7F]+)|([\u2C80-\u2CFF]+)|([\u2D00-\u2D2F]+)|([\u2D30-\u2D7F]+)|([\u2D80-\u2DDF]+)|([\u2DE0-\u2DFF]+)|([\u2E00-\u2E7F]+)|([\u2E80-\u2EFF]+)|([\u2F00-\u2FDF]+)|([\u2FF0-\u2FFF]+)|([\u3000-\u303F]+)|([\u3040-\u309F]+)|([\u30A0-\u30FF]+)|([\u3100-\u312F]+)|([\u3130-\u318F]+)|([\u3190-\u319F]+)|([\u31A0-\u31BF]+)|([\u31C0-\u31EF]+)|([\u31F0-\u31FF]+)|([\u3200-\u32FF]+)|([\u3300-\u33FF]+)|([\u3400-\u4DBF]+)|([\u4DC0-\u4DFF]+)|([\u4E00-\u9FFF]+)|([\uA000-\uA48F]+)|([\uA490-\uA4CF]+)|([\uA4D0-\uA4FF]+)|([\uA500-\uA63F]+)|([\uA640-\uA69F]+)|([\uA6A0-\uA6FF]+)|([\uA700-\uA71F]+)|([\uA720-\uA7FF]+)|([\uA800-\uA82F]+)|([\uA830-\uA83F]+)|([\uA840-\uA87F]+)|([\uA880-\uA8DF]+)|([\uA8E0-\uA8FF]+)|([\uA900-\uA92F]+)|([\uA930-\uA95F]+)|([\uA960-\uA97F]+)|([\uA980-\uA9DF]+)|([\uA9E0-\uA9FF]+)|([\uAA00-\uAA5F]+)|([\uAA60-\uAA7F]+)|([\uAA80-\uAADF]+)|([\uAAE0-\uAAFF]+)|([\uAB00-\uAB2F]+)|([\uAB30-\uAB6F]+)|([\uAB70-\uABBF]+)|([\uABC0-\uABFF]+)|([\uAC00-\uD7AF]+)|([\uD7B0-\uD7FF]+)|([\uD800-\uDFFF]+)|([\uE000-\uF8FF]+)|([\uF900-\uFAFF]+)|([\uFB00-\uFB4F]+)|([\uFB50-\uFDFF]+)|([\uFE00-\uFE0F]+)|([\uFE10-\uFE1F]+)|([\uFE20-\uFE2F]+)|([\uFE30-\uFE4F]+)|([\uFE50-\uFE6F]+)|([\uFE70-\uFEFF]+)|([\uFF00-\uFFEF]+)|([\uFFF0-\uFFFF]+)', str1)
    c1 = [c for c in c0 if c != '' and c != None]
    c2 = re.findall('(.{' + str(codelength) + '})', str2)
    ratio = len(c1) / (len(c1) + len(c2))
    i = 0
    j = 0
    while i < len(c1) and j < len(c2):
        if random.random() <= ratio:
            result.append(c1[i])
            i += 1
        else:
            result.append(c2[j])
            j += 1
    c1 = c1[i:]
    c2 = c2[j:]
    result.extend(c1)
    result.extend(c2)
    
    return ''.join(result)


def split_zerowidth_characters(str1):
    result = {}
    result['originalText'] = re.sub('[' + ''.join(chars) + ']', '', str1)
    result['hiddenText'] = re.sub('[^' + ''.join(chars) + ']', '', str1)
    return result

def decode_from_zero_width_characters(str1):
    r = str1
    result = []
    for i in range(radix):
        r = r.replace(chars[i], str(i))
    for i in range(0, len(r), codelengthText):
        code = int(r[i:i + codelengthText], radix)
        result.append(chr(code))
    return ''.join(result)

setUseChars('\u200c\u200d\u202c\ufeff')

unicodeSteganographer = {
    'encode': encode,
    'decode': decode,
    'setUseChars': setUseChars
}
