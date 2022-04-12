magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
var i=0
var v=15
while(i<(magic_square.length)){
    var col=0
    var sum=0
    while (col<magic_square.length){
        sum=sum+magic_square[i][col]
        col+=1
    i++
    }
}
console.log(sum)
var j=0;
while (j<(magic_square.length)){
    var row =0;
    var sum1=0
    while (row<(magic_square.length)){
        sum1=sum1+magic_square[row][j]
        row+=1
    j++
    }
}
console.log(sum1)
var x=magic_square[0][0]+magic_square[1][1]+magic_square[2][2]
var y=magic_square[0][2]+magic_square[1][1]+magic_square[2][0]
if (x==v){
    console.log("it is diagonal:",x)
    if (y==v){
        console.log("diagonal:",v)
        if (sum==sum1 && sum1==x && x==y){
            console.log("it is a magic square")
        }
        else{
            console.log("it is not a magic square")
        }
    }else{
        console.log("not diagonal")
    }
}
else{
    console.log("nothing")
}