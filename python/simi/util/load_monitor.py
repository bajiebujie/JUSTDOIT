#! encoding: utf8
import os

from simi.util.misc import get_host_ip


class LoadMonitor(object):
    host_ip = None

    def __init__(self):
        self.host_ip = get_host_ip()

    def get_byte_size(self, x):
        x = x.upper()
        unit = 1
        if x.endswith('B'):
            unit = 1
        elif x.endswith('K'):
            unit = 1024
        elif x.endswith('M'):
            unit = 1024 * 1024
        elif x.endswith('G'):
            unit = 1024 * 1024 * 1024
        else:
            return int(x)
        size = int(x[:-1]) * unit
        return size

    def get_system_load(self):
        sample_count = 1
        r = os.popen('dstat 1 %s' % sample_count)
        lines = r.readlines()
        lines = lines[-sample_count:]
        cpu_load = 0
        disk_load = 0
        net_load = 0
        MAX_DISK_SPEED = 800 * 1024 * 1024
        MAX_NET_SPEED = 1000 * 1024 * 1024
        for line in lines:
            # app_log.warning(line)
            item = line.split('|')
            cpu_item = item[0].split(' ')
            cpu_item = [x for x in cpu_item if x]
            cpu_idle = int(cpu_item[2])
            cpu_load += 100 - cpu_idle
            disk_item = item[1].split(' ')
            disk_item = [x for x in disk_item if x]
            disk_read = self.get_byte_size(disk_item[0])
            disk_write = self.get_byte_size(disk_item[1])
            disk_load += 100.0 * (disk_read + disk_write) / MAX_DISK_SPEED
            net_item = item[2].split(' ')
            net_item = [x for x in net_item if x]
            net_recv = self.get_byte_size(net_item[0])
            net_send = self.get_byte_size(net_item[1])
            net_load += 100.0 * (net_recv + net_send) / MAX_NET_SPEED
            # app_log.warning('cpu_idle=%s, disk_read=%s, disk_write=%s, net_recv=%s, net_send=%s' % (
            #     cpu_idle, disk_read, disk_write, net_recv, net_send))
        sample_count = len(lines)
        cpu_load /= sample_count
        disk_load /= sample_count
        net_load /= sample_count
        load = max(cpu_load, disk_load, net_load)
        # app_log.warning('cpu_load=%s, disk_load=%s, net_load=%s, load=%s' % (cpu_load, disk_load, net_load, load))
        return load

    def start(self):
        while True:
            try:
                load = self.get_system_load()
                print load
            except Exception as ex:
                print str(ex)
                break
