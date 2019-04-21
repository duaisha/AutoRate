
# coding: utf-8

# ## Compute Kappa for inter rater reliability

# ### Import Packages

# In[1]:


import os
import os.path
from os import listdir
from os import path
import numpy as np
import pandas as pd


# ### Plot graph

# In[19]:


def plot_bar(data, xlab, ylab, bars, colors, figname):
    
    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(10,6))
    index = np.arange(len(bars))
    bar1 = plt.bar(index, data, color=colors)

    # Add counts above the two bar graphs
    for rect in bar1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width()/2.0, height, '%d' % int(height), ha='center', va='bottom',fontsize = 15 )

    
    plt.xticks(index + 0.5, bars, fontsize = 15)
    plt.xlabel(xlab, fontsize = 20)
    plt.ylabel(ylab, fontsize = 20)
    plt.savefig(figname)


# In[3]:


def compute_kappa(data):
    
    k = 0; i = 0; diag_s = 0; prand_sum =0
    freq  = np.zeros((5,5))
    
    for k in range(len(data)):
        #print(int(data1[k,1]-1),int(data1[k,2]-1))
        freq[ int(data[k,0]-1), int(data[k,1]-1)] += 1
    print(freq)
    
    
    for i in range(5):
        diag_s += freq[i,i]
        pobs = diag_s/len(data)
        
    csum = np.sum(freq, axis =0)
    rsum = np.sum(freq, axis =1)
    prand = csum *rsum
    prand_sum = sum(prand)
    pexp = prand_sum/(len(data)*len(data))
    
    kappa = (pobs-pexp)/(1-pexp)
    return(kappa)


# In[4]:


def kappa(data1, n_raters):

    kappa_arr = []
    for i in range(n_raters):
        j = i+1
        while(j < n_raters):
            data2 = np.array([data1[:,i],data1[:,j]]).T
            kappa = compute_kappa(data2)
            kappa_arr.append(kappa)
            print("For combinations", i+1, j+1, "kappa is ", kappa)
            j = j+1
            print("\n")
            print("#########################################")
            print("\n")
            
        
        
    kappa_arr = np.array(kappa_arr)
    avg_kappa = np.mean(kappa_arr)
    print(kappa_arr)
    print("avg_kappa",avg_kappa)


# ### Old annotations

# In[5]:


data = pd.read_csv("driver_assistance_project/ordered_dataset/training.csv")
data1 = data.values[:,1:6]
#print(data1)
n_raters =5

kappa(data1, n_raters)


# ### New Annotations

# In[6]:


user1 = pd.read_csv("output_user1.csv", header = None).values[:,:2]
user2 = pd.read_csv("output_user2.csv", header = None).values[:,:2]
user3 = pd.read_csv("output_user3.csv", header = None).values[:,:2]
user4 = pd.read_csv("output_user4.csv", header = None).values[:,:2]
user5 = pd.read_csv("output_user5.csv", header = None).values[:,:2]
print(len(user1), len(user2), len(user3), len(user4), len(user5))




# In[7]:


### Data preprocessing

arr = []

for i in range(419):
    
    if(user1[i,0] == user2[i,0] and user2[i,0] == user4[i,0] and user4[i,0] == user5[i,0]):
        if(int(user1[i,1])!=0 and int(user2[i,1])!=0 and int(user5[i,1])!=0 and int(user4[i,1])!=0):
            temp = []
            temp = np.append(user1[i,0].replace('./data/training_ordered//', ''),user1[i,1])
            temp = np.append(temp, user2[i,1])
            temp = np.append(temp, user4[i,1])
            temp = np.append(temp, user5[i,1])

        
            #print(temp)
            arr.append(temp)
            #print(len(arr))  
    
#print(arr)
arr1 = arr
arr  = np.array(arr)[:,1:]
print(arr)
arr = arr.astype(int)
print(arr.shape)


# In[8]:


arr1 = np.array(arr1)
print (arr1)


# In[9]:


n_raters =4
kappa(arr, n_raters)


# In[10]:


mean = np.round(np.mean(arr, axis =1))
#print(mean)

std = np.std(arr, axis =1)
print(std)
#print(np.min(std), np.max(std))



distribution = np.concatenate(((mean).reshape(392,1),std.reshape(392,1)),axis =1)
#print(distribution)


# In[11]:


groundtruth = np.concatenate((arr,mean.reshape(392,1),std.reshape(392,1)), axis=1)
groundtruth.shape


# In[9]:



dir = listdir("video_anno")


len(dir)


# In[14]:



def convert_avi_to_mp4(avi_file_path, output_name):
    os.popen("ffmpeg -i '{input}' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 '{output}.mp4'".format(input = avi_file_path, output = output_name))
    return True

#dir = listdir("video_anno")

#for i in range(len(dir)):
 #   src_file = "video_anno/" + dir[i] 
  #  dest_file ="video_anno_mp4/" + (dir[i])[:-4]
   # convert_avi_to_mp4(src_file, dest_file)



# In[13]:

from shutil import copy

for i in range(len(arr1)):
    
    if(mean[i] == 1):
        src = "video_anno_mp4/" + (arr1[i,0])
        dst = "new_anno_score/score1/"
        
        
    elif(mean[i] == 2):
        src = "video_anno_mp4/" + (arr1[i,0])
        dst = "new_anno_score/score2/"
        
    elif(mean[i] == 3):
        src = "video_anno_mp4/" + (arr1[i,0])
        dst = "new_anno_score/score3/"
        
    elif(mean[i] == 4):
        src = "video_anno_mp4/" + (arr1[i,0])
        dst = "new_anno_score/score4/"
        
    elif(mean[i] == 5 ):
        src = "video_anno_mp4/" + (arr1[i,0])
        dst = "new_anno_score/score5/"
    
        
    print(src, dst)
    copy(src, dst)


from shutil import copy

for i in range(len(arr1)):
    
    if(std[i] == 0):
        src = "video_anno_mp4/" + (arr1[i,0])
        dst = "new_anno/0/"
        
        
    elif(std[i] > 0 and std[i] < 0.5):
        src = "video_anno_mp4/" + (arr1[i,0])
        dst = "new_anno/0_1-0_5/"
        
    elif(std[i] >= 0.5 and std[i] < 1):
        src = "video_anno_mp4/" + (arr1[i,0])
        dst = "new_anno/0_5-1/"
        
    elif(std[i] >= 1 and std[i] < 1.5):
        src = "video_anno_mp4/" + (arr1[i,0])
        dst = "new_anno/1-1_5/"
        
    elif(std[i] >= 1.5 ):
        src = "video_anno_mp4/" + (arr1[i,0])
        dst = "new_anno/1_5-2/"
    
        
    print(src, dst)
    copy(src, dst)


# In[14]:


np.savetxt('test.txt',groundtruth , delimiter=',')


# In[15]:


from collections import Counter
frequencies = Counter(mean)
print(frequencies[1.0])
freq = np.array([frequencies[1.0], frequencies[2.0], frequencies[3.0], frequencies[4.0], frequencies[5.0]])
freq


# In[16]:


bin1 = []; bin2 =[]; bin3 =[]; bin4 =[]

for i in range(len(distribution)):
    if(distribution[i,1] < 0.5):
        bin1.append(distribution[i,0])
         
    elif(distribution[i,1] >= 0.5 and distribution[i,1] < 1.0 ):
        bin2.append(distribution[i,0])
        
    elif(distribution[i,1] >= 1.0 and distribution[i,1] < 1.5 ):
        bin3.append(distribution[i,0])
        
    elif(distribution[i,1] >= 1.5):
        bin4.append(distribution[i,0])

bin1_count = Counter(bin1)
bin2_count = Counter(bin2)
bin3_count = Counter(bin3)
bin4_count = Counter(bin4)
print(bin1_count)
print(bin2_count)
print(bin3_count)
print(bin4_count)
       
bin1_count = np.array([bin1_count[1.0], bin1_count[2.0], bin1_count[3.0], bin1_count[4.0], bin1_count[5.0]])
bin2_count = np.array([bin2_count[1.0], bin2_count[2.0], bin2_count[3.0], bin2_count[4.0], bin2_count[5.0]])
bin3_count = np.array([bin3_count[1.0], bin3_count[2.0], bin3_count[3.0], bin3_count[4.0], bin3_count[5.0]])
bin4_count = np.array([bin4_count[1.0], bin4_count[2.0], bin4_count[3.0], bin4_count[4.0], bin4_count[5.0]])



# In[22]:



bars = ('Score1', 'Score2', 'Score3', 'Score4', 'Score5')
colors = ['black', 'red', 'green', 'blue', 'cyan']
print(freq)
plot_bar(freq, 'Attention Score', 'Number of Annotations', bars, colors, "distribution of score.jpg")


# In[23]:


bin_count = [np.sum(bin1_count), np.sum(bin2_count), np.sum(bin3_count) ,np.sum(bin4_count)]
print(bin_count)
bars = ('0 to 0.5', '0.5 to 1.0', '1.0 to 1.5', '1.5 to 2.0')
colors = [ 'red', 'green', 'blue', 'cyan']
plot_bar(bin_count, 'Range', 'Number of Annotations', bars, colors , "distribution of std deviation.jpg")

