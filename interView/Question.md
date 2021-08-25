### 1.腾讯面试题
- 题干：
    - 方格棋盘上，散落n颗珠子【n>3】，珠子位置在横线与纵线的交叉点上。沿着盘上的格子线画线条，线条可以转弯，把珠子连起来，达到3颗即算成串。
求最短的珠串长度。
        - 示例
>       输入：
>       [0,0],[10,2],[11,11],[10,10]]
>       输出:
>       4

- 尝试作答[文件](src/interview.html)
```
function sub(){
            input=document.getElementById('in').value
            input=input.split(',')
            let res=test([[0,0],[0,2],[10,11],[1,1],[10,10],[10,9]])
            document.getElementById('out').value=res
        }

        function test(arr){
            let martrix=[]
            let distan=Infinity
            for(let p1=0;p1<arr.length;p1++){
                let row=[]
                for(let p2=0;p2<arr.length;p2++){
                    if(p2<p1){
                        row.push(martrix[p2][p1])
                    }else {
                        row.push(dist(arr[p1],arr[p2]))
                    }
                }
                martrix.push(row)
            }
            for(let row=0;row<martrix.length;row++){
                let res=[]
                let rowDist=0
                let recordIndex=[]
                let martrixRow =martrix[row]
                while (res.length<2){
                    minNum=Infinity
                    indexX=0
                    for(let item=0;item<martrixRow.length;item++){
                        if(martrixRow[item]<minNum && res.indexOf(item)==-1&& martrixRow[item]!=0){
                            minNum=martrixRow[item]
                            indexX=item
                        }
                    }
                    res.push(indexX)
                    recordIndex.push(arr[indexX])

                }
                recordIndex.push(arr[row])
                rowDist=lineLength(recordIndex[0],arr[row])+lineLength(recordIndex[1],arr[row])
                distan=distan<rowDist?distan:rowDist
            }
            return distan


        }
        function dist(p1,p2) {
            x=p1[0]-p2[0]
            y=p1[1]-p2[1]
            return Math.sqrt(x*x+y*y)
        }
        function lineLength(p1,p2){
            x=Math.abs(p1[0]-p2[0])
            y=Math.abs(p1[1]-p2[1])
            return x+y
        }

```
