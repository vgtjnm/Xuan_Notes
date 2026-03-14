pt ={
            "(":1,  "{":2,  "[":3,
            ")":-1, "}":-2, "]":-3
        }
        stack = [1]

        for i in s:
            num  = pt[i]
            if num > 0:
                stack.append(num)
            else:
                leng = len(stack)
                nums = stack[leng-1]
                ans = nums-num
                if ans != 0:
                    return False
                stack.pop()
        if(len(stack)>1):
            return False
        else:
            return True