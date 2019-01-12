import pycurl
from io import BytesIO
import xml.etree.ElementTree as ET

buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://wiki.urbandead.com/index.php/User:DangerReport/Ackland_Mall')
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a byte string.
# We have to know the encoding in order to print it to a text file
# such as standard output.
print(body.decode('iso-8859-1'))
page = ET.parse('testFile.html')
