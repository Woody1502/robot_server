import os
def crc_sum(tcp_bytes,crc):
    
    count=0
    for i in range(len(tcp_bytes)):
        if tcp_bytes[i]!=48:
            count+=tcp_bytes[i]
    return count==(crc+1)
def port_check():
    return os.path.exists('/media/firefly/FLASH' )
    #return os.path.ismount('/dev/sda1' )