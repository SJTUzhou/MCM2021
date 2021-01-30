import pandas as pd 

df = pd.read_csv('zjy/task2_1.csv', header = None)

top10_seletion = ['新港_南沙', '营口_南沙', '营口_宁波', '钦州_宁波', '营口_福清', '营口_钦州', '上海_烟台', '日照_铁山', '上海_武汉', '乐从_营口']

for seletion in top10_seletion:

    df1 = df.loc[df[12] == seletion]

    SVVD_list = pd.unique(df1[4])
    svvd_num = len(SVVD_list)
    global tmp_large
    global tmp_small
    tmp_large = pd.DataFrame()
    tmp_small = pd.DataFrame()
    svvd_info_small = pd.DataFrame()
    svvd_info_large = pd.DataFrame()

    for svvd in SVVD_list:
        same_svvd = df1.loc[df1[4] == svvd]
        num = len(same_svvd)
        if num > 100:
            same_time_svvd = pd.to_datetime(same_svvd[1])
            time_list = pd.unique(same_time_svvd)
            time_counts = same_time_svvd.value_counts(sort=False)
            # 提前了几天
            time_before = time_list[-1] - time_list
            time_before_days = time_before.astype('timedelta64[D]').astype(int)
            svvd_info_large = pd.concat([pd.DataFrame(time_counts).reset_index(),pd.DataFrame(time_before_days)], axis=1)
            svvd_info_large.rename({'index':'date', 1: 'count', 0:'before'}, axis=1, inplace=True)
            before_list = pd.unique(svvd_info_large['before'])
            sum_s_list=[]
            for i in before_list:
                s = svvd_info_large.loc[svvd_info_large['before'] == i]
                sum_s = s['count'].sum()
                sum_s_list.append(sum_s)
                #tmp = pd.DataFrame({'count': [sum_s], 'before_days': [i])
            svvd_info_large = pd.DataFrame({'count': sum_s_list, 'before_days': before_list})
            #svvd_info_large.set_index('before')
            #svvd_info_large.rename_axis(svvd, axis=1, inplace=True)
            svvd_info_large['SVVD'] = svvd
            #svvd_info_large.set_index('before_days')

        else:
            same_time_svvd = pd.to_datetime(same_svvd[1])
            time_list = pd.unique(same_time_svvd)
            time_counts = same_time_svvd.value_counts(sort=False)
            # 提前了几天
            time_before = time_list[-1] - time_list
            time_before_days = time_before.astype('timedelta64[D]').astype(int)
            svvd_info_small = pd.concat([pd.DataFrame(time_counts).reset_index(),pd.DataFrame(time_before_days)], axis=1)
            svvd_info_small.rename({'index':'date', 1: 'count', 0:'before'}, axis=1, inplace=True)
            before_list = pd.unique(svvd_info_small['before'])
            sum_s_list=[]
            for i in before_list:
                s = svvd_info_small.loc[svvd_info_small['before'] == i]
                sum_s = s['count'].sum()
                sum_s_list.append(sum_s)
            svvd_info_small = pd.DataFrame({'count': sum_s_list, 'before_days': before_list})
            svvd_info_small['SVVD'] = svvd
            #svvd_info_small.set_index('before_days')

        tmp_large = pd.concat([tmp_large, svvd_info_large])
        tmp_small = pd.concat([tmp_small, svvd_info_small])
        #tmp_large['PORT'] = 'str(seletion)'

        

    large_count = tmp_large.groupby(by='before_days')['count'].sum()
    #small_count = tmp_small.groupby(by='before_days')['count'].sum
        
            


            
        
