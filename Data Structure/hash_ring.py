import hashlib
import bisect

md5 = hashlib.md5()  # 应用MD5算法
data = "11vcxvgdfdfdfdfdfdfdfdfdf    dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfcxvxc"

md5.update(data.encode('utf-8'))
print(md5.hexdigest())
md5 = hashlib.sha256()
data1 = "11vcxvgdfdfdfdfdfdfdfdfdf    dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfcxvxc"
md5.update(data1.encode('utf-8'))
tt = md5.hexdigest()
print(tt)
print(int(tt, 16))


class ConsistentHashRing:
    def __init__(self, virtual_nums=4):
        self._virtual_nums = virtual_nums  # 默认为4个虚拟节点
        self._nodes = {}  # _nodes存放所有节点，key为虚拟节点的hash值，val为真实ip
        self._keys = []  # 存放所有虚拟节点的hash值，为有序数组，用于快速查找hash的key

    @staticmethod
    def _hash(key):  # 用md5来实现hash值
        md5_str = hashlib.md5(key.encode("utf8")).hexdigest()
        return int(md5_str, 16)  # 返回2进制数

    def _repl_iterator(self, nodename):
        """根据编号和nodename，给每个虚拟节点取名后赋值hash"""

        return (self._hash("%s:%s" % (nodename, i)) for i in range(self._virtual_nums))

    def __setitem__(self, nodename, node):  # nodename为自定义标识名字，比如node1, node:192.168.4.1
        for hash_ in self._repl_iterator(nodename):
            if hash_ in self._nodes:
                raise ValueError("Node name %r is "
                                 "already present" % nodename)
            self._nodes[hash_] = node
            bisect.insort(self._keys, hash_)  # 二分法插入

    def __delitem__(self, nodename):  # 删除要同时删除_nodes和_keys的值
        for hash_ in self._repl_iterator(nodename):
            del self._nodes[hash_]
            index = bisect.bisect_left(self._keys, hash_)
            del self._keys[index]

    def __getitem__(self, key):  # 通过二分法快速查找
        hash_ = self._hash(key)
        start = bisect.bisect(self._keys, hash_)  # 返回这个key应该插入的位置，如果是最右边，则属于第0个节点
        if start == len(self._keys) - 1:
            start = 0
        return self._nodes[self._keys[start]]

    @property
    def nodes(self):
        return self._nodes

    @property
    def keys(self):
        return self._keys


consistent_hash_ring = ConsistentHashRing()
consistent_hash_ring["node1"] = "192222.168.4.1"
consistent_hash_ring["node2"] = "192222.168.4.2"
consistent_hash_ring["node3"] = "192222.168.4.3"
consistent_hash_ring["node4"] = "192222.168.4.4"

val1 = consistent_hash_ring["10_hash"]  # 加入key取名为主键+_hash，那第10个主键的key就是 10_hash
val2 = consistent_hash_ring["20_hash"]
val3 = consistent_hash_ring["30_hash"]  # 加入key取名为主键+_hash，那第10个主键的key就是 10_hash
val4 = consistent_hash_ring["40_hash"]
val5 = consistent_hash_ring["50_hash"]  # 加入key取名为主键+_hash，那第10个主键的key就是 10_hash
val6 = consistent_hash_ring["60_hash"]
print("哈希环存放的键值对为：", consistent_hash_ring.nodes)
print("哈希环当前所有的虚拟节点集合为：", consistent_hash_ring.keys)
print("10_hash存放的机器位于：", val1)
print("20_hash存放的机器位于：", val2)
print("30_hash存放的机器位于：", val3)
print("40_hash存放的机器位于：", val4)
print("50_hash存放的机器位于：", val5)
print("60_hash存放的机器位于：", val6)

del consistent_hash_ring["node1"]

