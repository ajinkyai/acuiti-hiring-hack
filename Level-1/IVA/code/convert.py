import datetime
import os
import os.path
import subprocess
RELPATH = '../input/IVA/'
os.chdir(RELPATH)

dirs = [name for name in os.listdir('.') if os.path.isdir(name)]
dates = sorted(dirs, key=lambda datestr: ''.join(reversed(datestr.split('.'))));
filepaths = []
for date in dates:
	filepaths = filepaths + sorted([os.path.join(date, name) for name in os.listdir(date) if os.path.isdir(os.path.join(date, name))])

# convert to mp4
for path in filepaths:
	path = path.replace('\\', '/')
	subprocess.call('ffmpeg -i "{ipath}" -c:v libx264 -c:a copy "{opath}"'.format(ipath=os.path.join(path, 'archive.iva'),opath=os.path.join(path, 'o.mp4')))

# write output filenames to txt file
paths = [os.path.join(path,'o.mp4').replace('\\', '/') for path in filepaths]
with open('opfiles.txt', 'w') as fp:
	for path in paths:
		fp.write('file {path}\n'.format(path=path))	

cmd = 'ffmpeg -f concat -i opfiles.txt -c copy output.mp4'
subprocess.call(cmd)
