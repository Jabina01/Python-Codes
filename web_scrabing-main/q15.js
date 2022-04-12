var elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
count_of_even_numbers=0;
count_of_odd_numbers=0;
for (var i of elements){
    if (i%2==0){
        count_of_even_numbers+=1
    }
    else{
        count_of_odd_numbers+=1
    }
}
console.log(count_of_even_numbers)
console.log(count_of_odd_numbers)


