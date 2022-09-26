'''
A test module

@author Oscar Capraro
'''

import main

def test_translate_rect_use():
  '''
  A testing function for when a use group is directly after a rectangle group.
  '''
  # Setup
  code = '<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="25.992ex" height="5.227ex" viewBox="0 -1446.1 11190.9 2250.4" role="img" focusable="false" style="vertical-align: -1.868ex;"><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><g transform="translate(120,0)"><rect stroke="none" width="1219" height="60" x="0" y="220"></rect><use xlink:href="#MJMATHI-64" x="346" y="676"></use><g transform="translate(60,-686)"><use xlink:href="#MJMATHI-64"></use><use xlink:href="#MJMATHI-78" x="523" y="0"></use></g></g><g transform="translate(1459,0)"><use xlink:href="#MJMAIN-28" x="0" y="0"></use><g transform="translate(392,0)"><use xlink:href="#MJMAIN-63"></use><use xlink:href="#MJMAIN-73" x="447" y="0"></use><use xlink:href="#MJMAIN-63" x="845" y="0"></use><use xlink:href="#MJMATHI-78" x="1572" y="0"></use></g><use xlink:href="#MJMAIN-29" x="2540" y="0"></use></g><use xlink:href="#MJMAIN-3D" x="4669" y="0"></use><use xlink:href="#MJMAIN-2212" x="5729" y="0"></use><g transform="translate(6677,0)"><use xlink:href="#MJMAIN-63"></use><use xlink:href="#MJMAIN-73" x="447" y="0"></use><use xlink:href="#MJMAIN-63" x="845" y="0"></use></g><use xlink:href="#MJMATHI-78" x="8249" y="0"></use><g transform="translate(8991,0)"><use xlink:href="#MJMAIN-63"></use><use xlink:href="#MJMAIN-6F" x="447" y="0"></use><use xlink:href="#MJMAIN-74" x="951" y="0"></use></g><use xlink:href="#MJMATHI-78" x="10615" y="0"></use></g></svg>'
  expected = "d/dx(cscx)=-cscxcotx"

  # Invoke
  stripped_code = main.strip_code(code)
  translated = main.translate(stripped_code)

  # Analyze
  assert translated == expected

