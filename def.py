def 发送邮件(内容)
    #发送邮件提醒
    连接邮箱服务器
    发送邮件
    关闭连接
     
while True：
     
    if cpu利用率 > 90%:
        发送邮件('CPU报警')
     
    if 硬盘使用空间 > 90%:
        发送邮件('硬盘报警')
     
    if 内存占用 > 80%:
        发送邮件('内存报警')