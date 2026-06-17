function GoalForm({

    goal,

    setGoal,

    generateLearningPath

}) {

    return (

        <div className="bg-white rounded-3xl shadow-xl p-10 mt-10">

            <input

                value={goal}

                onChange={(e)=>setGoal(e.target.value)}

                placeholder="Example : FastAPI Developer"

                className="w-full border-2 border-gray-200 rounded-xl p-5 text-lg"

            />

            <button

                onClick={generateLearningPath}

                className="primary-btn mt-8 w-full"

            >

                Generate Learning Path

            </button>

        </div>

    )

}

export default GoalForm