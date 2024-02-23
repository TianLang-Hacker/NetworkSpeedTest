import speedtest
import datetime

def test_speed():    #测速功能
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # 转换成Mbps
    upload_speed = st.upload() / 10**6  # 转换成Mbps
    return download_speed, upload_speed

def export_to_log(download_speed, upload_speed):   #将测速得出的数据导出成.log文件
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") #内容第一句是日期时间
    log_entry = f"{timestamp} - 下载速度: {download_speed:.2f} Mbps, 上传速度: {upload_speed:.2f} Mbps\n"  #第二句为下载带宽数据和上传带宽数据
    
    with open("Speedtest.log", "a") as log_file:      #将文件输出成log文件输出文件名为：Speedtest.log
        log_file.write(log_entry)

if __name__ == "__main__":        #命令行环境下输出运行状态
    print("正在运行Speed Test...")
    test_speed()

    download_speed, upload_speed = test_speed()
    print(f"下载速度: {download_speed:.2f} Mbps")    #测速完成后将下载带宽结果输出到命令行上
    print(f"上传速度: {upload_speed:.2f} Mbps")      #测速完成后将上行带宽结果输出到命令行上

    export_to_log(download_speed, upload_speed)
    print("测速结果已经导出到speedtest.log")

# input()   #类似于按任意键退出程序（仅限Windows上的终端上（Windows Terminal）使用，在Linux上无需此代码。如果要打包成Linux的.deb文件，建议删掉这段代码）