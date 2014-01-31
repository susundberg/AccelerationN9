
class AccelerationData:

   def __init__(self):
   
      self.filtered_limit       = 60   # number of times_limit
      self.filtered_data_min    = [0] * self.filtered_limit
      self.filtered_data_max    = [0] * self.filtered_limit
      self.filtered_data_mean   = [0] * self.filtered_limit
      self.filtered_current     = 0
      
      
      self.curr_last        = 9.81
      self.curr_min         = 0.0
      self.curr_max         = 0.0
      self.curr_mean        = 0.0
      self.curr_n           = 0
      
      self.scale_max        = 20
           
      self.times_limit   = 250*1000 # use 0.25s sampling time
      self.times_sum     = 0
   
   #
   # Add new datapoint
   #
   def add_data( self, add_data, timediff ):

      if ( timediff < 0 ):
         return False

      diff = add_data - self.curr_last
      self.curr_last = add_data
      
      if ( diff > self.curr_max ):
         self.curr_max = diff
      if ( diff < self.curr_min ):
         self.curr_min = diff
         
      self.curr_mean = self.curr_mean + diff
      self.curr_n = self.curr_n + 1
      
     # print "add of %f" % add_data + " (%f) " % diff + " %d " % timediff  
     # print self.curr_mean
     # print self.curr_max
     # print self.curr_n
     # print "----"
      
       
      # Check if this contributes to new point
      self.times_sum = self.times_sum + timediff
      # print "add %d " % self.times_sum + " this %d " % timediff
      
      if ( self.times_sum > self.times_limit ):
         # print " ----- new datapoint -----"
         self.times_sum = 0
         self.filtered_data_min  [ self.filtered_current ]  = self.curr_min
         self.filtered_data_max  [ self.filtered_current ]  = self.curr_max
         self.filtered_data_mean [ self.filtered_current ]  = self.curr_mean / self.curr_n
         
         # reset currents
         self.curr_min  = 0
         self.curr_max  = 0
         self.curr_mean = 0
         self.curr_n    = 0
         
         # move ring buffer pointer forward
         self.filtered_current = self.filtered_current + 1
         if ( self.filtered_current >= self.filtered_limit ):
            self.filtered_current = 0
         
         return True
         
      return False   
              
   def print_me(self):
     for loop in range(0, self.filtered_limit-1):
        print "value(%d) = " % loop + " %f " % self.filtered_data_min[ loop ] \
                                    + " %f " % self.filtered_data_max[ loop ] \
                                    + " %f " % self.filtered_data_mean[ loop ]  


