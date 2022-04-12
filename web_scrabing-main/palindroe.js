// var string=["m","a","d","a","m"]
// new_string=[];
//     for(var i=string.length-1; i>=0;i--){
//     new_string.push(string[i])
// }
// var count=0;
// for (j=0;j<string.length;j++){
//     if (new_string[j]===string[j]){
//         count++
//     }
//     }
//     if (count===string.length){
//         console.log(new_string,"it is a palindrome")
//     }
//     else{
//         console.log(string,"it is not a palindrome")
// }




var a=require("readline-sync")
var string=a.question("enter the string:")
new_string=[];
    for(var i=string.length-1; i>=0;i--){
    new_string.push(string[i])
}
var count=0;
for (j=0;j<string.length;j++){
    if (new_string[j]===string[j]){
        count++
    }
    }
    if (count===string.length){
        console.log(new_string,"it is a palindrome")
    }
    else{
        console.log(string,"it is not a palindrome")
}

