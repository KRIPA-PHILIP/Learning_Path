function ResourcesCard({ resources }) {

  return (

    <div className="bg-white rounded-3xl shadow-xl p-8 border border-gray-100">

      <div className="flex items-center gap-3 mb-5">

        <div className="w-12 h-12 bg-cyan-100 rounded-xl flex justify-center items-center text-2xl">
          📚
        </div>

        <div>

          <h2 className="text-2xl font-bold">
            Resources
          </h2>

          <p className="text-gray-500">
            Best learning materials
          </p>

        </div>

      </div>

      <div className="whitespace-pre-wrap leading-8">

        {resources || "Courses, YouTube channels and documentation will appear here."}

      </div>

    </div>

  )

}

export default ResourcesCard