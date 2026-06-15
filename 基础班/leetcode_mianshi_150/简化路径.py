from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split("/")
        res = []
        for path in path_list:
            if path != "..":
                res.append(path)
            elif path == "" or path == ".":
                continue
            else:
                path.pop()
        return "/" + "/".join(res)