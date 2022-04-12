question_list = ["How many continents are there?", 
                "What is the capital of India?",    
                "NG mei kaun se course padhaya jaata hai?"]
options_list = [["Four", "Nine", "Seven", "Eight"],
                ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
                ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
// # har ek question ke liye, uski solution key (yeh index nahi hai)
solution_list = [3, 4, 1]
answer_list=[
    ["1.four","3.seven"],
    ["2.bhopal","4.delhi"],
    ["1.software engenering","4.agriculture"]
]
function kbc_game(){
console.log("WELCOME TO COROROATI (kbc)")
i=0
s=0
count=0
while (i<question_list.length){
    console.log(question_list[i])
    j=0
    k=1
    while (j<options_list[i].length){
        console.log(k,".",options_list[i][j])
        k=k+1
        j=j+1
    }
    var a=require("readline-sync")
    var num1=a.question("do u want 50 50 lifeline")
    if (num1=="yes"){
        console.log("50 50 life line")
        if (count<1){
            console.log(answer_list[i])
            num2=a.question("enter the answer")
            if (num2==solution_list[i]){
                s=+10000
                console.log("ur answer is correct")
                console.log("u win Rs/",s)
            }
            else{
                console.log("ur answer is incorrect")
                break
            }
            count=count+1
        }
        else{
            console.log("u already use lifeline")
            var m=a.question("enter ur answer")
            if (m==solution_list[i]){
                console.log("congrates ur answer is right")
                s=+10000
                console.log("u win",s)
            }
            else{
                console.log("ur answer is wrong")
                console.log("u can play again")
                console.log("u win",s)
                break


            }
        }
    }
    else{
        var k=a.question("enter ur answer")
        if (k==solution_list[i]){
            console.log("right answer")
            s+=10000
            console.log("u win Rs/",s)
            console.log("congrates jabeena you won the game")
        }
        else{
            console.log("no chance")
            console.log("ur answer is wrong")
            break
        }

    }
    i++

}
}
kbc_game()


