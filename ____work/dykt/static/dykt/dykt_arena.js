const startButton = document.getElementById('start-btn')
const nextButton = document.getElementById('next-btn')
const questionContainerElement = document.getElementById('question_area')
const questionElement = document.getElementById('question')
const answerButtonsElement = document.getElementById('answer-buttons')
const bodyArea = document.getElementById('question_zone')
const quizDone = document.getElementById('quiz-done')

let scoreNumber = document.getElementById('score-number')
let shuffledQuestions, currentQuestionIndex



let score = 0

startButton.addEventListener('click', startGame)

// making the next button work
nextButton.addEventListener('click', () => {
  currentQuestionIndex++
  setNextQuestion()
})


function startGame() {
  console.log("start game!")
  startButton.classList.add('hide_me')

  // shuffling the questions so they don't show in the same order
  shuffledQuestions = questions.sort(() => Math.random() - .5)  // sort + then sort - then sort + again
  currentQuestionIndex = 0  // starting from the first question in our list (list is continuously changing)
  questionContainerElement.classList.remove('hide_me')
  setNextQuestion()
}

function setNextQuestion() {
  resetState()
  showQuestion(shuffledQuestions[currentQuestionIndex]) //shows question 1 in the continuously changing list
}

function showQuestion(question) {
  // showing questions in html
  questionElement.textContent = question.question // changes the question in html
  // showing answer options in html
  question.answers.forEach(answer => {
    const button = document.createElement('button')
    button.textContent = answer.text
    button.classList.add('btn')
    //checking if button is correct (correct was set it the question)
    if (answer.correct) {
      button.dataset.correct = answer.correct
    }
    button.addEventListener('click', selectAnswer)
    answerButtonsElement.appendChild(button)
  })

  scoreNumber.textContent = score
}

// hide_mes previous answer options
function resetState() {
  clearStatusClass(bodyArea)
  nextButton.classList.add('hide_me')
  while (answerButtonsElement.firstChild) {  // checking if there is a first child
    answerButtonsElement.removeChild(answerButtonsElement.firstChild) // removes the first child
  }
}

function selectAnswer(e) {
  const selectedButton = e.target  // checking which button we selected
  const correct = selectedButton.dataset.correct // checking if is correct

  // below we checking if its correct then adding the class. if wrong then adding the class
  setStatusClass(bodyArea, correct)
  let liveArray = Array.from(answerButtonsElement.children) // making an array of all buttons
  liveArray.forEach(button => {
    setStatusClass(button, button.dataset.correct)
  })

  // check if we have any questions remaining
  if (shuffledQuestions.length > currentQuestionIndex + 1) { // we have more questions
    nextButton.classList.remove('hide_me')
  } else {
    startButton.textContent = "Restart"
    quizDone.classList.remove("hide_me")
  }

}

function setStatusClass(element, correct) {
  clearStatusClass(element) // clearing the status from all buttons
  if (correct) {
    element.classList.add('correct')
  } else {
    element.classList.add('wrong')
  }
}

function clearStatusClass(element) {
  element.classList.remove('correct')
  element.classList.remove('wrong')
}


// QUESTIONS ########################################################

// questionList
// qOptions

// All right answers:
let questionListProgress = questionListBroken.replace('[', '')
questionListProgress = questionListProgress.replace(']', '')
let questionList = questionListProgress.split(', ')

// All choice options

let brokenList = qOptions.replace('[[', '[')
brokenList = brokenList.replace(']]', ']')
let fixedList = brokenList.replace('[', '').split('], [')
q0Choices = fixedList[0].split(', ')
q1Choices = fixedList[1].split(', ')
q2Choices = fixedList[2].split(', ')
q3Choices = fixedList[3].split(', ')
q4Choices = fixedList[4].split(', ')
q5Choices = fixedList[5].split(', ')
q6Choices = fixedList[6].split(', ')
q7Choices = fixedList[7].split(', ')
q8Choices = fixedList[8].split(', ')
q9Choices = fixedList[9].split(', ')

const questions = [
  {
    question: questionList[0],
    answers: [
      {'text': q0Choices[0], correct: false},
      {'text': q0 , correct: true},
      {'text': q0Choices[1], correct: false},
      {'text': q0Choices[2], correct: false},
    ]
  },
  {
    question: questionList[1],
    answers: [
      {'text': q1Choices[0], correct: false},
      {'text': q1Choices[1], correct: false},
      {'text': q1Choices[2], correct: false},
      {'text': q1 , correct: true},
    ]
  },
  {
    question: questionList[2],
    answers: [
      {'text': q2 , correct: true},
      {'text': q2Choices[0], correct: false},
      {'text': q2Choices[1], correct: false},
      {'text': q2Choices[2], correct: false},
    ]
  },
  {
    question: questionList[3],
    answers: [
      {'text': q3Choices[0], correct: false},
      {'text': q3Choices[1], correct: false},
      {'text': q3 , correct: true},
      {'text': q3Choices[2], correct: false},
    ]
  },
  {
    question: questionList[4],
    answers: [
      {'text': q4Choices[0], correct: false},
      {'text': q4 , correct: true},
      {'text': q4Choices[1], correct: false},
      {'text': q4Choices[2], correct: false},
    ]
  },
  {
    question: questionList[5],
    answers: [
      {'text': q5 , correct: true},
      {'text': q5Choices[0], correct: false},
      {'text': q5Choices[1], correct: false},
      {'text': q5Choices[2], correct: false},
    ]
  },
  {
    question: questionList[6],
    answers: [
      {'text': q6Choices[0], correct: false},
      {'text': q6Choices[1], correct: false},
      {'text': q6Choices[2], correct: false},
      {'text': q6 , correct: true},
    ]
  },
  {
    question: questionList[7],
    answers: [
      {'text': q7Choices[0], correct: false},
      {'text': q7 , correct: true},
      {'text': q7Choices[1], correct: false},
      {'text': q7Choices[2], correct: false},
    ]
  },
  {
    question: questionList[8],
    answers: [
      {'text': q8Choices[0], correct: false},
      {'text': q8 , correct: true},
      {'text': q8Choices[1], correct: false},
      {'text': q8Choices[2], correct: false},
    ]
  },
  {
    question: questionList[9],
    answers: [
      {'text': q9Choices[0], correct: false},
      {'text': q9Choices[1], correct: false},
      {'text': q9 , correct: true},
      {'text': q9Choices[2], correct: false},
    ]
  },
]
