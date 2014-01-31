
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *

from AccelerationData import * 

class AccelerationGraph (QDeclarativeItem):
  
  def __init__(self, parent = None):
    QDeclarativeItem.__init__(self, parent)
    # need to disable this flag to draw inside a QDeclarativeItem
    self.setFlag(QGraphicsItem.ItemHasNoContents, False)
    self.data   = AccelerationData()
    self.color_green = QColor("green")
    self.color_red   = QColor("red") 
    self.color_black = QColor("black")
    self.color_gray  = QColor("gray")
    
  #This function creates the whole graph
  def paint(self, paint, options, widget):
    paint.setRenderHints(QPainter.Antialiasing, True);

    ysize  = self.height()
    xsize  = self.width()

    paint.setBrush( self.color_black )
    paint.setPen( self.color_black )
    paint.drawRect( 0,0,xsize,ysize )
        
    paint.setBrush( self.color_red )
    paint.setPen( self.color_green )
    #paint.setFont(QFont('Decorative', 12))

    limit  = self.data.filtered_limit
    
    offset = ysize/2.0 
    yscale = ysize / (2.0*self.data.scale_max)
    xscale = xsize / limit
    
    
    
    #paint.drawRect(0,0,xsize,ysize)
    # print " ---------------------------------- "
    for loop in range(0, limit ):
       ind = (self.data.filtered_current + loop)
       
       if ( ind >= limit ):
          ind = ind - limit
       
       rec_x_low  = loop*xscale
       rec_x_size = xscale
       
       data_min  = self.data.filtered_data_min [ ind ]
       data_max  = self.data.filtered_data_max [ ind ]
       data_mean = self.data.filtered_data_mean[ ind ] 
       
       rec_y_low  = offset + data_min*yscale
       rec_y_size = ( data_max - data_min )*yscale
       
       # print "min %f " % data_min + " max %f " % data_max + " mean %f " % data_mean
       data_mean = data_mean*yscale + offset
              
       paint.drawRect( rec_x_low , rec_y_low, rec_x_size, rec_y_size )
       paint.drawLine( rec_x_low , data_mean, rec_x_low + rec_x_size, data_mean )
       
    
  def add_data( self, acc, stamp ):
    if ( self.data.add_data(acc, stamp ) == True):
       self.update()
    
    
    
