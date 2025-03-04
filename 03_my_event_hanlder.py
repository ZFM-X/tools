import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileChangeHandler(FileSystemEventHandler):
    """
    事件处理器
    """
    def on_modified(self, event):
        # 当文件被修改时触发此方法
        if not event.is_directory:
            print(f'文件 {event.src_path} 被修改')
            
    def on_deleted(self, event):
        # 当文件被修改时触发此方法
        if not event.is_directory:
            print(f'文件 {event.src_path} 被删除')
            
if __name__ == "__main__":
    path_to_monitor = r'E:\study\1'  # 这里可以将 '.' 替换为你要监控的实际目录路径
    event_handler = FileChangeHandler()
    observer = Observer()

    observer.schedule(event_handler, path_to_monitor, recursive=True)
    observer.start()  # 启动观察者

    try:
        while True:
            time.sleep(1)  # 保持程序运行，持续监听
    except KeyboardInterrupt:
        observer.stop()  # 按 Ctrl+C 停止监听

    observer.join()  # 等待观察者线程结束