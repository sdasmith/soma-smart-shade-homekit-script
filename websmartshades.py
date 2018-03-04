#!/usr/bin/env python
import web
import subprocess

urls = (
    '/getbattery/(.*)', 'get_battery',
    '/getposition/(.*)', 'get_position',
    '/getstate/(.*)', 'get_state',
    '/moveup/(.*)', 'move_up',
    '/movedown/(.*)', 'move_down',
    '/setposition/(.*)/(.*)', 'set_position'
)

app = web.application(urls, globals())

class get_battery:        
    def GET(self, mac):
        output = subprocess.check_output(['/usr/bin/python','./control.py', '-t', mac, '-c', 'get_battery'])
        return output

class get_position:
    def GET(self, mac):
        output_string = subprocess.check_output(['/usr/bin/python','./control.py', '-t', mac, '-c', 'get_position'])
        output = output_string.replace("get_position ", "")
        return output

class get_state:
    def GET(self, mac):
        output = '2'
        return output
        
class move_down:
    def GET(self, mac):
        output = subprocess.check_output(['/usr/bin/python','./control.py', '-t', mac, '-c', 'move_down'])
        return ""

class move_up:
    def GET(self, mac):
        output = subprocess.check_output(['/usr/bin/python','./control.py', '-t', mac, '-c', 'move_up'])
        return ""

class set_position:
    def GET(self, mac, position):
	    inverse_position = unicode(100 - int(position))
	    if position == "STATE":
	    	return '2'
	    else:
		return subprocess.check_output(['/usr/bin/python','./control.py', '-t', mac, '-c', 'move_target', '-a', inverse_position])


if __name__ == "__main__":
    app.run()