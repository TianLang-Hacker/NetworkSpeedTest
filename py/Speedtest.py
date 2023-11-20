import speedtest

def test_speed():
    st = speedtest.Speedtest()
    
    # 获取下载速度
    download_speed = st.download() / 10**6  # 转换为兆比特每秒（Mbps）
    
    # 获取上传速度
    upload_speed = st.upload() / 10**6  # 转换为兆比特每秒（Mbps）
    
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    print("Running Speed Test...")
    test_speed()
