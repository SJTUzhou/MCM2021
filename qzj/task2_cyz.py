import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('zjy/task2_1.csv', header = None)

top10_seletion = ['新港_南沙', '营口_南沙', '营口_宁波', '钦州_宁波', '营口_福清', '营口_钦州', '上海_烟台', '日照_铁山', '上海_武汉', '乐从_营口']
tmp_2 = pd.DataFrame()
ave_AMT_list = []
sales_volume_list = []
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
    tmp_1 = pd.DataFrame()

    figurename = 'qzj/cyz_thoughts/' + seletion+'.png'

    for svvd in SVVD_list:
        same_svvd = df1.loc[df1[4] == svvd]
        num = len(same_svvd)

        same_time_svvd = pd.to_datetime(same_svvd[1])
        time_list = pd.unique(same_time_svvd)
        time_list_2 = pd.unique(same_svvd[1])
        time_counts = same_time_svvd.value_counts(sort=False)
        time_counts = time_counts.sort_index()

        for times in time_list_2:
            times_df = same_svvd[same_svvd[1].isin([times])]
            darry = pd.to_numeric(pd.unique(times_df[5]))
            sales_volume_list.append(len(times_df))
            ave_AMT_list.append(darry[0])
            #print(times)

        #AMT_count = same_svvd[5]
        #AMT_count_list = pd.unique(AMT_count)
        # 提前了几天
        time_before = time_list[-1] - time_list
        time_before_days = time_before.astype('timedelta64[D]').astype(int)
        svvd_info_large = pd.concat([pd.DataFrame(time_before_days), pd.DataFrame(ave_AMT_list), pd.DataFrame(sales_volume_list)], axis=1)
        svvd_info_large.columns = ['before', 'ave_AMT', 'sales_volume']
        #svvd_info_large.rename({'index':'date', 1: 'count', 0:'before'}, axis=1, inplace=True)
        before_list = pd.unique(svvd_info_large['before'])
        sum_s_list=[]
        total_sales_list=[]
        for i in before_list:
            s = svvd_info_large.loc[svvd_info_large['before'] == i]
            total_sales = s['sales_volume'].sum()
            total_sales_list.append(total_sales)
            sum_s = s['ave_AMT'].mean()
            sum_s_list.append(sum_s)
            #tmp = pd.DataFrame({'count': [sum_s], 'before_days': [i])
        svvd_info_large = pd.DataFrame({'ave_AMT': sum_s_list, 'before_days': before_list, 'sales_volume':total_sales_list})
        #svvd_info_large.set_index('before')
        #svvd_info_large.rename_axis(svvd, axis=1, inplace=True)
        #svvd_info_large['SVVD'] = svvd
        #svvd_info_large.set_index('before_days')
        #tmp_large = pd.concat([tmp_large, svvd_info_large])
        #large_count = tmp_large.groupby(by='before_days')['count'].sum()/svvd_num
        #df2 = pd.DataFrame({'before_days':large_count.index, 'average_count': large_count.values})
        df2 = svvd_info_large
        df2['num'] = 'large'
        #filename = 'qzj/habbits/' + seletion+'_large.csv'
        
        #ax = df2.plot(x='before_days',y='average_count',color='DarkBlue',xlim=[0,14])
        #ax.set_ylabel('Average Container Quantity')
        #ax.set_xlabel('Days Before Sailing')
        #fig = ax.get_figure()
        #fig.savefig(figurename)
        #df2.to_csv(filename)

        '''
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
            tmp_large = pd.concat([tmp_large, svvd_info_large])
            large_count = tmp_large.groupby(by='before_days')['count'].sum()/svvd_num
            df2 = pd.DataFrame({'before_days':large_count.index, 'average_count': large_count.values})
            df2['num'] = 'large'
            #filename = 'qzj/habbits/' + seletion+'_large.csv'
            figurename = 'qzj/habbits/' + seletion+'_large.png'
            ax = df2.plot(x='before_days',y='average_count',color='DarkBlue')
            ax.set_ylabel('Average Container Quantity')
            ax.set_xlabel('Days Before Sailing')
            fig = ax.get_figure()
            fig.savefig(figurename)
            #df2.to_csv(filename)

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
            tmp_small = pd.concat([tmp_small, svvd_info_small])
            small_count = tmp_small.groupby(by='before_days')['count'].sum()/svvd_num
            df2 = pd.DataFrame({'before_days':small_count.index, 'average_count': small_count.values})
            df2['num'] = 'small'
            #filename = 'qzj/habbits/' + seletion+'_small.csv'
            figurename = 'qzj/habbits/' + seletion+'_small.png'
            ax = df2.plot(x='before_days',y='average_count',color='DarkBlue')
            ax.set_ylabel('Average Container Quantity')
            ax.set_xlabel('Days Before Sailing')
            fig = ax.get_figure()
            fig.savefig(figurename)
            #df2.to_csv(filename)

        '''    
        
        df2['SVVD'] = svvd
        tmp_1 = pd.concat([tmp_1, df2])
        #print(1)
    tmp_1['FLOW'] = seletion
    tmp_2 = pd.concat([tmp_2,tmp_1])

    ax = tmp_1.plot.scatter(x='sales_volume',y='ave_AMT',color='DarkBlue')
    ax.set_ylabel('Freight Rate Per Day')
    ax.set_xlabel('Sales Volume Per Day')
    fig = ax.get_figure()
    fig.savefig(figurename)
    #tmp_1.to_csv(filename)

tmp_2.to_csv('qzj/cyz_thoughts/final.csv')


        
        
            


            
        
