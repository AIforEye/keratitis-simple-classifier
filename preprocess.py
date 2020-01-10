import os
import numpy as np
import cv2


labels = ['bacterial', 'fungal', 'viral']


with open('labels.csv', 'w') as f:
	for l in range(len(labels)):
		label = labels[l]
		patients = os.listdir(label)
		for p in patients:
			img_name = os.listdir(os.path.join(label,p))[0]
			img = cv2.imread(os.path.join(label, p, img_name))
			img = cv2.resize(img, (300,200))
			cv2.imwrite(os.path.join('images_preprocessed', p + '.jpg'), img)
			f.write('%s.jpg,%s\n' % (p, l))


