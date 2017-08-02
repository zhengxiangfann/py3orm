#coding:utf-8

class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Sloution(object):

    def swap_pairs(self, head):
        if head != None and head.next != None:
            next = head.next
            head.next = next
            next.next = self.swap_pairs(next.next)
            next.next = head
            return next
        return head




if __name__ == '__main__':


    # dict = {'name': 'earth', 'port': '80'}
    items = [('name', 'earth'), ('port', '80')]
    dict2 = dict(items)
    dict1 = dict((['name', 'earth'], ['port', '80']))

    dict1 = {}.fromkeys(('x', 'y'), -1)
    dict = {'x': -1, 'y': -1}
    dict2 = {}.fromkeys(('x', 'y'))
    dict2 = {'x': None, 'y': None}


    def _recursion_merge_sort2(l1, l2, tmp):

        if len(l1) == 0 or len(l2) == 0:
            tmp.extend(l1)
            tmp.extend(l2)
            return tmp

        else:
            if l1[0] < l2[0]:
                tmp.append(l1[0])
                del l1[0]
            else:
                tmp.append(l2[0])
                del l2[0]
            return _recursion_merge_sort2(l1, l2, tmp)


    def recursion_merge_sort2(l1, l2):
        return _recursion_merge_sort2(l1, l2, [])


    def loop_merge_sort(l1, l2):
        tmp = []
        while len(l1) > 0 and len(l2) > 0:
            if l1[0] < l2[0]:
                tmp.append(l1[0])
                del l1[0]
            else:
                tmp.append(l2[0])
                del l2[0]
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp

    def binarySearch(l, t):
        low, high = 0, len(l) - 1
        while low < high:
            print
            low, high
            mid = (low + high) / 2
            if l[mid] > t:
                high = mid
            elif l[mid] < t:
                low = mid + 1
            else:
                return mid
        return low if l[low] == t else False

