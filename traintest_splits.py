import os

dir_path = 'D:/share_file/tsn/hdb_frames'
splits_path = 'D:/share_file/tsn/splits_file'
tmp = []
for file_name in os.listdir(splits_path):
    if 'split1' in file_name:
        with open(os.path.join(splits_path,file_name),'r+') as f:
            for x in f:
                tmp.append(x.strip().split(' '))
        train_list = [item[0].rstrip('.avi') for item in tmp if int(item[1]) == 1]
        test_list = [item[0].rstrip('.avi') for item in tmp if int(item[1]) == 2]
        val_list = [item[0].rstrip('.avi') for item in tmp if int(item[1]) == 0]
        with open('./trainpath.txt','a') as f:
            for line in sorted(train_list):
                f.write(line+'\n')
label = -1;                      
for file_name in os.listdir(dir_path):
    label += 1
    class_path=os.path.join(dir_path,file_name)
    for video_name in os.listdir(class_path):
        if video_name in train_list:
            video_path_train = os.path.join(class_path,video_name);
            num = len(os.listdir(video_path_train));
            with open('./train.txt','a') as f:
                f.write(os.path.join(class_path,video_name)+' '+str(num)+' '+str(label)+'\n');
            print('train');
        elif video_name in test_list:
            video_path_test = os.path.join(class_path,video_name);
            num = len(os.listdir(video_path_test));
            with open('./test.txt','a') as f:
                f.write(os.path.join(class_path,video_name)+' '+str(num)+' '+str(label)+'\n');
            print('test');
        else:
            video_path_val = os.path.join(class_path,video_name);
            num = len(os.listdir(video_path_val));
            with open('./val.txt','a') as f:
                f.write(os.path.join(class_path,video_name)+' '+str(num)+' '+str(label)+'\n');
            print('val');