import traceback

try:
    value = 8/0
except:
    # 使用traceback.format_exc()来捕获异常信息
    info = traceback.format_exc()
    print(info)
    print("value error")




