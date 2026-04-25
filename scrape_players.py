import json
import time

def scrape():
    # 模拟数据
    new_data = [
        {"name": "s1mple", "team": "NAVI", "cont": "Europe", "country": "Ukraine", "age": 26, "role": "AWPer", "majors": 12},
        {"name": "NiKo", "team": "G2", "cont": "Europe", "country": "Bosnia", "age": 27, "role": "Rifler", "majors": 11},
        # 加入这一行，记录更新时间
        {"_last_updated": time.strftime("%Y-%m-%d %H:%M:%S")}
    ]
    
    with open('players.json', 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
    print("题库已成功写入文件！")

if __name__ == "__main__":
    scrape()
