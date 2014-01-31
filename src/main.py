

import sys
import platform
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *
from QtMobility.Sensors import *

from AccelerationGraph import * 
from math import sqrt

class AccelerometerFilter(QAccelerometerFilter):
    global qml_accgraph
    
    stamp = 0

    def filter(self, reading):
        diff = reading.timestamp() - self.stamp
        self.stamp = reading.timestamp()
	if diff:
#            print "Acceleration: %.2f x" % reading.x(), " %.2f y" % reading.y(), " %.2f z m/s^2" % reading.z(), " %.2f ms since last, " % (diff / 1000), " %.2f Hz" % (1000000.0 / diff)
            x = reading.x();
            y = reading.y();
            z = reading.z();

            qml_accgraph.add_data( sqrt( x*x + y*y + z*z ) , diff );
        else:
            print "Same diff"
            
        return False # don't store the reading in the sensor



if __name__ == '__main__':

    app = QApplication(sys.argv)


    sensor = QAccelerometer()
    #if rate_val > 0:
    #    sensor.setDataRate(rate_val)

    filter = AccelerometerFilter()
    sensor.addFilter(filter)
    sensor.setProperty("alwaysOn", True)

    #qmlRegisterType(NAME OF CLASS, 	QML IMPORT NAME, 	VERSION MAJOR, 	VERSION MINOR, 	COMPONENT NAME IN QML)
    qmlRegisterType(AccelerationGraph, 'myAccelerationGraph', 1, 0, 'AccelerationGraph')

    view = QDeclarativeView()
    view.setSource(QUrl.fromLocalFile('Main.qml'))

    root = view.rootObject()

    
    qml_accgraph = root.findChild(QObject,"myAccGraph")



    
    # instantiate the Python object
    # qml_to_python = QML_to_Python_Interface()
    # expose the object to QML
    context = view.rootContext()
    #context.setContextProperty("qml_to_python", qml_to_python)
    
    if(platform.machine().startswith('arm')): view.showFullScreen()
    view.show()
    
    sensor.start()
    if not sensor.isActive():
        qWarning("Accelerometersensor didn't start!")
        sys.exit(1)    
    
    
    sys.exit(app.exec_())
    
    
    
    
    
