import subprocess
import webiopi

def setup():
	subprocess.call('/home/pi/drover/videostream/start_stream.sh', shell=True)

def destroy():
	subprocess.call('/home/pi/drover/videostream/stop_stream.sh', shell=True)