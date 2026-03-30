import base64, sys

encoded = sys.argv[1]
script = base64.b64decode(encoded.encode("ascii")).decode("utf-8")
exec(script)
