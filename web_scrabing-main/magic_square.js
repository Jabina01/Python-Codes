magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
// var col=0
// var row=0
// var diagonal=0
// for (var i=0;i<magic_square.length;i++){
//     for( var j=0;j<magic_square[i].length;j++){
//         diagonal=col+row+diagonal+magic_square[i][j]

//     }
// }
// console.log(diagonal)

// if (col==row==diagonal){
//     console.log("it is a magic square")
// }
// else{
//     console.log("it is not a magic square")
// }
var r=0
while (r<magic_square.length){
    var j=0
    var sum=0
    while (j<magic_square[r].length){
        sum=sum+magic_square[r][j]
        j=j+1
    }
    r=r+1
}
console.log(sum)

var d=0
while (d<magic_square.length){
    var j=0
    var sum1=0
    while (j<magic_square[d].length){
        sum1=sum1+magic_square[d][j]
        j=j+1
    }
    d=d+1
}
console.log(sum1)



var c=0
var b=0
var sum3=0
while (c<magic_square.length){
    sum3=sum3+magic_square[c][b]
    c=c+1
}
console.log(sum3)

