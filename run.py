"""测试任务运行说明

================================单进程启动================================
启动函数：run()
参数: 接收一个列表，pytest和arun支持的所有参数
Example：
run(["-s","-m demo","-e testing"])

================================多线程启动================================
启动函数：threads_run()           
参数：
    根据传入参数类型不同，启动不同的多线程分配模式
    list: dist-mark模式
    str：dist-file模式
    dict：dist-suite模式
多线程分配模式：
    1.dist-mark: 根据mark标记来分配线程，每个mark标记的线程独立运行
        example：
            threads_run(["-m demo1","-m demo2","-m demo3"])
            将启动三个子线程，分别执行标记为demo1,demo2,demo3的case
    2.dist-file: 根据测试文件来分配线程，每个文件下的case由独立线程运行
        example：
            threads_run({"path":"testcases/test_api"})
            testcases/test_api目录下有多少个测试文件，就启动多少个子线程来运行
    3.dist-suite: 根据测试套件来分配线程，每个套件下的case由独立的线程运行
        example：
            threads_run("testcases/test_api")
            testcases/test_api目录下有多少个测试套件，就启动多少个子线程来运行

================================多进程启动================================
****注意：windows下暂时不支持，linux和mac支持****
启动函数：processes_run()           
参数：
    根据传入参数类型不同，启动不同的多线程分配模式
    list: dist-mark模式
    str：dist-file模式
    dict：dist-suite模式
多线程分配模式：
    同多进程
=========================================================================
"""
from aomaker.cli import main_run

if __name__ == '__main__':
    main_run(env="mock", pytest_args=['-m mock_api'])