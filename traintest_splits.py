import os
class TrainTestSplits(object):
    def __init__(self, dir_path,splits_path,splits_num):
        self.dir_path = dir_path
        self.splits_path = splits_path
        self.splits_num = splits_num
    def splits_list(self,splits_path,splits_num):
        tmp = []
        for file_name in sorted(os.listdir(splits_path)):
            if splits_num in file_name:
                with open(os.path.join(splits_path,file_name),'r+') as f:
                    for x in f:
                        tmp.append(x.strip().split(' '))
                train_list = [item[0].rstrip('.avi') for item in tmp if int(item[1]) == 1]
                test_list = [item[0].rstrip('.avi') for item in tmp if int(item[1]) == 2]
                val_list = [item[0].rstrip('.avi') for item in tmp if int(item[1]) == 0]
                return train_list,test_list,val_list
    def get_list(self):
        label = -1;    
        splitlist = self.splits_list(self.splits_path,self.splits_num)           
        for file_name in sorted(os.listdir(self.dir_path)):
            label += 1
            class_path=os.path.join(dir_path,file_name)
            for video_name in sorted(os.listdir(class_path)):
                if video_name in splitlist[0]:
                    video_path_train = os.path.join(class_path,video_name);
                    num = len(os.listdir(video_path_train));
                    with open('./train_'+self.splits_num+'.txt','a') as f:
                        f.write(file_name+'/'+video_name+' '+str(num)+' '+str(label)+'\n');
                elif video_name in splitlist[1]:
                    video_path_test = os.path.join(class_path,video_name);
                    num = len(os.listdir(video_path_test));
                    with open('./test_'+self.splits_num+'.txt','a') as f:
                        f.write(file_name+'/'+video_name+' '+str(num)+' '+str(label)+'\n');
                else:
                    video_path_val = os.path.join(class_path,video_name);
                    num = len(os.listdir(video_path_val));
                    with open('./val_'+self.splits_num+'.txt','a') as f:
                        f.write(file_name+'/'+video_name+' '+str(num)+' '+str(label)+'\n');
dir_path = 'D:/share_file/tsn/hdb_frames'
splits_path = 'D:/share_file/tsn/splits_file'
splits_num = 'split3'
traintestsplits  = TrainTestSplits(dir_path,splits_path,splits_num)
traintestsplits.get_list()