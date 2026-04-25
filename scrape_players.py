import requests
import json

def scrape():
    # 这里你可以以后写复杂的 Liquipedia 爬虫逻辑
    # 暂时我们写一个简单的“数据补全”逻辑作为示例
    new_data = [
        {"name": "s1mple", "team": "NAVI", "cont": "Europe", "country": "Ukraine", "age": 26, "role": "AWPer", "majors": 12},
        {"name": "NiKo", "team": "G2", "cont": "Europe", "country": "Bosnia", "age": 27, "role": "Rifler", "majors": 11}
    ]
    
    # 写入文件
    with open('players.json', 'w', encoding='utf-8') as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
    print("题库已更新！")

if __name__ == "__main__":
    scrape()
