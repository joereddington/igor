#!/home/joereddington/env/bin/python
import numpy as np
import time
import matplotlib.pyplot as plt
import os

#Todo
#1 merge this with the other graph files - make a class that records the source, destination, and time period and then works. 


SOURCE= "/Volumes/Crucial X8/git/igor/eqt.results.txt"
DEST = "/Volumes/Crucial X8/git/todo.txt/eqt.priority.png"
DAYS = 21
SMOOTHING=4

class ProductivityPlotter():
  "Class designed to take a Jurgen-formatted file and turn it into a graph"
  def __init__(self,source,dest,days):
    self.source=source
    self.dest=dest
    self.days=days

  def smooth(self,y, box_pts=SMOOTHING):
      box = np.ones(box_pts)/box_pts
      y_smooth = np.convolve(y, box, mode='same')
      return y_smooth#from stackexcahnge

  def myround(self,x, base=24*3600):
      return int(base * round(float(x)/base))

  def processFile(self):
    dayold, weekold,threedayold,seconds,now=([],[],[],[],[])
    count=0
    with open(self.source) as file: 
      lastrawline="Hello"
      rawline = file.readline()
      #the array we have is going to be horizonal when we need vertical. So we have to deal with that. 
      for rawline in file:
        splitline=rawline.split(',')
        dayold.insert(0,int(splitline[3]))
        threedayold.insert(0,int(splitline[4]))
        weekold.insert(0,int(splitline[5]))
        seconds.insert(0,int(splitline[2]))
        now.insert(0,int(splitline[0]))
        count=count+1 
    return (seconds,now,dayold,threedayold,weekold)

  def graph(self,seconds,now, dayold, threedayold,weekold):
    dis=4*24*60*60
    x = np.array(seconds[-dis:])
    ynow  = self.smooth(np.array(now))
    yday  = self.smooth(np.array(dayold))
    y3day = self.smooth(np.array(threedayold))
    yweek = self.smooth(np.array(weekold))
    plt.figure(dpi=150)    
    plt.plot(x,ynow, 'blue')
    plt.plot(x,yday, 'green')
    plt.plot(x,y3day,'purple')
    plt.plot(x,yweek, 'red')
    currenttime=int(seconds[0])
    lastweek=self.myround(currenttime-self.days*24*3600)
    plt.xlim(lastweek, currenttime-10)
    plt.ylim(top=100, bottom=0)
    ticks=np.arange(lastweek,currenttime,24*3600)
    plt.ylabel('Size of list', fontsize=12)
    plt.xlabel('Day', fontsize=12)
    plt.xticks(fontsize=6)
    plt.rc('font', family='serif', size=20)   
    labels=[time.strftime("%a", time.gmtime(x)) for x in ticks]
    plt.xticks(ticks,labels)
    plt.grid()
    plt.savefig(self.dest)

  def get_graph(self):
    a=self.processFile()
    self.graph(a[0],a[1],a[2],a[3],a[4])
    print("%s written with output from %s"%(self.dest, self.source))

if __name__ == "__main__":
    SOURCE= "/Volumes/Crucial X8/git/igor/eqt.results.txt"
    DEST = "/Volumes/Crucial X8/git/todo.txt/eqt.priority.png"
    a=ProductivityPlotter(SOURCE,DEST,DAYS)
    a.get_graph()
    SOURCE= "/Volumes/Crucial X8/git/igor/results.txt"
    DEST = "/Volumes/Crucial X8/git/todo.txt/priority.png"
    a=ProductivityPlotter(SOURCE,DEST,DAYS)
    a.get_graph()


