import os
dir_path = 'D:/share_file/act_reg/UCF101_n_frames'
splits_path = './trainlist01.txt'
tmp = []
with open(splits_path,'r+') as f:
    for x in f:
        tmp.append(x.strip().split(' '))
train_list = [item[0].rstrip('.avi') for item in tmp]

label = -1;    
for file_name in sorted(os.listdir(dir_path)):
    label += 1
    class_path=os.path.join(dir_path,file_name)
    for video_name in sorted(os.listdir(class_path)):
        video_path = os.path.join(file_name,video_name)
        if video_path in train_list:
            video_path_train = os.path.join(class_path,video_name)
            num = len(os.listdir(video_path_train))
            with open('./ucf101_train_split1.txt','a') as f:
                f.write(video_path+' '+str(num)+' '+str(label)+'\n');