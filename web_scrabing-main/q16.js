var elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43];
sum_of_even_num=0;
sum_of_odd_num=0;
for (var i of elements){
    if (i%2===0){
        sum_of_even_num+=i
    }
    else{
        sum_of_odd_num+=i
    }
}
console.log(sum_of_even_num)
console.log(sum_of_odd_num)



