//sets time for timer, starts display one below time set
let time = 61;
//sets interval on the timer function to be 1 sec
let counter = setInterval(timer, 1000);
//used to make a list of good guesses
const good_word = []
//score starts at 0, increases by length of good guess
let currScore = 0;
//this shows the high score and gets previous high scores
//from local storage if there is one, otherwise it is
//set to 0
let hiScore = localStorage.getItem('highScore');
if (hiScore == null) {
    hiScore = 0;
}

//these both display the scores on the page
$("#high-score").html(`High Score: ${hiScore}`)
$("#score").html(`Current Score: ${currScore}`)

//This is what happens when a guess is submitted
//if it is good, added to list and scored
//if not, it will return proper message to user
async function workClick() {
    let word = $("#guess").val()
    console.log(word)
    const res = await axios.get("/word_check", { params: { word: word } })
    result = res.data.result;
    //message for user. Lets them know about guess
    $("#valid-msg").html(`"${word}" is ${result}`)
    if (result === 'ok') {
        if (good_word.includes(word)) {
            $("#valid-msg").html(`"${word}" has already been used`)
        } else {
            good_word.push(word)
            currScore = currScore + word.length
            $("#score").html(`Current Score: ${currScore}`)
            $("#good-list").append(`<li>${word}</li>`)
        }
    }
    $("#guess").val('')
    console.log(good_word)
    return res
}

$("#submit").on("click", function (e) {
    e.preventDefault();
    workClick();
})

function timer() {
    time -= 1;
    if (time <= 0) {
        clearInterval(counter)
        $("#submit").prop('disabled', true)
        $("#countdown").html(`TIME UP!!! PENCILS DOWN!`)
        if (currScore > hiScore) {
            hiScore = currScore
            $("#high-score").html(`High Score: ${hiScore}`)
            localStorage.setItem('highScore', currScore)
        }
        return
    }
    $("#countdown").html(`${time}`)
}
