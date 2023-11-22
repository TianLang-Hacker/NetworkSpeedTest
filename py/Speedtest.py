import speedtest
import datetime

def measure_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps
    return download_speed, upload_speed

def export_to_log(download_speed, upload_speed):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - Download Speed: {download_speed:.2f} Mbps, Upload Speed: {upload_speed:.2f} Mbps\n"
    
    with open("speedtest_log.txt", "a") as log_file:
        log_file.write(log_entry)

if __name__ == "__main__":
    download_speed, upload_speed = measure_speed()
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

    export_to_log(download_speed, upload_speed)
    print("Results exported to speedtest_log.txt")
    
