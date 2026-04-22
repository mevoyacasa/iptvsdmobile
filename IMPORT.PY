import os

# ===================== 核心配置 =====================
# 图片根目录
ROOT_FOLDER = r"E:\Git\iptvsdmobile\iptvsdmobile\tvglogo"
# Gitee 基础链接
BASE_LINK = "https://gitee.com/mevoyacasa/iptv/raw/master/tvglogo/"
# 输出文件
OUTPUT_FILE = "list.ini"
# 测试数量：10个（验证后改9999生成全部）
TEST_LIMIT = 9999
# 图片格式过滤
IMAGE_TYPES = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
# ===================================================

file_count = 0

# 写入文件（UTF-8编码，中文不乱码）
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    # 遍历所有子文件夹
    for current_dir, _, file_list in os.walk(ROOT_FOLDER):
        for file_name in file_list:
            # 过滤图片文件
            if file_name.lower().endswith(IMAGE_TYPES):
                if file_count >= TEST_LIMIT:
                    break
                
                file_count += 1
                # 提取频道名（去掉后缀）
                channel_name = os.path.splitext(file_name)[0]
                # 生成相对路径
                full_path = os.path.join(current_dir, file_name)
                relative_path = os.path.relpath(full_path, ROOT_FOLDER)
                # 路径符转换 \ → /
                relative_path = relative_path.replace("\\", "/")
                # 拼接链接
                full_link = BASE_LINK + relative_path
                
                # ✅ 关键修复：全部使用【英文半角符号】
                write_line = f"{file_count}.{channel_name}: {full_link},\n"
                f.write(write_line)
        if file_count >= TEST_LIMIT:
            break

print(f"执行完成！成功生成 {file_count} 条记录")
print(f"文件保存位置：{os.path.abspath(OUTPUT_FILE)}")