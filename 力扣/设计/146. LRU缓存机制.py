class LinkNode(object):
    """
    双向链表
    """

    def __init__(self, key, val):
        self.key, self.value = key, val
        self.next = None
        self.last = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur_size = 0
        self.link_dict = {}

        self.head = LinkNode(-1, -1)
        self.tail = LinkNode(-1, -1)

        self.tail.last = self.head
        self.head.next = self.tail

    def get(self, key: int) -> int:
        ans_link = self.link_dict.get(key)
        if not ans_link:
            return -1
        else:
            # 将节点从链表中抽出来
            ans_link.last.next = ans_link.next
            ans_link.next.last = ans_link.last

            # 将节点放置到尾节点前一个中
            ans_link.last = self.tail.last
            ans_link.next = self.tail
            self.tail.last.next = ans_link
            self.tail.last = ans_link

            return ans_link.value

    def put(self, key: int, value: int) -> None:
        if not self.link_dict.get(key, None):
            # 新建一个节点
            new_node = LinkNode(key, value)
            self.link_dict[key] = new_node
            # 当前大小+1
            self.cur_size += 1
        else:
            new_node = self.link_dict[key]
            new_node.value = value

            # 把现存节点抽出来
            new_node.last.next = new_node.next
            new_node.next.last = new_node.last

        # 节点放到链表尾部
        new_node.next = self.tail
        new_node.last = self.tail.last
        self.tail.last.next = new_node
        self.tail.last = new_node

        # 如果已经超出了容量，就把链表头部后第一个链表移除
        if self.cur_size > self.capacity:
            delete_node = self.head.next
            delete_key = delete_node.key

            self.head.next = self.head.next.next
            self.head.next.last = self.head

            del delete_node
            self.link_dict.pop(delete_key)
            self.cur_size -= 1
    
    def traverse(self):
        node = self.head
        while node:
            print(node.key, node.value)
            node = node.next


s = LRUCache(2)
s.put(2, 1)
s.put(2, 2)

s.put(1, 1)
s.put(2, 3)
s.put(4, 1)

print(s.get(1))
print(s.get(2))