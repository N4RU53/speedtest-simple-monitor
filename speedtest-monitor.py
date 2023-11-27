import speedtest 
import sys
import datetime

def get_speed_test():
    servers = []
    stest = speedtest.Speedtest(secure=True)
    stest.get_servers(servers)
    stest.get_best_server()
    return stest

def command_line_runner(cnt):
    stest = get_speed_test()
    down_result = stest.download()
    up_result = stest.upload()
    mbps_down_result = int(down_result / 1024 /1024)
    mbps_up_result = int(up_result / 1024 /1024)
    print(' (' + datetime.datetime.now().strftime('%H:%M:%S') + ')', end='')
    print('[COUNT' + str(cnt) + '] ' + 'DOWNLOAD: ' + str(mbps_down_result) + ' Mbps' + ',  UPLOAD: ' + str(mbps_up_result) + ' Mbps')
    return mbps_down_result, mbps_up_result

if __name__ == '__main__': 
    
    print('\nStarting Speedtest monitoring')
    print('Press (ctrl + c) to stop monitoring\n')
    print('-------------------------------------------------------------')
    cnt = 1
    down_sum = 0
    up_sum = 0
    
    while True:
        try:
            down, up = command_line_runner(cnt)
            cnt += 1
            down_sum += down
            up_sum += up
        except KeyboardInterrupt:
            try:
                down_ave = int(down_sum/(cnt-1))
                up_ave = int(up_sum/(cnt-1))
                print('\n' + ' DOWNLOAD_AVERAGE: ' + str(down_ave) + ' Mbps' + '\n UPLOAD_AVERAGE  : ' + str(up_ave) + ' Mbps')
                print('-------------------------------------------------------------')
                input('\nPress any key to exit this program...')
                sys.exit()
            except ZeroDivisionError:
                input('\nPress any key to exit this program...')
                sys.exit()