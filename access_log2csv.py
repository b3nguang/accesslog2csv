import csv
from urllib.parse import unquote

def convert_to_csv(log_file, csv_file):
    with open(log_file, 'r', encoding='utf-8') as file:
        logs = file.readlines()

    with open(csv_file, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['ip', '时间', '方法', '访问的文件', '状态码', '字节', '浏览器信息'])
        
        for log in logs:
            log_parts = log.split('"')
            
            if len(log_parts) >= 6:
                ip = log.split("- -", 1)[0]
                time = log.split('[', 1)[1].split(']')[0]
                method = log_parts[1].split(' ')[0]
                document = unquote(log_parts[1].split(' ')[1])
                status_code = log_parts[2].strip().split(' ')[0]
                byte_size = log_parts[2].strip().split(' ')[1]
                user_agent = log_parts[5]
                
                writer.writerow([ip, time, method, document, status_code, byte_size, user_agent])
            else:
                # 如果日志格式不符合预期，则在相应字段位置显示缺失值
                writer.writerow(['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'])

if __name__ == '__main__':
    log_file = 'access.log'
    csv_file = 'access.csv'
    convert_to_csv(log_file, csv_file)
