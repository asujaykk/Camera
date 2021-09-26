# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:52:23 2020

@author: AKHIL_KK
"""
import cv2
import urllib3
#import json

class IPCam():
    active_camers = 0
    http = urllib3.PoolManager()
    def __init__(self,url):
        video = '/video'
#        save_af_photo = '/photoaf_save_only.jpg'
#        photo_af = '/photoaf.jpg'
#        photo = '/photo.jpg'

        self.url = url
        self.cap = cv2.VideoCapture(self.url+video)
        camera.active_camers +=1
   
    def get_frames(self):
        return(self.cap.read())
        
    def get_latest_frame(self):
        pic = '/shot.jpg'
        url_response= (camera.http.request('GET', self.url +pic))
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, -1)
        return img
    def zoom(self, zoom_value):
        zoom_max= 78
        zoom_min = 0
        zoom_inc = 0.01
        zoom_cam = '/ptz?zoom='
        if zoom_value >= zoom_min and zoom_value <= zoom_max:
            camera.http.request('GET', self.url + zoom_cam + str(zoom_value))
        elif zoom_value < zoom_min:
            return zoom_value - zoom_min
        else:
            return zoom_value - zoom_max
        return 0
    
    def quality(self, quality_val):
        qual_max =100
        qual_min = 0
        qual_inc = 1
        qual_cam = '/settings/quality?set='
        if quality_val >= qual_min and quality_val <= qual_max:
            camera.http.request('GET', self.url + qual_cam + str(quality_val))
        elif quality_val < qual_min:
            return quality_val - qual_min
        else:
            return quality_val - qual_max
        return 0
    

    def exposure(self, exp_val):
        expo_max = 12
        expo_min = -12
        expo_inc = 1
        expo_cam = '/settings/exposure?set='
        if exp_val >= expo_min and exp_val <= expo_max:
            camera.http.request('GET', self.url + expo_cam + str(exp_val))
        elif exp_val < expo_min:
            return exp_val - expo_min
        else:
            return exp_val - expo_max
        return 0
    
    def flash_on(self):
        torch_on = '/enabletorch'
        camera.http.request('GET', self.url + torch_on)
    
    def flash_off(self):
        torch_off = '/disabletorch'
        camera.http.request('GET', self.url + torch_off)
    
    def focus(self):
        focus = '/focus'
        camera.http.request('GET', self.url + focus)
        
    def nofocus(self):
        nofocus = '/nofocus'
        camera.http.request('GET', self.url + nofocus)
        
    def switch_to_front_cam(self):
        fron_cam = '/settings/ffc?set=on'
        camera.http.request('GET', self.url + fron_cam)
        
    def swicth_to_main_cam(self):
        main_cam = '/settings/ffc?set=off'
        camera.http.request('GET', self.url + main_cam)
     
    def sensor_data(self):
        sensor = '/sensors.json'
        return(camera.http.request('GET', self.url + sensor))
        
    def __del__(self):
        self.cap.release()




#from matplotlib import pyplot as plt 
#
#sens_out_dir = "sens_data\\"
#img_out_dir = "image_data\\"      
#cam1 = camera('http://192.168.43.1:8080')
#
#
#x1 =[]
#y1 =[]
#
#x2 =[]
#y2 =[]
#
#x3 =[]
#y3 =[]
#
#i=0
#x=0
#while (i<2000):

   #http_resp = cam1.sensor_data()
#   ret, frame = cam1.get_frames()
   #print(type(frame))
   #print (http_resp.data)
   #j_data= json.loads(http_resp.data)
   # with open(sens_out_dir+str(i)+".txt","w") as sensor_file:
   #      json.dump(j_data, sensor_file)
#   cv2.imwrite(img_out_dir+str(i)+".jpg",frame)
#   cv2.imshow('img',frame)
#   cv2.waitKey(1)
   #sensor_file.close()
   #sensor_list = j_data.keys()
   #print(sensor_list)
   #print(len(j_data['accel']['data']))
#   count =0 
#   i +=1
   #print(j_data['accel']['data'][count][1])
   
#   y1.append(j_data['accel']['data'][count][1][0])
#   y2.append(j_data['accel']['data'][count][1][1])
#   y3.append(j_data['accel']['data'][count][1][2])
#   x1.append(x)
#   plt.plot(x1,y1)
#   plt.plot(x1,y2)
#   plt.plot(x1,y3)
#   plt.show()
#   plt.pause(0.05)
#   x += 1
   #break


#cv2.destroyAllWindows()


#i = 0
#while i<1000:
#    
#    ret,frame1 = cam1.get_frames() 
#    cv2.imshow('cam1',frame1)
#    cv2.waitKey(1)
#    http_resp = cam1.sensor_data()
#    j_data= json.loads(http_resp.data)
#    print(j_data)
#    i += 1 
##j_acc_data = json.loads(j_data['accel'])
#
#cv2.destroyAllWindows()
# del cam1
#for sensor in sensor_list:
#    print(sensor)
#    print(j_data[sensor])






#print(type(j_data))

#print(j_data['data'])   

   
