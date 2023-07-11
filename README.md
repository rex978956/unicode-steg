# unicode-steg

Unicode Steganography with Zero-Width Characters
This is plain text steganography with zero-width characters of Unicode.
Zero-width characters is inserted within the words.

Rewrite from [330k/unicode-steganography](https://330k.github.io/misc_tools/unicode_steganography.html)

### Installation

```bash
$ cd unicode-steg
$ pip install -e .
```

### Usage Example

```.py
import unicode_steg

encoded = unicode_steg.encode('Original text', 'Hidden text')
decoded = unicode_steg.decode(encoded)

print('Original text: ' + decoded['originalText'])
print('Hidden text: ' + decoded['hiddenText'])
```

### License

[MIT](https://opensource.org/licenses/MIT)
