class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        sorted_list_s = list.sort(list_s)
        sorted_list_t = list.sort(list_t)
        if list_s == list_t:
            return True
        else:
            return False