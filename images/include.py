import os
images=os.listdir()
out = []
for image in images:
	if image[-3:]!="jpg":
		continue
	out.append("![{}](/images/{})".format(image[:-4], image))

with open("outputfile.txt", 'w') as f:
	for o in out:
		f.write(o)
		f.write('\n')
f.closed
