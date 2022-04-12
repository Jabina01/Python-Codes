// var i=1
// var sum=0;
// var b=require("readline-sync")
// var num=b.questionInt("enter the number")
// while (i<=num){
//     str=b.question("enter the number")
//     sum=sum+str
//     i++
// }
// console.log(sum)



// var array=[1,3,2,4,[5,5],5,6,6,3]
// var i=0;
// var sum=0;
// while (i<array.length){
//     if (Array.isArray(array[i])==true){
//         var j=0;
//         while (j<array[i].length){
//             sum+=array[i][j]
//             j++  
//         }
//     }
//     else{
//         sum=sum+array[i]
//     }
//     i++
// }
// console.log(sum)







// a = [[1,2,3,4,],[1,2,3],[1,2]]
// i=0
// b=[]
// sum=0
// while i<len(a):
//     j=0;
//     while j<len(a[i]):
//         if a[i][j] not in b:
//             b.append(a[i][j])
//         if b[i]==a[i][j]:
//             sum+=b[i]
//         j+=1
    // i+=1
// print(sum)


// array=[[1,2,3],[1,2,3,5],[1,2]]
// var i=0;
// var sum=0;
// var b=[]
// while(i<array.length){
//     j=0;
//     while (j<array.length[i]){
//         if (!array[i][j].includes(b)){
//             b.push(array[i][j])
//         if (b[i]==array[i][j]){
//             sum=sum+b[i]
//         }
//         j++
//         }
//     }
//     i++
// }
// console.log(sum)




// var list1=[1,2,1,3,2,2,4,3,4,4,5,2,5]
// var i=0;
// var list2=[];
// while (i<list1.length){
//     h=list1[i]
//     if (!list2.includes(h)){
//         list2.push(h)
//     }
//     i++
// }
// console .log(list2)
// var i=0;
// while (i<list2.length){
//     count=0
//     var j=0;
//     while (j<list1.length){
//         if (list1[i]==list2[i]){
//             count++
//         }
//         j++
//     }
//     i++
// }
// console.log(list2,count/2)



// var list1=[1,2,1,3,2,2,4,3,4,4,5,2,5]
// if (list1.includes(7)){
//     console.log("yes")
// }
// else{
//     console.log("no")
// }



// var list1=[[1,2,1,3],[2,2,4],[3,4,4,5,2,5]]
// var array=[]
// for (var i=0;i<list1.length;i++){
//     for (var j=0;j<list1[i].length;j++){
//         var evenNumbers=list1[i][j]
//         if (evenNumbers%2==0){
//             array.push(evenNumbers)
//         }
//     }
// }
// console.log(array)




// list=[1,2,3,4,5]
// list[list.length]=6
// console.log(list)


// var a=new Array(1,2,5,4,3,2,1)
// console.log(a)




// function dic(a){
//     var a=require("readline-sync")
//     var b=["zero","one","two","three","four","five","six","seven","eight","nine"]
//     var num=a.question("enter the number:")
//     var i=0
//     var m={}
//     while (i<num.length){
//         s=(num[i])
//         m[s]=b[s]
//         i++
//     }
//     console.log(m)
// }
// dic()



// var chr=[['g',"f","g"],['i','s'],['b','e','s','t']]
// var a=''
// var i=0
// while (i<chr.length){
//     j=0
//     while (j<chr[i].length){
//         a=a+chr[i][j]
//         j++
//     }
//     i++
// }
// console.log(a)
// console.dir(a)


