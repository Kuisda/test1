#如果tx=ty，不存在上一个状态，状态 (tx,ty) 即为起点状态；
#如果tx>ty，则上一个状态是(tx−ty,ty)；
#如果tx<ty，则上一个状态是(tx,ty−tx)


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx< tx != ty > sy:    #如果tx=ty则不存在上一个状态：因为每一次变化都是(x,y) ->x,x+y或x+y,y,不可能相等
            if tx > ty:
                tx%=ty
            else:
                ty%=tx
            if tx == sx and ty == sy:
                return True
            #其中一个取到与原值sx，sy相等后另一个每一次只能减去sy或sx
            elif tx == sx:
                return ty>sy and (ty-sy)%tx ==0
            elif ty == sy:
                return tx>sx and (tx-sx)%ty ==0
            else:
                return False            

