*threading.active_count()：回傳目前仍活著的thread的數量
*threading.current_thread()：回傳目前的thread
*threading.get_ident()：回傳目前thread的識別碼 (identifier)
*threading.enumerate()：回傳目前活著的所有thread的清單
*threading.main_thread()：回傳主thread(main thread)，通常是Python開始編譯的那個
*threading.settrace(func)：設定一個追蹤函式 (trace function)
*threading.setprofile(func)：設定一個個資函式 (profile function)
*threading.stack_size([size])：當創立新的thread，回傳堆疊大小 (stack size)
*threading.TIMEOUT_MAX：允許阻塞函式的超時參數的最大數量 (The maximum value allowed for the timeout parameter of blocking functions)  e.g. Lock.acquire(), RLock.acquire(), Condition.wait(), etc.

>class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
>>    start()：啟動thread的活動
>>    run()：表示thread活動的方法
>>    join(timeout=None)：等待thread終止
>>    name：名稱
>>    getName()：取得名稱
>>    setName()：設定名稱
>>    ident：識別碼
>>    is_alive()：回傳thread是否活著
>>    daemon：布林值，說明這個thread是否為常駐程式的設定值
>>    isDaemon()：是否為常駐程式
>>    setDaemon()：設定為常駐程式

>class threading.Lock
>>    acquire(blocking=True, timeout=-1)：取得鎖定、阻塞、非阻塞
>>    release()：釋放鎖定 (可以從別的thread呼叫)

>class threading.Condition(lock=None)
>>    acquire(*args)
>>    release()
>>    wait(timeout=None)：等待通知或直到超時發生為止
>>    wait_for(predicate, timeout=None)：等待直到條件成立
>>    notify(n=1)：通知n個thread
>>    notify_all()：通知全部的thread

>class threading.Event
>>    is_set()：只在內部標籤為true的時候回傳true
>>    set()：使其處於激發狀態
>>    clear()：使其回到未激發狀態
>>    wait(timeout=None)：直到內部標籤為是之前進行阻塞

>class threading.Timer(interval, function, args=None, kwargs=None)
>>    cancel()：停止計時器
