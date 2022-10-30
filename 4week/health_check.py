'''
#!/usb/bin/env python3
'''

import check_cpu_usage as cpu
import check_free_space as disk
import check_memory_usage as mem
import check_network as net

print(cpu.check_cpu_usage(80))
print(disk.check_free_space(20))

threshold = 500 * 1024 * 1024  # 500MB
print(mem.check_memory_usage(threshold))

hostname = "localhost"
print(net.check_network(hostname))
